from functions_lists import *
from functions_parser import *
import os

def save(data_user,data_game,data_riwayat_data_kepemilikan):
    
    nama_folder = str(input("Masukkan nama folder penyimpanan: "))

    for (root,dirs,files) in os.walk