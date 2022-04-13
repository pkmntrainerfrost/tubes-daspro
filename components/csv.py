from .binomo import *
# MENGECEK KONDISI CSV
# I.S. Menerima file CSV
# F.S. Menghasilkan True jika CSV tidak kosong dan sebaliknya
# KAMUS
# len : int { pengidentifikasi }
# i, j :  int { variabel increment }
# raw_data : file { file csv }
def csv_checker(file):
    raw_data = open(file, 'r')
    len = 0
    for i in raw_data:
        for j in i:
            len += 1
    if len > 0:
        return True
    else: 
        return False
    
# MENDELETE SEMUA ISI CSV
def clear_csv(files):
    f = open(files, 'w')
    f.write('')
    f.close()

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
                if rows < 1:
                    cols += 1
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
                data[row][col] = str
                str = ''
                col += 1
            elif (j == "\n"):
                data[row][col] = str
                str = ''
                row += 1
                col = 0 
            else:
                str += j
    raw_data.close()
    # KEMBALIKAN LIST OF LIST OF STR data
    return data

# MENGEDIT FILE CSV
# I.S. Menerima input id, name , username, password, role, saldo , files
# F.S. Menambah informasi id, name , username, password, role, saldo pada file csv tujuan
# KAMUS
# editable_files : file { file csv }
def edit_files(id, param_1, param_2, param_3, param_4, param_5 , files):  
    editable_files = open(files, 'a')
    editable_files.write(id + ';' + param_1 + ';' + param_2 + ';' + param_3 + ';' + param_4 + ';' + param_5 + '\n')
    editable_files.close()

def edit_files_2(table ,files):
    editable_files = open(files, 'a')
    for i in range (length(table)):
        j = 0
        not_end = True
        while(not_end):
            if table[i][j] != last(table[i]):
                editable_files.write(table[i][j] + ';')
            else:
                editable_files.write(table[i][j] + '\n')
                not_end = False
                j = -1
            j += 1
    editable_files.close()


# PARSER 2 (input str -> Array)
def parse2(array):
    # MENGHITUNG JUMLAH ELEMEN dalam ARRAY
    cols = 0
    for i in array:
        if i == ',':
            cols += 1

    # INISIALISASI ARRAY of STR data
    data = ['' for i in range(cols)]

    # SIMPAN DATA DI ARRAY of STR data
    col = 0
    str = ''
    for i in array:
        if (i == ','):
            data[col] = str
            str = ''
            col += 1
        else:
            str += i
    data = data + [str]
    # KEMBALIKAN ARRAY of STR data
    return data

# WRITE DATA UNTUK KEPEMILIKAN CSV
def edit_files_2(table ,files):
    editable_files = open(files, 'a')
    for i in range (length(table)):
        for j in range(2):
            if j == 0:
                editable_files.write(table[i][j] + ';')
            else:
                for k in range(length(table[i][j])):
                    if k < length(table[i][j])-1:
                        if table[i][j][k] != '':
                            editable_files.write(str(table[i][j][k]) + ',')
                    else:
                        editable_files.write(str(table[i][j][k]) + '\n')
    editable_files.close()