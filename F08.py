# import functions module
from components.binomo import *
from components.csv import *
from datetime import datetime
# from .F03 import login

game = r'components\game.csv'
user = r'components\user.csv'
path_kepemilikan = r'components\kepemilikan.csv'
path_riwayat = r'components\riwayat.csv'
# id = login(user)

# After login process
# FUNCTION BUY GAME
def buy_game(game_files, user_files, kepemilikan_user_files, riwayat_files, id):
    # Prosedur bagi user untuk membeli game
    # Akses : user
    # KAMUS
    # kepemilikan, data_game, data_username : files { csv }
    # arr_id : array of array { tabel data untuk id dari data kepemilikan }
    # index3, index : integer { index untuk file user, index untuk file game }
    # game_id : string { input user }
    # found, found_game, loop : Boolean { variabel validasi }
    # id : string { id user }
    # stok, saldo : integer { stok game tersisa, saldo user }
    # memory_data_riwayat, memory_data_game, memory_data_user, memory_kepemilikan : array of string { memori }
    
    # ALGORITMA
    # INISIALISASI DATA DARI CSV
    kepemilikan = parse(kepemilikan_user_files) # data kepemilikan
    data_game = parse(game_files) # data game (stok)
    data_username = parse(user_files) # data user (username)
    data_riwayat = parse(riwayat_files) # data riwayat (riwayat user)

    # INISIALISASI DATA KEPEMILIKAN
    for i in range(length(kepemilikan)):
        arr_id = parse2(kepemilikan[i][1])
        kepemilikan[i][1] = arr_id

    # MENCARI USER ID
    index3 = 0
    for i in range(length(data_username)):
        if data_username[i][0] == id:
            index3 = i # mencari index dari account

    # INPUT
    game_id = input("Masukkan ID Game: ")

    # Variabel untuk validasi
    found = False
    found_game = False
    loop = True

    # PROSES MENCARI GAME ID
    for i in range(length(data_game)):
        # JIKA GAME ID DITEMUKAN
        if data_game[i][0] == game_id:
            index = i # mencari index dari game yang dicari
            loop = False
            found_game = False
            found = False

            # MEMVALIDASI KONDISI SALDO DAN STOK
            if (int(data_game[i][4]) <=  int(data_username[index3][5])) and int(data_game[i][5]) > 0:
                # MEMVALIDASI KEPEMILIKAN GAME
                if length(kepemilikan) != 0:
                    for j in range(length(kepemilikan)):
                        if kepemilikan[j][0] == game_id:
                            found_game = True
                            for k in range(length(kepemilikan[j][1])):
                                if id == kepemilikan[j][1][k]:
                                    found = True
                                    print("Anda sudah memiliki Game tersebut!")
                                    break

                            # JIKA USER BELUM MEMILIKI GAME TERSEBUT
                            if found == False:
                                kepemilikan[j][1] += [id]

                    # JIKA GAME ID BELUM ADA DI DALAM FILE KEPEMILIKAN
                    if found_game == False:
                        kepemilikan += [[game_id, [id]]]

                # JIKA DATA KEPEMILIKAN MASIH KOSONG
                else:
                    kepemilikan += [[game_id, [id]]]

                # MENGUPDATE ISI ARRAY
                if found == False:
                    stok = int(data_game[index][5])
                    data_game[index][5] = str(stok - 1)
                    saldo = int(data_username[index3][5])
                    data_username[index3][5] = str(saldo - int(data_game[index][4]))
                    
                    # MENYIMPAN DI MEMORY DATA
                    memory_data_riwayat = data_riwayat + [[game_id, data_game[index][1], data_game[index][4], id, str(datetime.now().year)]]
                    memory_data_game = data_game
                    memory_data_user = data_username
                    memory_kepemilikan = kepemilikan
                    print(f"Game “{data_game[index][1]}” berhasil dibeli!")
                    return memory_data_game, memory_data_riwayat, memory_data_user, memory_kepemilikan
            break
    # MEMORY VARIABEL
    memory_data_riwayat = data_riwayat
    memory_data_game = data_game
    memory_data_user = data_username
    memory_kepemilikan = kepemilikan
    # JIKA GAME ID TIDAK DITEMUKAN
    if loop == True:
        print("Game ID tersebut tidak ditemukan.")
    # JIKA STOK DARI GAME HABIS
    elif int(data_game[index][5]) <= 0:
        print("Out of Stock.")
    # JIKA SALDO TIDAK CUKUP
    elif int(data_game[i][4]) >  int(data_username[index3][5]):
        print("Saldo anda tidak cukup.")
    return memory_data_game, memory_data_riwayat, memory_data_user, memory_kepemilikan

# Run
# data = buy_game(game, user, path_kepemilikan, path_riwayat, id) # id dari F03
# data_game = data[0]
# data_riwayat = data[1]
# data_user = data[2]
# data_kepemilikan = data[3]
# print(data_game)
# print(data_riwayat)
# print(data_user)
# print(data_kepemilikan)
