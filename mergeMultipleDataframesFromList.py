import pandas as pd

def mergeMultipleDataframesFromList(dataframes, on_variable):
	merged_df = dataframes[0]
	for i in range(1, len(dataframes)):
		merged_df = pd.merge(merged_df, dataframes[i], on=on_variable)
	return merged_df
