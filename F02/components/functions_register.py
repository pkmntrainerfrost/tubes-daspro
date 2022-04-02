# MENGECEK KONDISI CSV
def csv_checker(file):
    raw_data = open(file, 'r')
    len = 0
    for i in raw_data:
        for j in i:
            len += 1
    return len
    
# MENKONVERSI CSV ke LIST OF LIST OF STR data
def parse(file):
    raw_data = open(file, 'r')
    # MENGHITUNG JUMLAH BARIS DAN KOLOM
    cols = 0
    rows = 0
    for i in raw_data:
        for j in i:
            if j == ";":
                if rows < 1:
                    cols += 1
            elif j == "\n":
                rows += 1
    raw_data.close()
    
    # INISIALISASI LIST OF LIST OF STR data 
    data = [['' for j in range(cols)] for i in range(rows)]
    raw_data = open(file, 'r')

    # SIMPAN DATA DI LIST OF LIST OF STR data
    col = 0
    row = 0
    str = ''
    for i in raw_data:
        for j in i:
            if (j == ';'):
                # print(str)
                data[row][col] = str
                str = ''
                col += 1
            elif (j == "\n"):
                str = ''
                row += 1
                col = 0 
            else:
                str += j
    raw_data.close()
    # KEMBALIKAN LIST OF LIST OF STR data
    return data

# MENGEDIT FILE CSV
def edit_files(name, username, password, files):    
    editable_files = open(files, 'a')
    editable_files.write(name + ';' + username + ';' + password + ';' + '\n')
    editable_files.close()
