# Tugas Besar IF 1210 Dasar Pemrograman

# Kelompok 06 / Kelas 07
# NIM - Nama Anggota Kelompok:
# 16521213 - Salman Ma'arif Achsien

# TODO:
# TULIS PROGRAM UTAMA
# TULIS KAMUS UTAMA
# TULIS KOMEN
# RAPIHKAN KODE, JADIKAN KONSISTEN

# Program BNMO
# 

# KAMUS

# ALGORITMA FUNGSI-FUNGSI LIST - KONSTRUKTOR

def konso(element,list):

    return [element] + list

def konsdot(list,element):

    return list + [element]

def konkat(*lists):

    new_list = []

    for list in lists:
        new_list += list

    return new_list

def insert(list,index,element):

    return 

def remove(list,index):

    return segment(list,0,index) + segment(list,index+1,length(list))

def delete(list,element,instances=1):

    new_list = []
    deleted = 0
    i = 0

    while (i < length(list)) and (deleted < instances):
        if list[i] == element:
            deleted += 1
        else:
            new_list += list[i]
        i += 1

    return new_list

# ALGORITMA FUNGSI-FUNGSI LIST - SELEKTOR

def segment(list,first,last=-1):

    # Mengembalikan list[first] s.d. list[last1] - pengganti slicing
    # I.S.: 
    # F.S.: List baru yang terdiri hanya atas semua elemen dari list[first] s.d. list[last1]

    # KAMUS LOKAL
    # list          : list of any           - list yang akan di-segment
    # first         : int                   - index awal
    # last          : int                   - index akhir
    
    # ALGORITMA FUNGSI

    if last == -1:
        last = length(list)
    
    new_list = []

    for i in range(first,last):
        new_list += [list[i]]
    
    return new_list

def maximum(list):

    # Mengembalikan elemen terbesar pada suatu list - pengganti fungsi max()
    # I.S.: List merupakan sebuah list yang tidak kosong dan elemennya bertipe int/float
    # F.S.: Elemen terbesar pada list

    # KAMUS LOKAL
    # list          : list of int/float     - list yang akan dicari elemen terbesarnya
    # max           : int/float             - elemen terbesar pada list
    # i             : int/float             - elemen tertentu pada list

    # ALGORITMA FUNGSI
    
    # INISIALISASI INTEGER max
    max = list[0]

    # CEK SEMUA ELEMEN PADA list, GANTI MAX DENGAN i BILA i > max
    for i in list:
        if i > max:
            max = i

    # OUTPUT
    return max

def minimum(list):

    # Mengembalikan elemen terkecil pada suatu list - pengganti fungsi min()
    # I.S.: List merupakan sebuah list yang tidak kosong dan elemennya bertipe int/float
    # F.S.: Elemen terkecil pada list

    # KAMUS LOKAL
    # list          : list of int/float     - list yang akan dicari elemen terkecilnya
    # min           : int/float             - elemen terkecil pada list
    # i             : int/float             - elemen tertentu pada list

    # ALGORITMA FUNGSI
    
    # INISIALISASI INTEGER min
    min = list[0]

    # CEK SEMUA ELEMEN PADA list, GANTI min DENGAN i BILA i < min
    for i in list:
        if i < min:
            min = i

    # OUTPUT
    return min

def head(list):

    return list[0]

def tail(list):
    
    return segment(list,1)

def init(list):

    return segment(list,0,length(list)-1)

def last(list):
    
    return list[length(list)-1] 

# ALGORITMA FUNGSI-FUNGSI LIST - PREDIKAT

def is_empty(list):

    if list == []:
        return True
    else:
        return False

def is_length(list,length):
    
    if length(list) == length:
        return True
    else:
        return False

def is_ordered(list,scheme=""):

    asc = sort(list,"+")
    dsc = sort(list,"-")

    if scheme == "+":
        ordered = list == asc
    elif scheme == "-":
        ordered = list == dsc
    else:
        ordered = list == asc or list == dsc
    
    return ordered

# ALGORITMA FUNGSI-FUNGSI LIST - LAINNYA

def length(list):

    # Mengembalikan panjang dari list - pengganti fungsi len()
    # I.S.: 
    # F.S.: Panjang dari list

    # KAMUS LOKAL
    # list          : list of any           - list yang akan dihitung panjangnya
    # length        : int                   - panjang list
    # i             : any                   - elemen tertentu pada list

    # ALGORITMA FUNGSI
    
    # INISIALISASI INTEGER length
    length = 0

    # HITUNG PANJANG list
    for i in list:
        length += 1
    
    # OUTPUT
    return length

def sort(list,scheme="+"):

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
    else:
        
        # INISIALISASI LIST pivot, l, DAN r
        pivot = last(list)
        l = []
        r = []

        # MASUKKAN SETIAP ELEMEN SELAIN pivot KE DALAM l ATAU r BERDASARKAN SKEMA
        for i in init(list):
            if scheme == "-":
                if i > pivot:
                    l += [i]
                else:
                    r += [i]
            else:
                if i < pivot:
                    l += [i]
                else:
                    r += [i]

        # OUTPUT
        return sort(l,scheme) + [pivot] + sort(r,scheme)

# ALGORITMA FUNGSI-FUNGSI VALIDASI

def is_integer(object):

    try:
        object = int(object)
    except:
        return False
    else:
        return True

def is_list(object):

    try:
        length = length(object)
    except:
        return False
    else:
        return True

