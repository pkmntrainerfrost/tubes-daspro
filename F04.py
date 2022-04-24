# import functions module
from functions_strings import *
from functions_lists import *
from functions_validation import *

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
    # VALIDASI INPUT
    valid = False
    while not valid:
        nama_game = str(input("Masukkan nama game: "))
        kategori = str(input("Masukkan kategori: "))
        tahun_rilis = remove_delimiter(str(input("Masukkan tahun rilis: ")))
        harga = remove_delimiter(str(input("Masukkan harga: ")))
        stok_awal = remove_delimiter(str(input("Masukkan stok awal: ")))

        # MEMVALIDASI INPUT
        if is_empty_string(nama_game) or is_empty_string(kategori) or is_empty_string(tahun_rilis) or is_empty_string(harga) or is_empty_string(tahun_rilis):
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        else:
            # MEMVALIDASI TAHUN RILIS DAN HARGA
            if is_integer(tahun_rilis) and is_integer(harga) and is_integer(stok_awal):
                valid = True
            else:
                print("Mohon mengecek input untuk tahun rilis atau harga.")

    # PROGRAM SETELAH INPUT BENAR
    if data_game[1] != []:
        id = last(data_game[1])[get_index(data_game[0],"id")]
        id = str(int(segment(id,4)) + 1)
        id = "GAME" + "0"*(3-length(id)) + id
    else:
        id = "GAME001"

    print("Selamat! Berhasil menambahkan game", nama_game)

    return (data_game[0],konsdot(data_game[1],[id,nama_game,kategori,tahun_rilis,harga,stok_awal]))