# import functions module
from components.csv import csv_checker, space_checker, edit_files, parse
# from components.parser import parse (error indexing)
from components.binomo import length

def register(files):
# Register function
# Akses : Admin & User
# Untuk melakukan registrasi user baru

# KAMUS
# name, username, password, word : str { nama user, username, password, variabel pengecek }
# valid_username, existing_account : bool { variabel validasi }
# orde, id : int { varibel untuk konversi karakter yang diperbolehkan, id otomatis }
# data : array of array of str { data user csv }

#ALGORITMA
    # INPUT DATA
    name = input("Nama : ")
    username = input("Username : ")
    password = input("Password : ")

    # PENGECEKAN INPUT NAMA DAN PASSWORD
    if not(space_checker(name)) or not(space_checker(password)):
        return print("Nama atau Password tidak boleh kosong")
    
    # PENGECEKAN KENUNIKAN USERNAME
    valid_username = False
    for word in username:
        orde = ord(word)
        # mengecek setiap karakter pada username
        if ((65<=orde<=90) or (97<=orde<=122) or word == '_' or word == '-' or (48<=orde<=57)):
            valid_username = True
        else:
            valid_username = False
            break

    # HASIL PENGECEKAN USERNAME
    if valid_username:   
        data = parse(files)
        existing_account = False

        # MEMVALIDASI PEMAKAIAN USERNAME
        for i in range(length(data)):
            if username == data[i][2]:
                existing_account = True
                
        # HASIL VALIDASI USERNAME
        if existing_account:
            return print(f"Username {username} sudah terpakai, silahkan menggunakan username lain.")
        else:
            if csv_checker(files):
                # pemberian id pada user
                id = int(data[length(data)-1][0]) + 1
                # id baru akan diberikan saldo 0 dan role 'user'
                edit_files (str(id) , name , username, password, 'user' , str(0) , files)
            else:
                edit_files (str(1) , name , username, password, 'user', str(0) ,files)
            return print(f'Username {username} telah berhasil register ke dalam "Binomo".')

    else:
        return print("Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.")

# Run
register(r'components\user.csv')

