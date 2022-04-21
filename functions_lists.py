#

# ALGORITMA FUNGSI-FUNGSI LIST - SEGMENT (PENGGANTI SLICING)

def segment(list,first,last=-1):

    # Mengembalikan list[first] s.d. list[last] - pengganti slicing

    # KAMUS LOKAL
    # list          : list of any           - list yang hendak disegment
    # first         : int                   - index awal
    # last          : int                   - index akhir
    # new_list      : list of any           - list hasil segmentasi

    # ALGORITMA

    # Jika last tidak ditentukan, simpan panjang list di last
    if last == -1:
        last = length(list)
    
    # Inisialisasi 
    new_list = []

    # Tambahkan setiap elemen dari index first ke index last (inklusif) ke new_list
    for i in range(first,last):
        new_list += [list[i]]
    
    # Output
    return new_list

# ALGORITMA FUNGSI-FUNGSI LIST - KONSTRUKTOR

def konso(element,list): # a homage to my beloved haskell-chan -A
    
    # Menmbuat sebuah list baru dari element dan list, dengan element sebagai elemen pertama

    # KAMUS LOKAL
    # element       : any                   -
    # list          : list of any           -

    # ALGORITMA

    # Output
    return [element] + list

def konsdot(list,element):

    # Menmbuat sebuah list baru dari element dan list, dengan element sebagai elemen terakhir

    # KAMUS LOKAL
    # list          : list of any           -
    # element       : any                   -

    # ALGORITMA

    # Output
    return list + [element]

def konkat(*lists):

    # Mengkonkatenasi semua list dalam lists

    # KAMUS LOKAL
    # lists         : tuple of list         - list-list yang akan dikonkatenasi
    # list          : list of any           - list individu
    # new_list      : list of any           - list hasil konkatenasi

    # ALGORITMA

    # Inisialisasi new_list
    new_list = []

    # Tambahkan setiap list dalam lists ke new_list
    for list in lists:
        new_list += list
    
    # Output
    return new_list

def insert(list,index,element):

    # Menyisipkan element ke dalam list pada index tertentu

    # KAMUS LOKAL
    # list          : list of any           -
    # index         : int                   - index untuk insert, diasumsikan valid
    # element       : any                   -

    # ALGORITMA

    # Output
    return segment(list,0,index) + [element] + segment(list,index+1) 

def remove(list,index):

    # Menghapus elemen pada index tertentu

    # KAMUS LOKAL
    # list          : list of any           -
    # index         : int                   -

    # ALGORITMA

    # Output
    return segment(list,0,index) + segment(list,index+1,length(list))

def delete(list,element,instances=1):

    # Menghapus elemen tertentu pada list

    # KAMUS LOKAL
    # list          : list of any           -
    # element       : any                   -
    # new_list      : list of any           -
    # deleted       : int                   -
    # i             : int                   -

    # ALGORITMA

    # Inisialisasi new_list, deleted, dan i
    new_list = []
    deleted = 0
    i = 0

    # Tambahkan semua elemen list yang != element selama deleted < instances
    for i in list:
        if (i == element) and (deleted < instances):
            deleted += 1
        else:
            new_list += [i]

    # Output
    return new_list

def strain(list,element,inverse=False,matrix=False,col=0):

    if type(col) == int:
        col = [col]
    if type(element) == str:
        element = [element]

    if matrix:
        new_matrix = []
        for row in list:
            match = True
            for i in range(length(element)):
                if (row[col[i]] == element[i]) == inverse:
                    match = False
                    break
            if match:
                new_matrix += row
        return new_matrix
    else:
        new_list = []
        for member in list:
            for i in range(length(element)):
                if (member == element[i]) != inverse:
                    new_list += [member]
                    break
        return new_list

def separate(string,separator=";"):

    # Mengembalikan suatu list yang berisi string-string kecil hasil separasi string berdasarkan separator tertentu - pengganti split()

    # KAMUS LOKAL
    # string        : string                -
    # separator     : char                  -
    # list          : list                  -
    # matrix        : list of list          -

    # ALGORITMA

    list = [""]
    matrix = []
    col = 0
    row = 0

    for char in string:

        if char == "\n":
            matrix += [list]
            list = [""]
            col = 0
            row += 1

        elif char == separator:
            list += [""]
            col += 1

        else:
            list[col] += char
    
    if row > 0:
        matrix += [list]
        return matrix

    return list

# ALGORITMA FUNGSI-FUNGSI LIST - SELEKTOR

def maximum(list):

    # Mengembalikan elemen terbesar pada suatu list - pengganti fungsi max()

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

def is_member(list,element):

    # Mengecek apakah element merupakan anggota dari list

    # KAMUS LOKAL
    # list          : list                  - 
    # element       : any                   -

    # Cek setiap elemen di list, kembalikan true jika sama dengan element
    for i in list:
        if i == element:
            return True
    
    # Output - hanya terjadi apabila tidak ada elemen di list yang sama dengan element
    return False

# ALGORITMA FUNGSI-FUNGSI LIST - LAINNYA

def length(list):

    # Mengembalikan panjang dari list - pengganti fungsi len()

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

    # Mengurutkan elemen-elemen pada list of int/float menggunakan quicksort - pengganti sort()

    # KAMUS LOKAL
    # list          : list of int/float     - list yang akan diurutkan elemennya
    # scheme        : char ("+"/"-")        - skema pengurutan; "+" ascending, "-" descending
    # pivot         : int/float             - elemen yang dijadikan pivot
    # l             : list of int/float     - list yang berisi elemen-elemen < (+) atau > (-) pivot
    # r             : list of int/float     - list yang berisi elemen-elemen >= (+) atau <= (-) pivot
    # i             : int/float             - elemen tertentu pada list

    # ALGORITMA FUNGSI

    # Cek panjang list, kembalikan list bila panjangnya <= 1 - basis
    if length(list) <= 1:

        return list

    # Panjang list > 1
    else:
        
        # Inisialisasi pivot, l, dan r
        pivot = last(list)
        l = []
        r = []

        # Masukkan setiap elemen selain pivot ke dalam l atau r berdasarkan skema
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

        # Output - rekurens
        return sort(l,scheme) + [pivot] + sort(r,scheme)

def index(list,element,occurence=1):

    if occurence == "last":
        for i in range(length(list)-1,-1,-1):
            if list[i] == element:
                return i
    else:
        for i in range(length(list)):
            if list[i] == element:
                return i

    return -1