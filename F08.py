# import functions module
from functions_lists import *
from datetime import date

# id = login(user)

# After login process
# FUNCTION BUY GAME

def buy_game(user_id,data_game,data_user,data_riwayat,data_kepemilikan):

    id_game = str(input("Masukkan ID Game: "))

    user = strain(data_user[1],str(user_id),False,True,get_index(data_user[0],"id"))
    game = strain(data_game[1],id_game,False,True,get_index(data_game[0],"id"))

    if game == []:
        print("Game tidak ditemukan!")
    else:
        if strain(data_kepemilikan[1],[id_game,str(user_id)],False,True,[get_index(data_kepemilikan[0],"game_id"),get_index(data_kepemilikan[0],"user_id")]) != []:
            print("Anda sudah memiliki game tersebut!")
        else:
            user_row = get_index(data_user[1],user)
            game_row = get_index(data_game[1],game)

            harga = int(game[get_index(data_game[0],"harga")])
            stok = int(game[get_index(data_game[0],"stok")]) - 1

            saldo = int(user[get_index(data_game[0],"saldo")]) - harga

            if saldo < 0:
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")

            elif stok < 0:
                print("Stok Game tersebut sedang habis!")
            
            else:
                game_title = game[get_index(data_game[0],"nama")]
                tahun_beli = str(date.today().year)

                user[get_index(data_game[0],"saldo")] = str(saldo)
                game[get_index(data_game[0],"stok")] = str(stok)

                data_user = (data_user[0],konkat(segment(data_user[1],0,user_row),[user],segment(data_user[1],user_row + 1)))
                data_game = (data_game[0],konkat(segment(data_game[1],0,game_row),[game],segment(data_game[1],game_row + 1)))
                data_riwayat = (data_riwayat[0],konsdot(data_riwayat[1],[id_game,game_title,str(harga),str(user_id),tahun_beli]))
                data_kepemilikan = (data_kepemilikan[0],konsdot(data_kepemilikan[1],[id_game,str(user_id)]))

                print('Game "' + game_title + '" berhasil dibeli!')

                return (data_user,data_game,data_riwayat,data_kepemilikan)
            
    return (data_user,data_game,data_riwayat,data_kepemilikan)