from functions_lists import *
from functions_io import print_table

def search_my_game(user,data_game,data_kepemilikan):

    user_id = ("user_id",user)

    id = ("game_id",str(input("Masukkan ID Game: ")))
    tahun_rilis = ("tahun_rilis",str(input("Masukkan Tahun Rilis Game: ")))

    params = [id,user_id]
    element = []
    col = []

    for i in params:
        if i[1] != "":
            element += [i[1]]
            col += [get_index(data_kepemilikan[0],i[0])]

    games_owned = strain(data_kepemilikan[1],element,False,True,col)

    if games_owned == []:

        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

    else:

        if type(games_owned[1]) != list:
            games_owned = [games_owned]

        games = []

        for game in games_owned:
            element = [game[0]]
            col = [get_index(data_game[0],"id")]
            if tahun_rilis[1] != "":
                element += [tahun_rilis[1]]
                col += [get_index(data_game[0],"tahun_rilis")]
            games += [strain(data_game[1],element,False,True,col)]
        
        if games == []:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        else:
            if type(games[1]) != list:
                games = [games]
            print()
            print("Daftar game pada inventory yang memenuhi kriteria:")
            print_table(games)    