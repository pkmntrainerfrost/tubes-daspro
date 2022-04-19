import time

# FUNGSI KERANG AJAIB
def kerangajaib():
    # I.S. Menerima input dari user
    # F.S. Memberikan jawaban secara acak dari kerang ajaib

    # KAMUS
    # answer : array of string { macam-macam pilihan jawaban } 
    # i : integer { index }
    # ans_time : float { waktu saat enter dari user }
    # loop_index : float

    # ALGORITMA
    # MENERIMA INPUT
    input("Apa pertanyaanmu? ")
    # RAGAM JAWABAN KERANG AJAIB
    answer = ['Iya', 'Tidak', 'Mungkin', 'Bisa jadi', 'Tidak Mungkin', 'Sepertinya', 'Seharusnya', 'Mungkin saja', 'Mungkin Iya']
    # LCG function
    def lcg(seed):
        # Fungsi LCG mengembalikan nilai 'random'
        # KAMUS
        # seed : float
        # a, c, m : integer { konstanta }
        # random : float { random number }
        
        # ALGORITMA
        a, c, m = 8121, 28411, 134456
        seed = (a*seed + c) % m
        random = seed/m # 'random' numbers
        return random
    # Mencatat  waktu saat user menekan enter pada input
    ans_time = time.time() # untuk mendapatkan kapan user melakukan enter
    loop_index = lcg(ans_time)*10 # untuk mendapatkan nilai bulat
    i = int(loop_index % 9) # mencari indeks random untuk jawaban
    return print(answer[i]) # jawaban dari kerang ajaib

# Run
kerangajaib()
