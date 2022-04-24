# import functions modules

from functions_lists import *
from functions_strings import *
from functions_validation import *

def ubah_game(data_game): # files = game.csv
    # Ubah Game Function
    # Mengubah informasi game pada toko game
    # Prekondisi : stock tidak bisa diubah
    # KAMUS
    # id, nama_game, kategori : string { input informasi data baru }
    # found : Bool { variabel validasi }
    # tahun_rilis : integer { data baru untuk tahun rilis }
    # harga : real { data baru untuk harga }
    # data : arr of arr of str { data game.csv }
#ALGORITMA
    # MENGVALIDASI KONDISI CSV

    valid = False

    id = ""

    while not valid:
        id = str(input("Masukkan ID game: "))
        if is_empty_string(id):
            print("Field ID tidak boleh kosong!")
        else:
            valid = True

    game = []
    idx = 0

    for row in data_game[1]:
        if row[get_index(data_game[0],"id")] == id:
            game = row
            break
        idx += 1

    if game != []:

        valid = False
        
        while not valid:
            nama = ("nama",str(input("Masukkan nama game: ")))
            kategori = ("kategori",str(input("Masukkan kategori: ")))
            tahun_rilis = ("tahun_rilis",remove_delimiter(str(input("Masukkan tahun rilis: "))))
            harga = ("harga",remove_delimiter(str(input("Masukkan harga: "))))

            if (is_empty_string(tahun_rilis[1]) or is_integer(tahun_rilis[1])) and (is_empty_string(harga[1]) or is_integer(harga[1])):
                params = [nama,kategori,tahun_rilis,harga]
                for i in params:
                    if not is_empty_string(i[1]):
                        game[get_index(data_game[0],i[0])] = i[1]
                valid = True
            else:
                print("Mohon mengecek input untuk tahun rilis, harga, atau stok awal.")
        
        print("Game dengan ID: ",id," berhasil diubah.")
        return (data_game[0],konkat(segment(data_game[1],0,idx),[game],segment(data_game[1],idx+1)))
    
    else:

        print("ID Game tersebut tidak ditemukan.")
        
    return data_game