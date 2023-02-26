def findLineNumberInStringsUsingString(string, search_string):
    for i, line in enumerate(string.split('\n'), 1):
        if search_string in line:
            return i
    return (-1)
