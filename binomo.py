# Tugas Besar IF 1210 Dasar Pemrograman

# Kelompok 06 / Kelas 07
# NIM - Nama Anggota Kelompok:
# 16521213 - Salman Ma'arif Achsien

# Program BNMO
# 

# KAMUS

# NAMA MODUL / LIBRARY

import argparse
import datetime
import math
import os
import sys
import time

from functions_io import *
from functions_lists import *
from functions_parser import *

from F02 import *
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F08 import *
from F09 import *
from F10 import *
from F11 import *
from F12 import *
from F13 import *
from F14 import *
from F15 import *
from F16 import *
from F17 import *

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder",type=str)
args = parser.parse_args()
nama_folder = args.nama_folder

(data_user,data_game,data_riwayat,data_kepemilikan) = load(nama_folder)

user_id = 0
role = 0
status = 2

while __name__ == "__main__":

    commands = define_commands()

    command = user_input(commands,role,status)

    if command != False:
        
        if command == "register":
            data_user = register(data_user)
        if command == "login":
            (user_id,role,status) = login(data_user)
        if command == "tambah_game":
            data_game = tambah_game(data_game)
        if command == "ubah_game":
            data_game = ubah_game(data_game)
        if command == "ubah_stok":
            data_game = ubah_stok(data_game)
        if command == "list_game_toko":
            list_game_toko(data_game)
        if command == "buy_game":
            (data_user,data_game,data_riwayat,data_kepemilikan) = buy_game(user_id,data_game,data_user,data_riwayat,data_kepemilikan)
        if command == "list_game":
            list_game(user_id,data_game,data_kepemilikan)
        if command == "search_my_game":
            search_my_game(user_id,data_game,data_kepemilikan)
        if command == "search_game_at_store":
            search_game_at_store(data_game)
        if command == "topup":
            data_user = topup(data_user)
        if command == "riwayat":
            riwayat(user_id,data_riwayat)
        if command == "help":
            bantuan(commands,role,status)
        if command == "save":
            save(data_user,data_game,data_riwayat,data_kepemilikan)
        if command == "exit":
            terminate(data_user,data_game,data_riwayat,data_kepemilikan)