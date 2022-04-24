from F16 import *

def terminate(data_user,data_game,data_riwayat,data_kepemilikan):

    valid = False

    while not valid:

        save_yn = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))

        save_yn = save_yn.lower()

        if save_yn == "y":
            save(data_user,data_game,data_riwayat,data_kepemilikan)
            valid = True
        if save_yn == "n":
            valid = True

    exit()
        
    