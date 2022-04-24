# import function module
from functions_strings import *
from functions_lists import *
from functions_validation import *

# After login process

def topup(data_user):

    username = str(input("Masukkan username: "))
    nominal = remove_delimiter(str(input("Masukkan saldo: ")))

    user = []
    index = 0

    for row in data_user[1]:
            if row[get_index(data_user[0],"username")] == username:
                user = row
                break
            index += 1

    if is_empty_string(username) or is_empty_string(nominal):
        print("Masukan tidak valid.")
        return data_user
    
    if not is_integer(nominal):
        print("Masukan tidak valid.")
        return data_user
    
    if int(user[get_index(data_user[0],"saldo")]) + int(nominal) < 0:
        print("Masukan tidak valid.")
        return data_user

    if user == []:
        print('Username "' + username + '" tidak ditemukan.')
        return data_user

    user[get_index(data_user[0],"saldo")] = str(int(user[get_index(data_user[0],"saldo")]) + int(nominal))
    
    print("Top up berhasil. Saldo",user[get_index(data_user[0],"nama")],"berubah menjadi",user[get_index(data_user[0],"saldo")]+".")

    return (data_user[0],konkat(segment(data_user[1],0,index),[user],segment(data_user[1],index+1)))