import pandas as pd
import os




def analyze_csv(path):
    df=pd.read_csv(path)
    return {
            "df_shape": df.shape,
        "head": df.head().to_html(),
        "tail": df.tail().to_html(),
        "dtypes": df.dtypes.to_string(),
        "duplicated": int(df.duplicated().sum()),
        "isnull": df.isnull().sum().to_string()

    }