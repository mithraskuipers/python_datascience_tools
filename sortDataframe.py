import pandas as pd

def sortDataframe(df, sort_type="alphabetical", sort_dir="ascending"):
    if sort_type == "numerical":
        if sort_dir == "ascending":
	        df = df.sort_index(axis=1, ascending=True, key=lambda x: pd.to_numeric(x, errors='coerce'))
        elif sort_dir == "descending":
            df = df.sort_index(axis=1, ascending=False, key=lambda x: pd.to_numeric(x, errors='coerce'))
        else:
	        print("Invalid sort order specified.")
    elif sort_type == "alphabetical":
        if sort_dir == "ascending":
            df = df.reindex(sorted(df.columns), axis=1)
        elif sort_dir == "descending":
            df = df.reindex(sorted(df.columns, reverse=True), axis=1)
        else:
            print("Invalid sort order specified.")
    else:
        print("Invalid sort order specified.")
    return (df)
