# import function module
from .csv import *
from functions_lists import length

# After login process
def topup(data_user):
    # Topup function
    # Prosedur untuk menambahkan saldo kepada User
    # Akses : admin
    # I.S. Menerima username dan jumlah nominal top up
    # F.S. Menambah saldo sesuai dengan username atau tidak jika username atau nominal tidak valid
    # KAMUS
    # username, name : string { input username, nama }
    # nominal_topup, saldo : integer { input nominal , variabel saldo sementara }
    # found : Bool
    # saldo_updated : integer { saldo setelah top up }
    # idx_username : integer { index user_id yang memenuhi }
#ALGORITMA
    # LOAD DATA
    data = data_user[1]
    # INPUT
    username = input("Masukkan username: ")
    nominal_topup = int(input("Masukkan saldo: "))

    # VALIDASI INPUT USERNAME DAN NOMINAL TOP UP
    if (not(space_checker(username)) or not(space_checker(str(nominal_topup)))):
        return print("Username atau Saldo tidak boleh kosong.")
    else:
        # VALIDASI USERNAME DAN PASSWORD
        found = False
        for i in range(length(data)):
            if data[i][2] == username:
                idx_username = i
                found = True
        if found == False:
            print(f"Username \"{username}\" tidak ditemukan.")
        else:
            # JIKA USERNAME VALID, PERIKSA INPUT NOMINAL
            if int(data[idx_username][5]) + nominal_topup < 0:
                print("Masukkan tidak valid.")
            else:
                # JIKA INPUT NOMINAL VALID
                for j in range(length(data)):
                    # MENCARI USERNAME YANG INGIN DITOP UP & UPDATE DATA
                    if data[j][2] == username:
                        saldo = int(data[j][5])
                        saldo += nominal_topup
                        data[j][5] = str(saldo)
                        saldo_updated = data[j][5]
                        name = data[j][1]
                print(f"Top up berhasil. Saldo {name} bertambah menjadi {saldo_updated}.")
                return data