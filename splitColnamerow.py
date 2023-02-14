import pandas as pd

def splitColnamerow(df, split_char='_'):
    # Create a new dataframe with a MultiIndex for the column names
    new_cols = pd.MultiIndex.from_tuples([(col.split(split_char, maxsplit=1) + ['', ''][:2-len(col.split(split_char, maxsplit=1))] if split_char in col else [col, '']) for col in df.columns])
    new_df = pd.DataFrame(columns=new_cols)

    # Copy the data from the old dataframe to the new dataframe
    for col in new_cols:
        if col[1]:
            new_df[(col[0], col[1])] = df[col[0] + split_char + col[1]]
        else:
            new_df[(col[0], '')] = df[col[0]]

    return new_df
