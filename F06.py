# import functions module
from components.binomo import *
from components.csv import *

def ubahstok(files): # files = game.csv
    # Untuk menghubah stok game 
    # akses admin
    # I.S. Menerima input ID Game yang ingin diubah stoknya
    # F.S. Mengganti informasi dari ID Game yang dipilih
    # KAMUS
    # id,  : string { input informasi data baru }
    # data : arr of arr of str { data game.csv }
#ALGORITMA
    data = parse(files)
    if csv_checker(files):
        # INPUT ID
        id=input("Masukkan ID game :") 
        if (id != ""):
            found = False
        #MENCARI INDEX DARI ID    
            for i in range(length(data)):
                for j in data[i]:
                    if id == data[i][0]:
                        index=i
                        found = True
                if found: #JIKA UDAH KETEMU LANGSUNG BREAK
                    break 
            if found == False :
                print("Game not found")
            else :  
                tambah_stok=int(input("Masukkan jumlah :"))
                if (data[index][5]+tambah_stok)<0:
                    print("Stok game {} gagal dikurangi karena stok kurang. Stok sekarang: {} (<{})".format(data[index][1],data[index][5],-1*tambah_stok))
                else : 
                    if tambah_stok>=0 :
                        data[index][5]+=tambah_stok
                        print("Stok game {} berhasil ditambahkan. Stok sekarang: {}".format(data[index][1],data[index][5]))
                    else : 
                        data[index][5]+=tambah_stok
                        print("Stok game {} berhasil dikurangi. Stok sekarang: {}".format(data[index][1],data[index][5]))
            
        else:
                print("Field ID tidak boleh kosong!")
            
    # JIKA CSV KOSONG / BELUM ADA GAME MAKA PESAN ERROR
    else:
        print("Data kosong.")
    return data
