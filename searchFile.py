import os
import pandas as pd

def searchFile(start_path, file_name):
	paths = []
	for root, dirs, files in os.walk(start_path):
		if file_name in files:
			paths.append(os.path.join(root, file_name))
	return pd.DataFrame({"path": paths})

'''
This function uses the os.walk function to traverse the directory tree rooted at
start_path. For each directory in the tree, os.walk returns a tuple (root, dirs,
files), where root is the current directory, dirs is a list of subdirectories of
root, and files is a list of files in root.

In the function, we check whether the file name that we're looking for,
file_name, is in the list of files files. If it is, we append the full path to
the file to the paths list. Finally, the list of paths is returned in the form
of a Pandas DataFrame, with a single column named "path".
'''