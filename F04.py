# import functions module
from .csv import *
from binomo_old import *
from functions_lists import *

def tambah_game(data_game): # files = game.csv
# Tambah Game Function
# Akses : Admin
# Untuk menambah game yang dijual pada toko

# KAMUS
# not_valid : Bool { variabel kondisi untuk break while }
# nama_game, kategori : string { data game }
# tahun_rilis, stok_awal : integer { data game }
# harga : real { data game }
# id : integer { id data }
# data : arr of arr of str { data game.csv }
# memory_data : arr of arr of str { data temporary setelah perubahan }

#ALGORITMA
    # Data dari CSV
    data = data_game[1]
    # VALIDASI INPUT
    not_valid = True
    while(not_valid):
        nama_game = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok_awal = input("Masukkan stok awal: ")

        # MEMVALIDASI INPUT
        if (not(space_checker(nama_game)) or not(space_checker(kategori)) or not(space_checker(tahun_rilis)) or not(space_checker(harga)) or not(space_checker(stok_awal))):
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        else:
            # MEMVALIDASI TAHUN RILIS DAN HARGA
            if (is_integer(tahun_rilis) and (is_integer(harga)) and is_integer(stok_awal)):
                not_valid = False
            else:
                print("Mohon mengecek input untuk tahun rilis, harga, atau stok awal.")

    # PROGRAM SETELAH INPUT BENAR
    if (not_valid == False):
        if length(data) > 0:
            # pemberian id pada game
            id = length(data) + 1
            # id akan diincrement berdasarkan urutan game yang ada
            # MEMORY DATA UNTUK DISAVE
            memory_data = data + [['GAME'+str(id), nama_game, kategori, tahun_rilis, harga, stok_awal]]
            
        else:
            # jika belum ada game , game yang ditambah pertama kali akan diberi id = 1
            # MEMORY DATA UNTUK DISAVE
            memory_data = [['GAME'+str(1), nama_game, kategori, tahun_rilis, harga, stok_awal]]
            
        print("Selamat! Berhasil menambahkan game", nama_game)
        # MENGEMBALIKAN MEMORY DATA
        return memory_data