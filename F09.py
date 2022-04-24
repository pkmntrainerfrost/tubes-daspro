# import functions module
from functions_io import print_table
from functions_lists import *
        
def list_game(user_id,data_game,data_kepemilikan):

    games_owned = strain(data_kepemilikan[1],str(user_id),False,True,get_index(data_kepemilikan,"user_id"))

    if games_owned != []:

        if type(games_owned[1]) != list:
            games_owned = [games_owned]

        col = []
        games = []
        for game in games_owned:
            element = [game[0]]
            col = [get_index(data_game[0],"id")]
            games += [strain(data_game[1],element,False,True,col)]
        if type(games[1]) != list:
            games = [games]
        print_table(games)
    else:
        print("Maaf, anda belum membeli game. Ketik perintah beli_game untuk beli.")