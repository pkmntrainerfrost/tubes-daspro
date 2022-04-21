def order(char):

    if is_uppercase(char):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

    return index(alphabet,char)
    
def uppercase(order):

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return uppercase[order]

def lowercase(order):

    lowercase = "abcdefghijklmnopqrstuvwxyz"

    return lowercase[order]

def cipher(text,key,mode):

    # cipher v 0.1 aka frost's cipher
    # modified vigenere cipher; saya namakan frost's cipher karena ya saya sedikit narsis
    # untuk huruf mengikuti vigenere cipher biasa
    # untuk angka, k = a mod 10 dimana a adalah urutan k dalam alfabet [a=0,b=1,...]
    #              o = (t + k) mod 10
    # untuk karakter selain huruf dan angka tidak dienkripsi

    result = ""
    keychr = 0

    for i in text:

        if is_alphabetical(i):
            
            t = order(i)
            k = order(key[keychr])
            
            if mode == "encrypt":
                o = (t + k) % 26
            else:
                o = (t - k) % 26

            if is_lowercase(i):
                result += lowercase(o)
            else:
                result += uppercase(o)

            keychr = (keychr + 1) % length(key)

        elif is_integer(i):

            t = int(i)
            k = order(key[keychr]) % 10
            
            if mode == "encrypt":
                o = (t + k) % 10
            else:
                o = (t - k) % 10

            result += str(o)

            keychr = (keychr + 1) % length(key)

        else:

            result += i
    
    return result