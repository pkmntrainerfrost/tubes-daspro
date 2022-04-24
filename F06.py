# import functions module
from functions_lists import *
from functions_strings import *

def ubah_stok(data_game): # files = game.csv
    # Untuk menghubah stok game 
    # akses admin
    # I.S. Menerima input ID Game yang ingin diubah stoknya
    # F.S. Mengganti informasi dari ID Game yang dipilih
    # KAMUS
    # id,  : string { input informasi data baru }
    # data : arr of arr of str { data game.csv }
#ALGORITMA
    id = str(input("Masukkan ID game: "))

    if is_empty_string(id):
        print("ID game tidak boleh kosong!")
        return data_game
    else:
        game = []
        index = 0
        for row in data_game[1]:
            if row[get_index(data_game[0],"id")] == id:
                game = row
                break
            index += 1
        if game != []:
            try:
                perubahan_stok = int(input("Masukkan jumlah: "))
            except:
                print("Jumlah harus berupa integer!")
                return data_game
        
        if int(game[get_index(data_game[0],"stok")]) + perubahan_stok < 0:
            print("Stok game", game[get_index(data_game[0],"nama")],"gagal dikurangi karena stok kurang. Stok sekarang:",game[get_index(data_game[0],"stok")], "(<", perubahan_stok + ")" )
            return data_game
        else:
            game[get_index(data_game[0],"stok")] = str(int(game[get_index(data_game[0],"stok")]) + perubahan_stok)
            if perubahan_stok < 0:
                print("Stok game", game[get_index(data_game[0],"nama")],"berhasil dikurangi. Stok sekarang:", game[get_index(data_game[0],"stok")])
            if perubahan_stok == 0:
                print("Stok game", game[get_index(data_game[0],"nama")],"tidak diubah. Stok sekarang:", game[get_index(data_game[0],"stok")])
            if perubahan_stok > 0:
                print("Stok game", game[get_index(data_game[0],"nama")],"berhasil ditambahkan. Stok sekarang:", game[get_index(data_game[0],"stok")])
            return (data_game[0],konkat(segment(data_game[1],0,index),[game],segment(data_game[1],index+1)))

    if length(data) > 0:
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
