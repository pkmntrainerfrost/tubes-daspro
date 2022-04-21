# import functions module
from components.binomo import *
from components.csv import *
from functions_io import print_table
from datetime import datetime

def list_game(files):
    if csv_checker(files):
        print_table(files)
    else : 
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
list_game("'components\game.csv'")
        


