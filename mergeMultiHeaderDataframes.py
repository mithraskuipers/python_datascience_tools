import pandas as pd

def mergeMultiHeaderDataframes(df1, df2, merge_cols):
    """
    Merge two multi-column header DataFrames on user specified columns.
    
    Parameters:
    -----------
    df1, df2: pandas DataFrame
        Two DataFrames to merge.
    
    merge_cols: list
        List of column names to merge the DataFrames on.
        
    Returns:
    --------
    pandas DataFrame
        The merged DataFrame.
    """
    # Filter out any empty column names
    merge_cols = [col for col in merge_cols if col]

    # Merge the DataFrames on the specified columns
    merged_df = pd.merge(df1, df2, on=merge_cols)
    return merged_df

'''
df1:
| "id"  |"name"	|"name"	|"name" |
|		|"first"	|"last" |"nick"	|
|-------|-------|-------|-------|
|0		|"mith"	|"kuip" |"mith"	|
|1		|"bas"	|"meij" |"bassi"	|
|2		|"rick"	|"brun" |"ricky"	|

df2:
| "id"  |"name"	|"name" |
|		|"pet"	|"bff"  |
|-------|-------|-------|
|0		|"sjaak"	|"fredd"|
|1		|"fredd"	|"bink" |
|2		|"lola"	|"sjaak"|

merged_df = merge_dataframes(df1, df2, ["id", ""])

merged_df:
| "id"  |"name"	|"name"	|"name" |"name" |"name" |
|		|"first"	|"last" |"nick"	|"pet"  |"bff"  |
|-------|-------|-------|-------|-------|-------|
|0		|"mith"	|"kuip" |"mith"	|"sjaak"|"fredd"|
|1		|"bas"	|"meij" |"bassi"	|"fredd"|"bink" |
|2		|"rick"	|"brun" |"ricky"	|"lola" |"sjaak"|
'''
