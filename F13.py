from functions_lists import *
from functions_io import print_table

def riwayat(user,data_riwayat):
    
    riwayat = strain(data_riwayat[1],user,False,True,index(data_riwayat[0],"user_id"))

    if riwayat == []:
        print("gk punya game lu miskin")
    else:
        print_table(riwayat)
