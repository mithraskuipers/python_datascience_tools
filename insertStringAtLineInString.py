def insertStringAtLineInString(string1, string2, row):
    code = string1.split('\n')
    code_to_insert = string2.split('\n')

    code[row:row] = [''] + code_to_insert

    return '\n'.join(code)