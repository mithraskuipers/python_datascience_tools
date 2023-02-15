import pandas as pd

def moveColumn(df, column_name, position):
    """
    Move the specified column to the specified position in the dataframe.

    Args:
    dataframe: a pandas dataframe object
    column_name: the name of the column to be moved
    position: the new index position of the column

    Returns:
    A new dataframe with the specified column moved to the new position.
    """
    # Create a list of all column names in the dataframe
    column_list = list(df.columns)

    # Remove the specified column from the list
    column_list.remove(column_name)

    # Insert the specified column at the new position
    column_list.insert(position, column_name)

    # Return the new dataframe with the columns in the new order
    return (df[column_list])
