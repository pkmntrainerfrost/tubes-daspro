from functions_lists import *

def define_commands():

    commands = []

    # Setiap perintah disimpan sebagai sebuah tuple di dalam list of tuple
    # Isi tuple adalah sebagai berikut - (nama,deskripsi,izin,status)
    # Untuk izin, 0 berarti semua user, 1 berarti user, 2 berarti admin
    # Untuk status, 0 berarti bisa dilakukan kapan saja, 1 berarti harus login, 2 berarti sebelum login

    commands += [("register","Untuk melakukan registrasi user baru",2,1)]
    commands += [("login","Untuk melakukan login ke dalam sistem",0,2)]
    commands += [("tambah_game","Untuk menambah game yang dijual pada toko",2,1)]
    commands += [("ubah_game","Mengubah informasi game pada toko game",2,1)]
    commands += [("ubah_stok","Mengubah stok suatu game pada toko",2,1)]
    commands += [("list_game_toko","Untuk melihat list game yang dijual pada toko",0,1)]
    commands += [("buy_game","prosedur bagi user untuk membeli game",1,1)]
    commands += [("list_game","memberikan daftar game yang dimiliki pengguna",1,1)]
    commands += [("search_my_game","mencari game yang dimiliki dari ID dan tahun rilis",1,1)]
    commands += [("search_game_at_store","Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis",0,1)]
    commands += [("topup","prosedur untuk menambahkan saldo kepada User",2,1)]
    commands += [("riwayat","melihat riwayat pembelian user",1,1)]
    commands += [("help","tampilkan semua command",0,0)]
    commands += [("save","simpan data",0,1)]
    commands += [("exit","keluar",0,0)]

    return commands

def user_input(commands,role,status):

    user_input = str(input(">>> "))
    user_input = user_input.lower()

    for i in commands:
        if is_member(i,user_input):
            if status != i[3] and i[3] != 0:
                if i[3] == 1:
                    print("Anda harus login terlebih dahulu.")
                if i[3] == 2:
                    print("Anda sudah login.")
                return False
            if role != i[2] and i[2] != 0:
                if i[2] == 1:
                    print("")
                if i[2] == 2:
                    print("")
                return False
            return user_input
    
    print("Fungsi tidak ditemukan.")
    return False

def print_table(table):

    if table != []:
        col_length = [0 for i in range(length(table[0]))]

    for row in table:
        for col in range(length(col_length)):
            if length(row[col]) > col_length[col]:
                col_length[col] = length(row[col])
    
    for row in range(length(table)):
        print(str(row+1) + ". ",end="")
        for col in range(length(col_length)):
            print(table[row][col] + " "*(col_length[col] - length(table[row][col])),end="")
            if col < length(col_length) - 1:
                print(" | ",end="")
        print()
                
    