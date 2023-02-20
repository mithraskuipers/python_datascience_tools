import pandas as pd

def concatListOfDataframes(dataframes):
	concatenated_df = pd.concat(dataframes)
	return concatenated_df
