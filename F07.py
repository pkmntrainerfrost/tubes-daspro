import csv
from binomo.py import parse, length, last, init

# Mission Board
# 1. Mencari cara sorting data sesuai kategori
# 2. Mencari cara melakukan display data
# 3. Mencari cara implementasi fungsi sorting dan parser buatan
# 4. Mencari kemungkinan penggunaan fungsi buatan lain(tail,init,etc)

def sort_game(list,key,scheme="+"):

    # Mengurutkan elemen-elemen pada list of int/float menggunakan algoritma quicksort - pengganti sort()
    # I.S.: list merupakan sebuah list of int/float, scheme sembarang (selain "+"/"-", akan ascending)
    # F.S.: sebuah list baru yang berisi elemen-elemen list, tetapi terurut berdasarkan skema scheme

    # KAMUS LOKAL
    # list          : list of int/float     - list yang akan diurutkan elemennya
    # scheme        : char ("+"/"-")        - skema pengurutan; "+" ascending, "-" descending
    # pivot         : int/float             - elemen yang dijadikan pivot
    # l             : list of int/float     - list yang berisi elemen-elemen < (+) atau > (-) pivot
    # r             : list of int/float     - list yang berisi elemen-elemen >= (+) atau <= (-) pivot
    # i             : int/float             - elemen tertentu pada list

    # ALGORITMA FUNGSI

    # CEK PANJANG list, KEMBALIKAN list BILA <= 1
    if length(list) <= 1:

        return list

    # PANJANG list > 1
    elif key == '' or key == "tahun_rilis" or key == 'harga':
        # penentuan kategori sorting
        if key == "tahun_rilis":
            j = 3
        elif key == 'harga':
            j = 4
        else:
            j = 0

        # INISIALISASI LIST pivot, l, DAN r
        pivot = last(list)
        l = []
        r = []

        # MASUKKAN SETIAP ELEMEN SELAIN pivot KE DALAM l ATAU r BERDASARKAN SKEMA
        for i in init(list):
            if scheme == "-":
                # mensorting kategori (element of list inside list)
                if list[i][j] > pivot[j]:
                    l += [i]
                else:
                    r += [i]
            else:
                if list[i][j] < pivot[j]:
                    l += [i]
                else:
                    r += [i]

        # OUTPUT
        return sort_game(l,key,scheme) + [pivot] + sort_game(r,key,scheme)
    else:
        error_msg = 'Skema sorting tidak valid!'
        return error_msg
    
# Main Function
def list_game_toko():
    data = parse('game.csv')
    skema = str(input("Skema sorting : "))
    category = skema[:-1]

    if skema[-1] == '+' or skema[-1] == '':
        display = sort_game(data,category,scheme='+')
        print(display)
    elif skema[-1] == '-':
        display = sort_game(data,category,scheme='-')
        print(display)
    else:
        print("Skema sorting tidak valid!")
