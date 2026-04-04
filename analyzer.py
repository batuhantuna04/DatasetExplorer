import pandas as pd
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64


def analyze_csv(path):
    df = pd.read_csv(path)

    duplicate = duplicate_info(df)
    quality = data_score(df)
    suggest_chart = chart_suggestion(df)
    generate_chart = generate_charts(df, suggest_chart["suggestions"])

    info_list = []
    for col in df.columns:
        non_null_count = df[col].notnull().sum()
        dtype = str(df[col].dtype)
        info_list.append({
            "Column": col,
            "Non-Null Count": f"{non_null_count} non-null",
            "Data Type": dtype
        })
    df_info_html = pd.DataFrame(info_list).to_html(classes="table table-striped", border=0, index=False)

    df_describe_html = (
        df.describe(include="all")
        .fillna("-")
        .to_html(classes="table table-striped", border=0, float_format="{:.2f}".format)
    )

    return {
        "df_shape":   df.shape,
        "df_info":    df_info_html,       
        "df_describe": df_describe_html, 
        "head":       df.head().to_html(classes="table table-striped", border=0),
        "tail":       df.tail().to_html(classes="table table-striped", border=0),
        "dtypes":     df.dtypes.astype(str).rename("Data Type").reset_index().to_dict(orient="records"),
        "duplicate":  duplicate,
        "isnull":     df.isnull().sum().rename("Missing Count").reset_index().to_dict(orient="records"),
        "quality":    quality,
        "suggestion": suggest_chart,
        "chart":      generate_chart["chart"],
    }


def duplicate_info(df):
    total_row = df.shape[0]
    duplicate_count = df.duplicated().sum()

    duplicate_ratio = round((duplicate_count / total_row) * 100, 2) if total_row else 0

    if duplicate_ratio == 0:
        status = "Clear!"
    elif duplicate_ratio < 5:
        status = "Low Duplicate"
    elif duplicate_ratio < 15:
        status = "Medium Duplicate"
    else:
        status = "High Duplicate"

    return {
        "total_row":       total_row,
        "duplicate_count": int(duplicate_count),
        "duplicate_ratio": duplicate_ratio,
        "status":          status,
    }


def data_score(df):
    total_row    = df.shape[0]
    total_column = df.shape[1]
    total_cell   = total_row * total_column

    null_count = df.isnull().sum().sum()
    null_ratio_decimal  = (null_count / total_cell) if total_cell else 0
    null_ratio_percent  = round(null_ratio_decimal * 100, 2)
    null_score          = 40 * null_ratio_decimal

    duplicate               = duplicate_info(df)
    duplicate_ratio_decimal = duplicate["duplicate_ratio"] / 100
    duplicate_score         = 25 * duplicate_ratio_decimal

    empty_column_count = int(df.isnull().all().sum()) if total_column else 0
    empty_column_ratio = (empty_column_count / total_column) if total_column else 0
    empty_score        = 20 * empty_column_ratio

    score = round(max(0, min(100, 100 - null_score - duplicate_score - empty_score)), 2)

    if score >= 90:
        label = "Excellent"
    elif score >= 70:
        label = "Good"
    elif score >= 50:
        label = "Medium"
    else:
        label = "Poor"

    return {
        "score":               score,
        "label":               label,
        "null_count":          int(null_count),
        "null_ratio":          null_ratio_percent,
        "null_score":          round(null_score, 2),
        "duplicate_score":     round(duplicate_score, 2),
        "empty_column_count":  empty_column_count,
        "empty_score":         round(empty_score, 2),
    }


def chart_suggestion(df):
    suggestions = []

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            suggestions.append({"column": col, "chart": "histogram"})
        elif pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_categorical_dtype(df[col]):
            if df[col].nunique(dropna=True) <= 20:
                suggestions.append({"column": col, "chart": "bar_chart"})

    return {"suggestions": suggestions}


def generate_charts(df, suggestions):
    charts = []

    for suggestion in suggestions:
        chart_type = suggestion["chart"]
        plt.figure(figsize=(6, 4))

        try:
            if chart_type == "histogram":
                col = suggestion["column"]
                sns.histplot(df[col].dropna(), kde=True, color="#2196f3")

            elif chart_type == "boxplot":
                col = suggestion["column"]
                sns.boxplot(x=df[col].dropna(), color="#2196f3")

            elif chart_type == "bar_chart":
                col = suggestion["column"]
                df[col].value_counts(dropna=False).head(20).plot(kind="bar", color="#2196f3")
                plt.xticks(rotation=45, ha="right")

            elif chart_type == "pie_chart":
                col = suggestion["column"]
                df[col].value_counts(dropna=False).head(10).plot(kind="pie", autopct="%1.1f%%")

            elif chart_type == "scatter_plot":
                x = suggestion["columns"][0]
                y = suggestion["columns"][1]
                sns.scatterplot(x=df[x], y=df[y], color="#2196f3")

            plt.title(f"{suggestion.get('column', '')} — {chart_type}", fontsize=13)
            plt.tight_layout()

            buf = io.BytesIO()
            plt.savefig(buf, format="png", bbox_inches="tight", dpi=110)
            plt.close()
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode("utf-8")
            buf.close()

            charts.append({
                "base64":  img_base64,
                "type":    chart_type,
                "column":  suggestion.get("column", " vs ".join(suggestion.get("columns", []))),
            })

        except Exception as e:
            print("Chart error:", e)
            plt.close()

    return {"chart": charts}