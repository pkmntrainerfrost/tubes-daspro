from lists import *
from parser import *

def load(nama_folder):

    try:
        data_user = parse(nama_folder + "/user.csv")
        data_game = parse(nama_folder + "/game.csv")
        data_riwayat = parse(nama_folder + "/riwayat.csv")
        data_kepemilikan = parse(nama_folder + "/kepemilikan.csv")
    except FileNotFoundError:
        print("Folder tidak ditemukan")
        quit()
    else:
        print('Selamat datang di antarmuka "Binomo"')
        return (data_user,data_game,data_riwayat,data_kepemilikan)