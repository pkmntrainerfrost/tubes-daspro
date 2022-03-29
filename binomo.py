# Program BNMO
# 

# KAMUS

# ALGORITMA PARSER

def parse(file):

    # KAMUS LOKAL
    # f             : file                  - file yang di-parse
    # raw_data      : str                   - data mentah file
    # cols, row     : int                   - jumlah kolom dan baris
    # col, row, j   : int                   - index
    # i             : char/int              - index
    # data          : list of lists of str  - data hasil parsing

    # ALGORITMA

    # BUKA FILE, SIMPAN DI STRING raw_data
    f = open(file,"r")
    raw_data = f.read()
    f.close()

    # MENGHITUNG JUMLAH BARIS DAN KOLOM
    cols = 1
    rows = 1

    for i in raw_data:
        if i == ";":
            cols += 1
        if i == "\n":
            rows += 1
            cols = 1
    
    # INISIALISASI LIST OF LIST OF STR data 
    data = [["" for j in range(cols)] for i in range(rows)]

    # SIMPAN DATA DI LIST OF LIST OF STR data
    col = 0
    row = 0

    for i in raw_data:
        if (i != ";") and (i != "\n"):
            data[row][col] += i
        elif (i == ";"):
            col += 1
        else:
            row += 1
            col = 0 

    # KEMBALIKAN LIST OF LIST OF STR data
    return data

def add_game():

    global game

    nama = str(input("Masukkan nama game: "))
    kategori = str(input("Masukkan kategori: "))
    tahun_rilis = str(input("Masukkan tahun rilis: "))
    harga = str(input("Masukkan harga: "))
    stok_awal = str(input("Masukkan stok awal: "))

    nama_valid = nama != ""
    kategori_valid = kategori != ""

    try:
        shirakami_fubuki = tahun_rilis + harga + stok_awal + 1
    except:
        numerics_valid = False
    else:
        numerics_valid = True

    valid = nama_valid and kategori_valid and numerics_valid

    if valid:
        
        id = ""

        for i in game:
            id = i[0]
        
        id = int(id[-3:]) + 1

        if id < 100:
            id = "0" + str(id)

        game += [["GAME"+id,nama,kategori,tahun_rilis,harga,stok_awal]]
    
    else:

        print("eror")

game = parse("game.csv")
add_game()
print(game)
