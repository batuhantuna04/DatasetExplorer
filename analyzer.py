import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os



def analyze_csv(path):
    df=pd.read_csv(path)
    duplicate=duplicate_info(df)
    quality=data_score(df)
    suggest_chart=chart_suggestion(df)

    return {
            "df_shape": df.shape,
        "head": df.head().to_html(),
        "tail": df.tail().to_html(),
        "dtypes": df.dtypes.reset_index(name="Data Type").to_dict(orient="records"),
        "duplicate":duplicate,
        "isnull": df.isnull().sum().reset_index(name="Missing Count").to_dict(orient="records"),
        "quality":quality,
        "suggestion":suggest_chart
 
    }

def duplicate_info(df):
    total_row=df.shape[0]
    duplicate_count=df.duplicated().sum()
   
    if total_row==0:
        duplicate_ratio=0
    else:
        duplicate_ratio=(duplicate_count/total_row)*100

    duplicate_ratio=round(duplicate_ratio,2)


    if duplicate_ratio==0:
        status="Clear!"
    elif duplicate_ratio < 5:
        status="Low Duplicate"
    elif duplicate_ratio <15:
        status="Medium Duplicate"
    else:
        status="High Duplicate"

    return{
        "total_row":total_row,
        "duplicate_count":int(duplicate_count),
        "duplicate_ratio":duplicate_ratio,
        "status":status
    }



def data_score(df):
    total_row = df.shape[0]
    total_column = df.shape[1]
    total_cell = total_row * total_column

    null_count = df.isnull().sum().sum()

    if total_cell == 0:
        null_ratio_decimal = 0
    else:
        null_ratio_decimal = null_count / total_cell

    null_ratio_percent = round(null_ratio_decimal * 100, 2)
    null_score = 40 * null_ratio_decimal

    duplicate = duplicate_info(df)
    duplicate_ratio_decimal = duplicate["duplicate_ratio"] / 100
    duplicate_score = 25 * duplicate_ratio_decimal

    if total_column==0:
        empty_column_count=0
        empty_column_ratio=0
    else:
        empty_column_count=(df.isnull().all().sum())
        empty_column_ratio=empty_column_count/total_column

    empty_score=20*empty_column_ratio

    #Final score
    total_penalty=null_score+duplicate_score+empty_score
    score=100-total_penalty
    score=max(0,min(100,score))
    score=round(score,2)

    #Label
    if score>=100:
        label="Excellent"
    elif score>=70:
        label="Good"
    elif score>=50:
        label="Medium"
    else:
        label="Poor"

    return {
        "score": score,
        "label": label,
        "null_count": int(null_count),
        "null_ratio": null_ratio_percent,
        "null_score": round(null_score, 2),
        "duplicate_score": round(duplicate_score, 2),
        "empty_column_count": int(empty_column_count),
        "empty_score": round(empty_score, 2),
    }

def chart_suggestion(df):
    suggestions = []

    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns

    # Numerical kolonlar
    for col in numerical_cols:
        suggestions.append({
            "column": col,
            "chart": "histogram"
        })
        suggestions.append({
            "column": col,
            "chart": "boxplot"
        })

    # Categorical kolonlar
    for col in categorical_cols:
        unique_count = df[col].nunique()

        if unique_count <= 20:
            suggestions.append({
                "column": col,
                "chart": "bar_chart"
            })

        if unique_count <= 10:
            suggestions.append({
                "column": col,
                "chart": "pie_chart"
            })

    # Scatter (iki numeric)
    if len(numerical_cols) >= 2:
        suggestions.append({
            "columns": list(numerical_cols[:2]),
            "chart": "scatter_plot"
        })
    suggestions=suggestions[:4]
    return {"suggestions":suggestions}
