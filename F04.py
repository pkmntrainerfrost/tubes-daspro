# import functions module
from components.csv import csv_checker, parse, edit_files
from components.binomo import length, is_integer

def tambah_game(files, kepemilikan_files): # files = game.csv , kepemilikan_files = memberikan nilai game id default
# Tambah Game Function
# Akses : Admin
# I.S. Menerima input informasi game baru yang akan ditambahkan
# F.S. Melakukan penambahan game pada BNMO (game.csv)
# KAMUS
# not_valid : Bool { variabel kondisi untuk break while }
# nama_game, kategori : string { data game }
# tahun_rilis, stok_awal : integer { data game }
# harga : real { data game }
# id : integer { id data }
# data : arr of arr of str { data game.csv }

#ALGORITMA
    # PARSE CSV
    data = parse(files)
    # VALIDASI INPUT
    not_valid = True
    while(not_valid):
        nama_game = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok_awal = input("Masukkan stok awal: ")
        if (nama_game =="" or kategori =="" or tahun_rilis =="" or harga =="" or stok_awal ==""):
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        else:
            # Untuk harga, bisa input integer maupun input real
            if (is_integer(tahun_rilis) and (is_integer(harga)) and is_integer(stok_awal)):
                not_valid = False
            else:
                print("Mohon mengecek input untuk tahun rilis, harga, atau stok awal.")
    # PROGRAM SETELAH INPUT BENAR
    if (not_valid == False):
        if csv_checker(files):
            # pemberian id pada game
            id = length(data) + 1
            # id akan diincrement berdasarkan urutan game yang ada
            # MEMORY DATA UNTUK DISAVE
            memory_data = ['GAME'+str(id), nama_game, kategori, tahun_rilis, harga, stok_awal]
            
            # JIKA SAVE
            # edit_files ('GAME' + str(id) , nama_game , kategori, tahun_rilis, harga , stok_awal , files)
            # f = open(kepemilikan_files, 'a')
            # f.write('GAME' + str(id) + ';' + '\n')
            # f.close()
        else:
            # jika belum ada game , game yang ditambah pertama kali akan diberi id = 1
            # MEMORY DATA UNTUK DISAVE
            memory_data = ['GAME'+str(1), nama_game, kategori, tahun_rilis, harga, stok_awal]

            # JIKA SAVE
            # edit_files ('GAME'+ str(1) , nama_game , kategori, tahun_rilis, harga, stok_awal ,files)
            # f = open(kepemilikan_files, 'a')
            # f.write('GAME' + str(1) + ';' + '\n')
            # f.close()
        print("Selamat! Berhasil menambahkan game", nama_game)
        # MENGEMBALIKAN MEMORY DATA
        return memory_data

# Run        
tambah_game('components\game.csv', 'components\kepemilikan.csv')
            