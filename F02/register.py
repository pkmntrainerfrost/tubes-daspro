# import functions module
from components.functions_register import edit_files
from components.functions_register import parse
from components.old import length

# csv path files
files = r'components\acc_data.csv'

# Register function
def register():
    # INPUT DATA
    name = input("Nama : ")
    username = input("Username : ")
    password = input("Password : ")

    # PENGECEKAN KENUNIKAN USERNAME
    valid_username = False
    for word in username:
        orde = ord(word)
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
            if username == data[i][1]:
                existing_account = True
                
        # HASIL VALIDASI USERNAME
        if existing_account:
            print(f"Username {username} sudah terpakai, silahkan menggunakan username lain.")
        else:
            print(f'Username {username} telah berhasil register ke dalam "Binomo".')
            edit_files (name , username, password, files)

    else:
        print("Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.")

# Run
register()
