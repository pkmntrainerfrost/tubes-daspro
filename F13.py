from functions_lists import *
from functions_io import print_table

def riwayat(user_id,data_riwayat):
    
    riwayat = strain(data_riwayat[1],str(user_id),False,True,get_index(data_riwayat[0],"user_id"))

    if riwayat == []:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else:
        if type(riwayat[1]) != list:
            riwayat = [riwayat]
        print_table(riwayat)
