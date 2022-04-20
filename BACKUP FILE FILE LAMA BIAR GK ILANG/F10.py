from lists import *

def search_my_game(user,data_game,data_kepemilikan):

    user_id = ("user_id",user)

    id = ("id",str(input("Masukkan ID Game: ")))
    tahun_rilis = ("tahun_rilis",str(input("Masukkan Tahun Rilis Game: ")))

    params = [id,user]
    element = []
    col = []

    for i in params:
        if i[1] != "":
            element += [i[1]]
            col += [index(data_kepemilikan[0],i[0])]
    
    games = strain(data_kepemilikan,element,False,True,col)

    if tahun_rilis[1] != "":
        games = strain(data_game)

    # games = strain(data_kepemilikan,user,False,True,index(data_kepemilikan,"user_id"))

    games = strain(data_game,games,False,True,index(data_game,"tahun_rilis"))
    