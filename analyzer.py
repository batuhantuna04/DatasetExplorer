import pandas as pd
import os

path=os.path.join("uploads","data.csv")
df=pd.read_csv(path)


def analyze_csv():
    return {
            "df_shape": df.shape,
        "head": df.head().to_html(),
        "tail": df.tail().to_html(),
        "dtypes": df.dtypes.to_string(),
        "duplicated": int(df.duplicated().sum()),
        "isnull": df.isnull().sum().to_string()

    }