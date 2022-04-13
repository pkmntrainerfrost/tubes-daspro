# import functions module
from components.binomo import *
from components.csv import *
from datetime import datetime

game = r'components\game.csv'
user = r'components\user.csv'
path_kepemilikan = r'components\kepemilikan.csv'
path_riwayat = r'components\riwayat.csv'

# After login process
# FUNCTION BUY GAME
def buy_game(game_files, user_files, kepemilikan_user_files, id):
    # KAMUS
    # kepemilikan, data_game, data_username : files { csv }
    # arr_id : array of array { tabel data untuk id dari data kepemilikan }
    # index3, index : integer { index untuk file user, index untuk file game }
    # game_id : string { input user }
    # found : Boolean
    # id : string { id user }
    # stok, saldo : integer { stok game tersisa, saldo user }
    # memory_data_riwayat, memory_data_game, memory_data_user, memory_kepemilikan : array of string { memori }
    
    # ALGORITMA
    kepemilikan = parse(kepemilikan_user_files) # data kepemilikan
    data_game = parse(game_files) # data game (stok)
    data_username = parse(user_files) # data user (username)
    # INISIALISASI DATA KEPEMILIKAN
    for i in range(length(kepemilikan)):
        arr_id = parse2(kepemilikan[i][1])
        kepemilikan[i][1] = arr_id
    # MENCARI USER ID
    index3 = 0
    for i in range(length(data_username)):
        if data_username[i][0] == id:
            index3 = i # mencari index dari account
    game_id = input("Masukkan ID Game: ")
    found = False
    for i in range(length(data_game)):
        if data_game[i][0] == game_id:
            index = i # mencari index dari game yang dicari
            found = True
            break
    if found:
        found = False
        if int(data_game[index][5]) > 0 and int(data_username[index3][5]) - int(data_game[index][4]) > 0:
            for i in range(length(kepemilikan)):
                if kepemilikan[i][0] == game_id:
                    for j in range(length(kepemilikan[i][1])):
                        if kepemilikan[i][1][j] == id:
                            found = True
                            print("Anda sudah memiliki Game tersebut!")
                            break
                        else:
                            if j == length(kepemilikan[i][1]) - 1 and kepemilikan[i][1][j] != id:
                                kepemilikan[i][1] += [id]
            if found == False:
                stok = int(data_game[index][5])
                data_game[index][5] = str(stok - 1)
                saldo = int(data_username[index3][5])
                data_username[index3][5] = str(saldo - int(data_game[index][4]))
                # MENYIMPAN DI MEMORY DATA
                memory_data_riwayat = [game_id, data_game[index][1], data_game[index][4], id, str(datetime.now().year)]
                memory_data_game = [data_game[index][0], data_game[index][1], data_game[index][2], data_game[index][3], data_game[index][4], data_game[index][5]]
                memory_data_user = [data_username[index3][0], data_username[index3][1], data_username[index3][2], data_username[index3][3], data_username[index3][4], data_username[index3][5]]
                memory_kepemilikan = kepemilikan
                # JIKA SAVE
                # f = open(riwayat_user_files , 'a')
                # f.write(game_id + ';' + data_game[index][1] +';' + data_game[index][4] + ';' + id + ';' + str(datetime.now().year) + '\n')

                # MENGOSONGI CSV
                # clear_csv(game_files)
                # clear_csv(user_files)
                # clear_csv(kepemilikan_user_files)
                # for m in range(length(data_game)):
                #     edit_files(data_game[m][0], data_game[m][1], data_game[m][2], data_game[m][3], data_game[m][4], data_game[m][5], game_files)
                #     edit_files(data_username[m][0], data_username[m][1], data_username[m][2], data_username[m][3], data_username[m][4], data_username[m][5], user_files)
                # edit_files_2(kepemilikan, kepemilikan_user_files)

                print(f"Game “{data_game[index][1]}” berhasil dibeli!")
        else:
            if int(data_game[index][5]) <= 0:
                print("Stok Game tersebut sedang habis!")
            else:
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
    else:
        print("Invalid input.")
    return memory_data_game, memory_data_riwayat, memory_data_user, memory_kepemilikan

# data_game =  buy_game(game, user, path_kepemilikan, '1')[0]
# data_riwayat = buy_game(game, user, path_kepemilikan, '1')[1]
# data_user = buy_game(game, user, path_kepemilikan, '1')[2]
# data_kepemilikan =  buy_game(game, user, path_kepemilikan, '1')[3]
# print(data_game)
# print(data_riwayat)
# print(data_user)
# print(data_kepemilikan)