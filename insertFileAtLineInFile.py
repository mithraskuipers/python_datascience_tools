def insertFileAtLineInFile(file1, file2, row):
    with open(file1) as f:
        code = f.readlines()

    with open(file2) as f:
        code_to_insert = f.readlines()

    code[row:row] = ['\n'] + code_to_insert

    return ''.join(code)
