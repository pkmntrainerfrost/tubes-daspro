from lists import is_member

def user_input():

    global commands
    global status
    global role

    user_input = str(input(">>> ",end=""))
    user_input = user_input.lower()

    for i in commands:
        if is_member(i,user_input):
            if status != i[3] and i[3] != 0:
                if i[3] == 1:
                    print("Anda harus login terlebih dahulu.")
                if i[3] == 2:
                    print("Anda sudah login.")
                return False
            if role != i[2] and i[2] != 0:
                if i[2] == 1:
                    print("")
                if i[2] == 2:
                    print("")
                return False
            return user_input
    
    print("Fungsi tidak ditemukan.")
    return False

def define_commands():

    commands = []

    # Setiap perintah disimpan sebagai sebuah tuple di dalam list of tuple
    # Isi tuple adalah sebagai berikut - (nama,deskripsi,izin,status)
    # Untuk izin, 0 berarti semua user, 1 berarti user, 2 berarti admin
    # Untuk status, 0 berarti bisa dilakukan kapan saja, 1 berarti harus login, 2 berarti sebelum login

    commands += [("register","lorem",1,0)]

    return commands