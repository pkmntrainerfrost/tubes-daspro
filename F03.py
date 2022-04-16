# import functions module
from components.csv import *
from components.binomo import length

# KAMUS
# admin_username, admin_password : string { data admin }
# admin : array of string { data function yang bisa dirun dalam state admin }
# user : array of string { data function yang bisa dirun dalam state user }
# not_admin_msg, not_user_msg, error_before_login, error, greeting : string
# data : array of array of string { csv file }
# username, password : string { input }
# success, logged_in, admin_status : Boolean { hasil login }
# select : string { input }
# user_id : int { user unique id }

# ALGORITMA
# user data csv path
files = r'components\user.csv'

# ADMINISTRATOR FUNCTION
admin = ["function that only admin can run."]
# USER FUNCTION
user = ["function that only user can run."]
# ERROR MESSAGE FOR ACCESSING WRONG FUNCTION
not_admin_msg = "Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut."
not_user_msg = "Maaf, anda harus menjadi user untuk melakukan hal tersebut."
error_before_login = "Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”"

# LOGIN FUNCTION
def login(files):
    # DATA CSV
    data = parse(files)
    error = "Password atau username salah atau tidak ditemukan."
    # ADMIN ACCESS KEY
    user_id = 0
    admin_username = "localhost"
    admin_id = 8888
    admin_password = "port8888"
    # INPUT LOGIN
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    # PENANDA VALIDASI LOGIN DAN STATUS ADMIN
    global success, logged_in, admin_status
    success = False
    logged_in = False
    admin_status = False
    # VERIFY IF ITS ADMIN
    if username == admin_username and password == admin_password:
        admin_status = True
        success = True
        logged_in = True
        # Menyimpan user id
        user_id = admin_id
        print("---ADMINISTRATOR---")
    # VERIFY IF ITS USER
    else:
        for i in range(length(data)):
            if data[i][2] == username and data[i][3] == password:
                # Menyimpan user id
                user_id = data[i][0]
                greeting = f"Halo {data[i][1]}! Selamat datang di “Binomo”"
                success = True
                logged_in = True
                break
        if success == False:
            print(error)
        else:
            print(greeting)
    return user_id

# PROGRAM SETELAH LOGIN
def after_login():
    # INPUT FIELD
    select = input(">>>")
    # MENCARI VALIDASI INPUT TERHADAP STATE USER
    for i in range(length(admin)):
        if select == admin[i] and admin_status == False:
            print(not_admin_msg)
            break
        elif select == user[i] and admin_status == True:
            print(not_user_msg)
        else:
            # FUNCTION HERE
            print("Proceed>>>")

# PROGRAM UTAMA
def main(files):
    # FUNCTION INPUTS HERE
    select = input(">>>")
    # VALIDASI KEBENARAN LOGIN
    if select == "login":
        login(files)
        if success == True:
            after_login()
    else:
        print(error_before_login)
        
# Run
main(files)



