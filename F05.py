# import functions modules
from components.csv import parse, csv_checker
from components.binomo import length

def ubah_game(files): # files = game.csv
    # Ubah Game Function
    # Mengubah informasi game pada toko game
    # Prekondisi : stock tidak bisa diubah
    # KAMUS
    # id, nama_game, kategori : string { input informasi data baru }
    # found : Bool { variabel validasi }
    # tahun_rilis : integer { data baru untuk tahun rilis }
    # harga : real { data baru untuk harga }
    # data : arr of arr of str { data game.csv }
#ALGORITMA
    data = parse(files)
    # MENGVALIDASI KONDISI CSV
    if csv_checker(files):
        # INPUT DATA BARU
        id = input("Masukkan ID game: ")
        nama_game = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")

        # DATA BARU
        data_baru = [id , nama_game , kategori, tahun_rilis, harga, ""] 

        # VALIDASI INPUT ID
        if (id != ""):
            found = False
            # MENGUPDATE DATA LAMA
            for i in range(length(data)):
                for j in data[i]:
                    if id == data[i][0]:
                        for k in range(length(data_baru)):
                            if data_baru[k] != "":
                                data[i][k] = data_baru[k] 
                        found = True
                if found:
                    break
            if found == False:
                print("ID Game tersebut tidak ditemukan.")
            else:
                print("Game dengan ID: ",id," berhasil diubah.")
                return data
        else:
            print("Field ID tidak boleh kosong!")
            
    # JIKA CSV KOSONG / BELUM ADA GAME MAKA PESAN ERROR
    else:
        print("Tidak ada data game yang dapat diubah (data kosong).")
# Run
ubah_game('components\game.csv')