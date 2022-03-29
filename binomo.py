# Program BNMO
# 

# KAMUS

# ALGORITMA FUNGSI

def is_integer(x):

    try:
        y = int(x)
    except:
        return False
    else:
        return True

def remove_delimiter(x):

    y = ""

    for i in x:
        if i != "." and i != ",":
            y += i

    return y

# ALGORITMA FUNGSI-FUNGSI YANG BERHUBUNGAN DENGAN LIST

def maximum(list):

    max = list[0]

    for i in list:
        if i > max:
            max = i

    return max

def minimum(list):

    min = list[0]

    for i in list:
        if i < min:
            min = i

    return min

def length(list):

    # KAMUS LOKAL
    # list          : list                  - list
    # length        : int                   - panjang list/str
    # i             : int                   - index

    # ALGORITMA

    # INISIALISASI INTEGER length
    length = 0

    # HITUNG PANJANG list
    for i in list:
        length += 1
    
    # KEMBALIKAN INTEGER length
    return length

def remove_index(list,index):

    new_list = []

    for i in range(length(list)):
        if i != index:
            new_list += [list[i]]

    return new_list

def remove_element(list,element):

    new_list = []

    index = element_index(list,element)

    new_list += get_element(list,0,index)
    new_list += get_element(list,index+1)

    return new_list

def remove_all_of_element(list,element):

    new_list = []

    for i in range(length(list)):
        if list[i] != element:
            new_list += [list[i]]

    return new_list

def element_index(list,element):

    for i in range(length(list)):
        if list[i] == element:
            return i

def get_element(list,first,last=-1):

    if last == -1:
        last = length(list)

    new_list = []

    for i in range(first,last):
        new_list += [list[i]]
    
    return new_list

def insert_element(list,index,element):

    new_list = []

    new_list += get_element(list,0,index)
    new_list += element
    new_list += get_element(list,index)

    return new_list

def head(list):

    return list[0]

def tail(list):

    return get_element(list,1)

def init(list):

    return get_element(0,length(list)-1)

def last(list):

    return list[length(list)-1]

def sort(list,scheme="+"):

    old_list = list
    new_list = []

    while length(new_list) != length(list):
        if scheme == "+":
            new_list += [minimum(old_list)]
            old_list = remove_element(old_list,minimum(old_list))
        else:
            new_list += [maximum(old_list)]
            old_list = remove_element(old_list,maximum(old_list))

    return new_list

# ALGORITMA PARSER

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

print(sort([5,2,31,24,4,1,23,12412]))