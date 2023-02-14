import pandas as pd

def insertRows(df, index, num_rows=1):
    empty_row = pd.Series([None] * len(df.columns), index=df.columns)
    for i in range(num_rows):
        df = pd.concat([df.iloc[:index], empty_row.to_frame().T, df.iloc[index:]]).reset_index(drop=True)
        index += 1
    return (df)
