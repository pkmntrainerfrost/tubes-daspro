# import functions module
from .csv import space_checker, parse
from functions_strings import *
# from components.parser import parse (error indexing)
from functions_lists import *

def register(data_user):
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
    name = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # PENGECEKAN INPUT NAMA DAN PASSWORD
    if is_empty_string(name) or is_empty_string(username) or is_empty_string(password):
        print("Field tidak diperbolehkan kosong!")
        return data_user
    
    # PENGECEKAN KENUNIKAN USERNAME
    valid_username = True
    for char in username:
        orde = ord(char)
        # mengecek setiap karakter pada username
        if not (((65<=orde<=90) or (97<=orde<=122) or char == '_' or char == '-' or (48<=orde<=57))):
            valid_username = False
            break

    # HASIL PENGECEKAN USERNAME
    if valid_username:   
        existing_account = False

        # MEMVALIDASI PEMAKAIAN USERNAME
        for user in data_user[1]:
            if user[index(data_user[0],"username")] == username:
                existing_account = True
                break
                
        # HASIL VALIDASI USERNAME
        if existing_account: 
            print(f"Username {username} sudah terpakai, silahkan menggunakan username lain.")
            return data_user
        else:
            print(f'Username {username} telah berhasil register ke dalam "Binomo".')
            if length(data) > 0:
                # pemberian id pada user
                id = int(data[length(data)-1][0]) + 1
                # id baru akan diberikan saldo 0 dan role 'user'
                memory_data = data + [[str(id) , name , username, password, 'user' , str(0)]]
                return memory_data
            else:
                data = [[str(1) , name , username, password, 'user', str(0)]]
                return data
    else: 
        print("Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.")
        return 