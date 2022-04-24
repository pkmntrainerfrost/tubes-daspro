from functions_lists import *

def parse(file):

    # KAMUS LOKAL
    # file          : str                   - nama + path file yang hendak di-parse
    # f             : file                  - file yang di-parse
    # raw_data      : str                   - data mentah file
    # data          : list of lists of str  - data hasil parsing

    # ALGORITMA

    # BUKA FILE, SIMPAN DI STRING raw_data
    f = open(file,"r")
    raw_data = f.read()
    f.close()

    data = separate(raw_data)

    if data == []:
        data = ([],[])
    elif type(data[0]) != list:
        data = (data,[])
    else:
        data = (head(data),tail(data))

    # KEMBALIKAN LIST OF LIST OF STR data
    return data

def write(file,data,create=False):

    if create:
        f = open(file,"x")
    else:
        f = open(file,"w")

    contents = ""

    rows = length(data[1])
    cols = length(data[0])

    for header in range(cols):
        contents += data[0][header]
        if header != cols - 1:
            contents += ";"
    if rows != 0:
        contents += "\n"

    for row in range(rows):
        for col in range(cols):
            contents += data[1][row][col]
            if col != cols - 1:
                contents += ";"
        if row != rows - 1:
            contents += "\n"

    f.write(contents)

    f.close()