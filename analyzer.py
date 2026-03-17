import pandas as pd
import os



def analyze_csv(path):
    df=pd.read_csv(path)
    duplicate=duplicate_info(df)
    quality=data_score(df)

    return {
            "df_shape": df.shape,
        "head": df.head().to_html(),
        "tail": df.tail().to_html(),
        "dtypes": df.dtypes.to_string(),
        "duplicate":duplicate,
        "isnull": df.isnull().sum().to_string(),
        "quality":quality
 
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
