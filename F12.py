# import function module
from components.csv import parse, edit_files, clear_csv
from components.binomo import length

# After login process
def topup (files):
    # Topup function
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
    data = parse(files)
    # INPUT
    username = input("Masukkan username: ")
    nominal_topup = int(input("Masukkan saldo: "))
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
        if int(data[idx_username][5]) - nominal_topup < 0:
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
            # MENGOSONGI CSV
            clear_csv(files)
            # MENGISI ULANG CSV DENGAN FILE YANG SUDAH DIUPDATE
            for i in range(length(data)):
                edit_files(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], files)
            print(f"Top up berhasil. Saldo {name} bertambah menjadi {saldo_updated}.")
                
# Run
topup('components\\user.csv')