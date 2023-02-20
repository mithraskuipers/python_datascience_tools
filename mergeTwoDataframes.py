import pandas as pd

def mergeTwoDataframes(df1, df2, on_variable):
	merged_df = pd.merge(df1, df2, on=on_variable)
	return merged_df
