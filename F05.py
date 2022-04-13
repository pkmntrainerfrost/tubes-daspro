# import functions modules
from components.csv import parse, edit_files, csv_checker,  clear_csv
from components.binomo import length

def ubah_game(files): # files = game.csv
    # Ubah Game Function
    # I.S. Menerima input ID Game yang ingin diubah
    # F.S. Mengganti informasi dari ID Game yang dipilih
    # Prekondisi : stock tidak bisa diubah
    # KAMUS
    # id, nama_game, kategori : string { input informasi data baru }
    # found : Bool
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
        # if (tahun_rilis != "" and harga != ""):
        #     if(not(is_integer(tahun_rilis) and (is_integer(harga) or is_float(harga)))):
        #         print("Mohon mengecek input untuk tahun rilis atau harga.")
        #         exit()

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
                # JIKA SAVE
                # PROGRAM SEMENTARA KARENA SAVE TERDAPAT PADA F16
                ans = input("Save? (y/n): ")
                if ans == "y":
                    # MENGOSONGI CSV
                    clear_csv(files)
                    # MENGISI ULANG DENGAN DATA YANG TELAH DIGANTI
                    for i in range(len(data)):
                        edit_files(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], files)
        else:
                print("Field ID tidak boleh kosong!")
            
    # JIKA CSV KOSONG / BELUM ADA GAME MAKA PESAN ERROR
    else:
        print("Tidak ada data game yang dapat diubah (data kosong).")
# Run
ubah_game('components\game.csv')