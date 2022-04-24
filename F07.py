from functions_lists import *
from functions_io import *
from functions_strings import *
from functions_validation import is_alphabet

# Mission Board
# 1. Mencari cara sorting data sesuai kategori
# 2. Mencari cara melakukan display data
# 3. Mencari cara implementasi fungsi sorting dan parser buatan
# 4. Mencari kemungkinan penggunaan fungsi buatan lain(tail,init,etc)

def list_game_toko(data_game):

    skema = str(input("Skema sorting: "))

    atribut = ""
    urutan = ""
    i = 0

    while i < length(skema) and is_alphabet(skema[i]):
        atribut += skema[i]
        i += 1

    atribut = atribut.lower()
    urutan = segment(skema,i)

    if (urutan != "+" and urutan != "-") or (atribut != "tahun" and atribut != "harga"):
        print("Skema sorting tidak valid!")
    else:
        games = data_game[1]

        if type(games[1]) != list:
            games = [games]

        if atribut == "tahun":
            atribut = "tahun_rilis"

        games = sort(games,urutan,True,get_index(data_game[0],atribut))
        print_table(games)