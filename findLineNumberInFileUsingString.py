def findLineNumberInFileUsingString(file_name, search_string):
    with open(file_name) as f:
        for i, line in enumerate(f, 1):
            if search_string in line:
                return (i)
    return (-1)
