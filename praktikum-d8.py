pwd_benar = 'si23d'
pwd_benar2 = 'MHSITH'
pwd_benar3 = '2023'

def cekpass(id_password, password, page):
    limit = 3
    i = 0
    while i < limit:
        pwd = input(f'Masukkan Password {id_password} untuk Halaman {page}= ')
        if pwd == password:  
            print(f'Password Benar, Selamat Datang di Halaman {page}')
            return True
        else:
            i += 1
            if i == limit:
                print('Kesempatan Anda Habis!')
                return False
            else:
                print(f'Password Salah. Kesempatan anda tersisa {limit - i} kali')

# Tes password pertama
tes1 = cekpass('pertama', 'si23d', 1)
if tes1:
    # Tes password kedua
    tes2 = cekpass('kedua', 'MHSITH', 2)
    if tes2:
        # Tes password ketiga
        tes3 = cekpass('ketiga', '2023', 3)
        if tes3:
            print('Selamat Anda Berhasil Login')
