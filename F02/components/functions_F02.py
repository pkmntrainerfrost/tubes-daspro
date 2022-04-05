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
# I.S. Menerima input id, name , username, password, role, saldo , files
# F.S. Menambah informasi id, name , username, password, role, saldo pada file csv tujuan
# KAMUS
# user_id : int { mengidentifikasi ID User }
# editable_files : file { file csv }
def edit_files(id, name, username, password, role, saldo , files):
    user_id = id   
    editable_files = open(files, 'a')
    editable_files.write(str(user_id)  + ';' + name + ';' + username + ';' + password + ';' + role + ';' + str(saldo) + '\n')
    editable_files.close()
