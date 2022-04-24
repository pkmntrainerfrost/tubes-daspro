from functions_lists import *
from functions_parser import *
import os

def save(data_user,data_game,data_riwayat,data_kepemilikan):
    
    nama_folder = str(input("Masukkan nama folder penyimpanan: "))
    folder_ada = False

    for (root,dirs,files) in os.walk("."):
        for dir in dirs:
            if dir == nama_folder:
                folder_ada = True

    if not folder_ada:
        os.mkdir(nama_folder)

    csv = ["user.csv","game.csv","riwayat.csv","kepemilikan.csv"]
    create_csv = [True,True,True,True]
    data = [data_user,data_game,data_riwayat,data_kepemilikan]

    for (root,dirs,files) in os.walk(nama_folder):
        for i in range(length(csv)):
            if is_member(files,csv[i]):
                create_csv[i] = False

    for i in range(length(csv)):
        write(nama_folder + "/" + csv[i],data[i],create_csv[i])

    print("Data telah disimpan pada folder" + nama_folder + "!")