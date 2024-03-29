from functions_lists import *
from functions_io import print_table

def search_game_at_store(data_game):

    id = ("id",str(input("Masukkan ID Game: ")))
    nama = ("nama",str(input("Masukkan Nama Game: ")))
    harga = ("harga",str(input("Masukkan Harga Game: ")))
    kategori = ("kategori",str(input("Masukkan Kategori Game: ")))
    tahun_rilis = ("tahun_rilis",str(input("Masukkan Tahun Rilis Game: ")))

    params = [id,nama,harga,kategori,tahun_rilis]
    element = []
    col = []

    for i in params:
        if i[1] != "":
            element += [i[1]]
            col += [get_index(data_game[0],i[0])]
    
    if element != []:
        match = strain(data_game[1],element,False,True,col)
        
    else:
        match = data_game[1]

    if match == []:
        print("Tidak ada game yang memenuhi kriteria.")
    else:
        if type(match[1]) != list:
            match = [match]
        print()
        print("Daftar game pada toko yang memenuhi kriteria:")   
        print_table(match)

    


