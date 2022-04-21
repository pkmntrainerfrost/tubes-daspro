from functions_lists import *
from functions_parser import *

def validate_and_fix(data,header):

    if data[0] != header: # Header tidak sesuai
        if data[0] != []: # File csv tidak memiliki header
            data = (header,konkat(data[0],data[1]))
        else: # File csv kosong total
            data = (header,[])
    
    return data

def load(nama_folder):

    try:
        data_user = parse(nama_folder + "/user.csv")
        data_game = parse(nama_folder + "/game.csv")
        data_riwayat = parse(nama_folder + "/riwayat.csv")
        data_kepemilikan = parse(nama_folder + "/kepemilikan.csv")

        header_user = separate("id;username;nama;password;role;saldo")
        header_game = separate("id;nama;kategori;tahun_rilis;harga;stok")
        header_riwayat = separate("game_id;nama;harga;user_id;tahun_beli")
        header_kepemilikan = separate("game_id;user_id")

        data_user = validate_and_fix(data_user,header_user)
        data_game = validate_and_fix(data_game,header_game)
        data_riwayat = validate_and_fix(data_riwayat,header_riwayat)
        data_kepemilikan = validate_and_fix(data_kepemilikan,header_kepemilikan)
    except FileNotFoundError:
        print("Folder tidak ditemukan")
        quit()
    else:
        print('Selamat datang di antarmuka "Binomo"')
        return (data_user,data_game,data_riwayat,data_kepemilikan)