import fungsi_user as user
import fungsi_admin as admin
from F03.py import logged_in, login, admin_status

# Mision Board
# 1. Mencari cara menentukan sudah login atau belum
# 2. Mencari cara penentuan admin_status dari fungsi login() atau menambahkan integrated login function agar admin_status dikenali
# 3. Membuat fungsi_user dan fungsi_admin dari fungsi fungsi yang ada 
# 4. 

def asciiart():
    print("============ HELP ============")

def help():
    asciiart()
    global admin_ID, user_ID
    login() # Mengecek status dan role dengan fungsi login

    if logged_in == False:
    #   print all options
        print("1. register - Untuk melakukan registrasi user baru")
        print("2. login - Untuk melakukan login ke dalam sistem")
        print("3. tambah_game - Untuk menambah game yang dijual pada toko")
        print("4. ubah_game - Mengubah informasi game pada toko game")
        print("5. ubah_stok - Mengubah stok suatu game pada toko")
        print("6. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("7. search_game_at_store - Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis")
        print("8. topup - prosedur untuk menambahkan saldo kepada User")
        print("3. buy_game - prosedur bagi user untuk membeli game")
        print("4. list_game - memberikan daftar game yang dimiliki pengguna")
        print("5. search_my_game - mencari game yang dimiliki dari ID dan tahun rilis")
        print("7. riwayat - melihat riwayat pembelian user")
        print("9. help")
        print("10. load")
        print("11. save")
        print("12. exit")

        # Jika belum login hanya bisa login dan help

    else: # logged_in == True
        if admin_status == True:
            print("1. register - Untuk melakukan registrasi user baru")
            print("2. login - Untuk melakukan login ke dalam sistem")
            print("3. tambah_game - Untuk menambah game yang dijual pada toko")
            print("4. ubah_game - Mengubah informasi game pada toko game")
            print("5. ubah_stok - Mengubah stok suatu game pada toko")
            print("6. list_game_toko - Untuk melihat list game yang dijual pada toko")
            print("7. search_game_at_store - Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis")
            print("8. topup - prosedur untuk menambahkan saldo kepada User")
            print("9. help")
            print("10. load")
            print("11. save")
            print("12. exit")

            command = input(">>> ").lower()
            print("Opsi: {}".format(command))
            print("\n")

            if command == "register":
                admin.register
            elif command == "login":
                admin.login
            elif command == "tambah_game":
                admin.tambah_game
            elif command == "ubah_game":
                admin.ubah_game
            elif command == "ubah_stok":
                admin.ubah_stok
            elif command == "list_game_toko":
                admin.list_game_toko
            elif command == "search_game_at_store":
                admin.search_game_at_store
            elif command == "topup":
                admin.topup
            elif command == "exit":
                #save()
                exit()
            else:
                print("Opsi tidak dikenali!")
                
        else: # admin_status == False, maka yang login adalah user
            print("1. login - Untuk melakukan login ke dalam sistem")
            print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
            print("3. buy_game - prosedur bagi user untuk membeli game")
            print("4. list_game - memberikan daftar game yang dimiliki pengguna")
            print("5. search_my_game - mencari game yang dimiliki dari ID dan tahun rilis")
            print("6. search_game_at_store - mencari game di toko dari ID, nama game, harga, kategori dan tahun rilis")
            print("7. riwayat - melihat riwayat pembelian user")
            print("8. help")
            print("9. load")
            print("10. save")
            print("11. exit")

            command = input(">>> ").lower()
            print("Opsi: {}".format(command))
            print("\n")

            if command == "login":
                user.login
            elif command == "list_game_toko":
                user.list_game_toko
            elif command == "buy_game":
                user.buy_game
            elif command == "list_game":
                user.list_game
            elif command == "search_my_game":
                user.search_my_game
            elif command == "search_game_at_store":
                user.search_game_at_store
            elif command == "riwayat":
                user.riwayat
            elif command == "exit":
                #save()
                exit()
            else:
                print("Opsi tidak dikenali!")