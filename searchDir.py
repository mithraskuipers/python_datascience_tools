import os
import pandas as pd

def searchDir(start_path, subdir_name):
	paths = []
	for root, dirs, files in os.walk(start_path):
		for dir in dirs:
			if dir == subdir_name:
				paths.append(os.path.join(root, dir))
			path = os.path.join(root, dir)
			if os.path.isdir(path):
				paths += find_subdirectories(path, subdir_name)
	return paths

'''
This function works similarly to the previous function, but includes a check for
whether the current path is a directory (using os.path.isdir(path)) before
making a recursive call to find_subdirectories. This helps to prevent the
function from running indefinitely, as it ensures that a recursive call is only
made if the current path is a directory.

The paths list is updated with the path of each found subdirectory, and the
final list of paths is returned. Note that, in this case, the function returns
a list, not a DataFrame, but you can easily convert the list to a DataFrame if
desired, by doing return pd.DataFrame({"path": paths}).
'''