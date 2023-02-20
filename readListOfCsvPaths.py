'''
Expects a list of csv file paths.
It will read each of them and return the read dataframes into a list.
'''

import pandas as pd

def readListOfCsvPaths(file_paths):
	dataframes = []
	for file_path in file_paths:
		df = pd.read_csv(file_path)
		dataframes.append(df)
	return dataframes