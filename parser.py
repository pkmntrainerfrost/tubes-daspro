from lists import separate

def parse(file):

    # KAMUS LOKAL
    # file          : str                   - nama + path file yang hendak di-parse
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

    data = separate(raw_data)

    # KEMBALIKAN LIST OF LIST OF STR data
    return data

def rewrite(file,data):
    return