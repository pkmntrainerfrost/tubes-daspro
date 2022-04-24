from functions_lists import *
from functions_io import print_table

def riwayat(user_id,data_riwayat):
    
    riwayat = strain(data_riwayat[1],str(user_id),False,True,get_index(data_riwayat[0],"user_id"))

    if riwayat == []:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else:
        if type(riwayat[0]) != list:
            riwayat = [riwayat]

        riwayat_show = []
        for pembelian in riwayat:
            riwayat_show += [segment(pembelian,0,3) + [pembelian[4]]]

        print()
        print("Daftar game:")
        print_table(riwayat_show)