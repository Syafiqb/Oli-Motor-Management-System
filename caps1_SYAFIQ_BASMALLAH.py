
from prettytable import PrettyTable



daftar_oli  = [
    ['CASRR','CASTROL',20,75000,'REGULER'],
    ['CASST','CASTROL',20,100000,'SPORT'],
    ['SHERR','SHELL',15,80000,'REGULER'],
    ['SHEST','SHELL',25,100000,'SPORT'],
    ['MOTST','MOTUL',25,100000,'SPORT'],
    ]

### SUBMENU READ
def tampilkan_daftar_oli(): 
    if len(daftar_oli)== 0:
        print('''
-----------------------                   
Data tidak tersedia !!!
-----------------------
              ''')
    else:
        table = PrettyTable()
        table.field_names = ["Kode oli", "Merk Oli", "Stock", "Harga", "Kategori"]
        print('\nDaftar Oli') 
        for i in range(len(daftar_oli)):
            table.add_row([daftar_oli[i][0], daftar_oli[i][1], daftar_oli[i][2],f'Rp.{daftar_oli[i][3]:,}', daftar_oli[i][4]])
        print(table)  

def daftar_detail():
    if len(daftar_oli)== 0:
        print('''
-----------------------                   
Data tidak tersedia !!!
-----------------------
              ''')
    else:
        table = PrettyTable()
        table.field_names = ["Kode oli", "Merk Oli"]
        print('\nDaftar Oli') 
        for i in range(len(daftar_oli)):
            table.add_row([daftar_oli[i][0], daftar_oli[i][1]])
        print(table)  
        while True:
            kode_oli = input('Masukkan kode oli yang ingin Anda cari: ').upper().strip()

            oli_ditemukan = None
            for item in daftar_oli:
                if item[0] == kode_oli:
                    oli_ditemukan = item
                    break  
            if oli_ditemukan is None:
                print(f'''
--------------------------------------
Kode oli "{kode_oli}" tidak ditemukan!
--------------------------------------
                ''')
                continue

            detail_table = PrettyTable()
            detail_table.field_names = ["Kode", "Merk", "Stock", "Harga (Rp)", "Kategori"]
            detail_table.add_row([oli_ditemukan[0], oli_ditemukan[1], oli_ditemukan[2], f"{oli_ditemukan[3]:,}", oli_ditemukan[4]])
            
            print("\nOli yang Anda cari adalah:")
            print(detail_table)
            break

def urutkan_stok_oli():
    if len(daftar_oli) == 0:  
        print('''
-----------------------                   
Data tidak tersedia !!!
-----------------------
              ''')
        return  
    else:
        while True:
            pilihan_urut = input('''
-------------------------------------------
Pilih Opsi Pengurutan Stok:
1. Dari Stok Terendah ke Tertinggi
2. Dari Stok Tertinggi ke Terendah
3. Kembali ke Menu Daftar Oli
Masukkan pilihan Anda: ''')

            daftar_oli_sort = daftar_oli.copy()
            
            if pilihan_urut == '1':  
                for i in range(len(daftar_oli_sort) - 1):
                    for j in range(len(daftar_oli_sort) - i - 1):
                        if daftar_oli_sort[j][2] > daftar_oli_sort[j + 1][2]:  
                            daftar_oli_sort[j], daftar_oli_sort[j + 1] = daftar_oli_sort[j + 1], daftar_oli_sort[j]
                print("\nDaftar Oli (Stok Terendah ke Tertinggi):")
                table = PrettyTable()
                table.field_names = ["Kode Oli", "Merk Oli", "Stock", "Harga (Rp)", "Kategori"]
                for oli in daftar_oli_sort:
                    table.add_row([oli[0], oli[1], oli[2], f"Rp.{oli[3]:,}", oli[4]])
                print(table)

            elif pilihan_urut == '2':  
                for i in range(len(daftar_oli_sort) - 1):
                    for j in range(len(daftar_oli_sort) - i - 1):
                        if daftar_oli_sort[j][2] < daftar_oli_sort[j + 1][2]:  
                            daftar_oli_sort[j], daftar_oli_sort[j + 1] = daftar_oli_sort[j + 1], daftar_oli_sort[j]
                print("\nDaftar Oli (Stok Tertinggi ke Terendah):")
                table = PrettyTable()
                table.field_names = ["Kode Oli", "Merk Oli", "Stock", "Harga (Rp)", "Kategori"]
                for oli in daftar_oli_sort:
                    table.add_row([oli[0], oli[1], oli[2], f"Rp.{oli[3]:,}", oli[4]])
                print(table)

            elif pilihan_urut == '3':  
                break

            else:
                print('Invalid Input !!!')
                
def urutkan_harga_oli():
    if len(daftar_oli) == 0:  
        print('''
-----------------------                   
Data tidak tersedia !!!
-----------------------
              ''')
        return  
    else:
        while True:
            pilihan_urut = input('''
-------------------------------------------
Pilih Opsi Pengurutan Harga:
1. Dari Harga Terendah ke Tertinggi
2. Dari Harga Tertinggi ke Terendah
3. Kembali ke Menu Daftar Oli
Masukkan pilihan Anda: ''')
            daftar_oli_sort = daftar_oli.copy() 
            if pilihan_urut == '1':  
                for i in range(len(daftar_oli_sort) - 1):
                    for j in range(len(daftar_oli_sort) - i - 1):
                        if daftar_oli_sort[j][3] > daftar_oli_sort[j + 1][3]:  
                            daftar_oli_sort[j], daftar_oli_sort[j + 1] = daftar_oli_sort[j + 1], daftar_oli_sort[j]
                print("\nDaftar Oli (Harga Terendah ke Tertinggi):")
                table = PrettyTable()
                table.field_names = ["Kode Oli", "Merk Oli", "Stock", "Harga (Rp)", "Kategori"]
                for oli in daftar_oli_sort:
                    table.add_row([oli[0], oli[1], oli[2], f"Rp.{oli[3]:,}", oli[4]])
                print(table)

            elif pilihan_urut == '2':  
                for i in range(len(daftar_oli_sort) - 1):
                    for j in range(len(daftar_oli_sort) - i - 1):
                        if daftar_oli_sort[j][3] < daftar_oli_sort[j + 1][3]:  
                            daftar_oli_sort[j], daftar_oli_sort[j + 1] = daftar_oli_sort[j + 1], daftar_oli_sort[j]
                print("\nDaftar Oli (Harga Tertinggi ke Terendah):")
                table = PrettyTable()
                table.field_names = ["Kode Oli", "Merk Oli", "Stock", "Harga (Rp)", "Kategori"]
                for oli in daftar_oli_sort:
                    table.add_row([oli[0], oli[1], oli[2], f"Rp.{oli[3]:,}", oli[4]])
                print(table)

            elif pilihan_urut == '3':  
                break

            else:
                print('Invalid Input !!!')




### SUBMENU CREATE
def menambah_data_oli():
    tampilkan_daftar_oli()
    while True:
        try:
            nama_oli = input('Masukkan Nama Oli : ').upper().strip()
            if len(nama_oli) < 1: 
                print('Nama oli tidak boleh kosong!')
                continue

            while True:
                try:
                    stock_oli = int(input('Masukkan Jumlah Stock Oli : '))
                    if stock_oli <= 0:
                        print('''
---------------------------------------
Stock oli tidak boleh bernilai negatif!
---------------------------------------
                        ''')
                        continue
                    break  
                except ValueError:
                    print('''
----------------------------------------------
Masukkan angka yang valid untuk jumlah stock!
----------------------------------------------
                    ''')

            while True:
                try:
                    harga_oli = int(input('Masukkan Harga Oli : '))
                    if harga_oli <= 0:
                        print('''
----------------------------------------
Harga oli tidak boleh bernilai negatif!
----------------------------------------
                        ''')
                        continue
                    break  
                except ValueError:
                    print('''
----------------------------------------------
Masukkan angka yang valid untuk harga oli!
----------------------------------------------
                    ''')

            while True:
                kategori_oli = input('Masukkan Kategori Oli (Sport/Reguler) : ').upper().strip()
                if kategori_oli not in ['SPORT', 'REGULER']:
                    print('''
-------------------------------------------------                   
Input kategori yang anda masukkan tidak valid !!!
Masukkan hanya "Sport" atau "Reguler".
-------------------------------------------------
                      ''')
                    continue
                break  

            for item in daftar_oli:
                if item[1] == nama_oli and item[4] == kategori_oli:
                    print(f'''
-----------------------------------------------------------------
Nama oli "{nama_oli}" dengan kategori "{kategori_oli}" sudah ada!
-----------------------------------------------------------------
                      ''')
                    break  
            else:
                kode_oli = generate_kode_oli(nama_oli, kategori_oli)

                validasitambah = input('Apakah anda yakin ingin menambahkan item ini? (Y/N): ').upper()
                if validasitambah == 'Y':
                    daftar_oli.append([kode_oli, nama_oli, stock_oli, harga_oli, kategori_oli])
                    print(f'Oli {kode_oli} berhasil ditambahkan ke daftar oli')
                    tampilkan_daftar_oli()
                    break  
                elif validasitambah == 'N':
                    print('''
--------------------------
Penambahan oli dibatalkan.
--------------------------
                      ''')
                    break
                else:
                    print('Masukkan Y atau N!')

        except ValueError:
            print('''
----------------------------------------------------------                 
Masukkan variabel yang benar (angka untuk stok dan harga)!
----------------------------------------------------------                
                  ''')


def generate_kode_oli(merk_oli, kategori_oli):
    kode_oli = merk_oli[:3].upper()  
    kode_kategori = kategori_oli[0].upper() + kategori_oli[-1].upper()  
    return kode_oli + kode_kategori



### SUBMENU DELETE
def menghapus_data_oli():  
    tampilkan_daftar_oli()
    if len(daftar_oli) == 0:
        print('''
-----------------------                   
Data tidak tersedia !!!
-----------------------
        ''')
        return
    while True:
        kode_oli = input('Masukkan kode oli yang ingin Anda hapus: ').upper().strip()
        
        for oli in daftar_oli:
            if oli[0] == kode_oli:
                detail_table = PrettyTable()
                detail_table.field_names = ["Kode", "Merk", "Stock", "Harga (Rp)", "Kategori"]
                detail_table.add_row([oli[0], oli[1], oli[2], f"{oli[3]:,}", oli[4]])

                print("\nOli yang ingin Anda hapus:")
                print(detail_table)
                
                while True:  
                    validasi = input('Apakah Anda yakin ingin menghapus data ini? (Y/N): ').upper()
                    if validasi == 'Y':  
                        daftar_oli.remove(oli)
                        print(f'Oli dengan kode "{kode_oli}" berhasil dihapus.')
                        tampilkan_daftar_oli()
                        return
                    elif validasi == 'N':  
                        print('Data batal dihapus.')
                        return
                    else:
                        print('Invalid Input! Masukkan Y atau N.')
                        
        else:
            print(f'''
--------------------------------------
Kode oli "{kode_oli}" tidak ditemukan!
--------------------------------------
            ''')


### SUBMENU UPDATE

def update_stok_oli():
    if len(daftar_oli) == 0:  
        print('''
-----------------------                   
Data tidak tersedia !!!
-----------------------
              ''')
        return  
    else:
        tampilkan_daftar_oli()  
    
        while True:
            kode_oli = input('Masukkan kode oli yang ingin Anda ubah stoknya: ').upper().strip()

            oli_ditemukan = None
            for item in daftar_oli:
                if item[0] == kode_oli:
                    oli_ditemukan = item
                    break  
            if oli_ditemukan is None:
                print(f'''
--------------------------------------
Kode oli "{kode_oli}" tidak ditemukan!
--------------------------------------
                ''')
                continue

            table = PrettyTable()
            table.field_names = ["Kode", "Merk", "Stock", "Harga", "Kategori"]
            table.add_row([
                oli_ditemukan[0],
                oli_ditemukan[1],
                oli_ditemukan[2],
                f"Rp.{oli_ditemukan[3]:,}",
                oli_ditemukan[4]
            ])
            
            print(f'''
Oli yang ingin Anda ubah stoknya adalah:
{table}
            ''')
            
            try:
                stok_baru = int(input("Masukkan stok baru oli: "))
                if stok_baru < 0:
                    print('''
--------------------------------------
Stok baru tidak boleh bernilai negatif!
--------------------------------------
                    ''')
                    continue

                konfirmasi = input("Apakah Anda yakin ingin mengubah stok oli ini? (Y/N): ").upper()
                if konfirmasi == 'Y':
                    oli_ditemukan[2] = stok_baru
                    print(f'''
--------------------------------------
Stok oli berhasil diperbarui!
Kode: {oli_ditemukan[0]} | Stok Baru: {stok_baru}
--------------------------------------
                    ''')
                    tampilkan_daftar_oli()
                    break
                elif konfirmasi == 'N':
                    print("Perubahan stok dibatalkan.")
                    break
                else:
                    print('''
----------------------------------
Input yang Anda masukkan salah !!!
----------------------------------
                        ''')
            except ValueError:
                print('''
-------------------------------------------------
Masukkan angka yang valid untuk stok baru oli!
-------------------------------------------------
                    ''')

def update_harga_oli():
    if len(daftar_oli) == 0:  
        print('''
-----------------------                   
Data tidak tersedia !!!
-----------------------
              ''')
        return  

    else:
        tampilkan_daftar_oli()  
    
        while True:
            kode_oli = input('Masukkan kode oli yang ingin Anda ubah harganya: ').upper().strip()

            oli_ditemukan = None
            for item in daftar_oli:
                if item[0] == kode_oli:
                    oli_ditemukan = item
                    break  
            if oli_ditemukan is None:
                print(f'''
--------------------------------------
Kode oli "{kode_oli}" tidak ditemukan!
--------------------------------------
                ''')
                continue

            table = PrettyTable()
            table.field_names = ["Kode", "Merk", "Stock", "Harga", "Kategori"]
            table.add_row([
                oli_ditemukan[0],
                oli_ditemukan[1],
                oli_ditemukan[2],
                f"Rp.{oli_ditemukan[3]:,}",
                oli_ditemukan[4]
            ])
            
            print(f'''
Oli yang ingin Anda ubah harganya adalah:
{table}
            ''')
            
            try:
                harga_baru = int(input("Masukkan harga baru oli: "))
                if harga_baru <= 0:
                    print('''
--------------------------------------
Harga baru harus lebih besar dari 0!
--------------------------------------
                    ''')
                    continue

                konfirmasi = input("Apakah Anda yakin ingin mengubah harga oli ini? (Y/N): ").upper()
                if konfirmasi == 'Y':
                    oli_ditemukan[3] = harga_baru
                    print(f'''
--------------------------------------
Harga oli berhasil diperbarui!
Kode: {oli_ditemukan[0]} | Harga Baru: Rp.{harga_baru:,}
--------------------------------------
                    ''')
                    tampilkan_daftar_oli()
                    break
                elif konfirmasi == 'N':
                    print("Perubahan harga dibatalkan.")
                    break
                else:
                    print('''
----------------------------------
Input yang Anda masukkan salah !!!
----------------------------------
                        ''')
            except ValueError:
                print('''
-------------------------------------------------
Masukkan angka yang valid untuk harga baru oli!
-------------------------------------------------
                    ''')






### SUBMENU OPTION

def update_data_oli():  
    while True:
        pilihanMenu = input('''
-------------------------------------------
Selamat Datang Admin Toko Oli Motor
                                          
List Menu:
1. Mengubah data stock oli
2. Mengubah data harga oli
3. Keluar ke Menu Utama
                            
Masukkan angka Menu yang ingin dijalankan : ''').strip()
        if pilihanMenu == '1':  
            update_stok_oli()
        elif pilihanMenu == '2':  
            update_harga_oli()
        elif pilihanMenu == '3':  
            break
        else:
            print('Invalid Input !!!')


def submenu_daftar_oli():
    while True:
        pilihanMenu=input('''
-------------------------------------------
Selamat Datang Admin Toko Oli Motor
                                          
List Menu:
1. Menampilkan Semua Daftar Oli
2. Mencari kategori oli
3. Urutkan stok oli
4. Urutkan harga oli
5. Keluar ke Menu Utama
                            
Masukkan angka Menu yang ingin dijalankan :  ''').strip()
        if pilihanMenu=='1': 
            tampilkan_daftar_oli()
        elif pilihanMenu=='2': 
            daftar_detail()
        elif pilihanMenu=='3': 
            urutkan_stok_oli()
        elif pilihanMenu=='4': 
            urutkan_harga_oli()
        elif pilihanMenu =='5': 
            break 
        else:
            print('Invalid Input !!!')

def submenu_tambah_oli():
    while True:
        pilihanMenu=input('''
-------------------------------------------
Selamat Datang Admin Toko Oli Motor
                                          
List Menu:
1. Menambah data oli
2. Kembali ke menu utama

                            
Masukkan angka Menu yang ingin dijalankan :  ''').strip()
        if pilihanMenu=='1':
            menambah_data_oli()
        elif pilihanMenu=='2': 
            break 
        else:
            print('Invalid Input !!!')

def submenu_hapus_oli():
    while True:
        pilihanMenu=input('''
-------------------------------------------
Selamat Datang Admin Toko Oli Motor
                                          
List Menu:
1. Menghapus data oli
2. Kembali ke menu utama

                            
Masukkan angka Menu yang ingin dijalankan :  ''').strip()
        if pilihanMenu=='1': 
            menghapus_data_oli()
        elif pilihanMenu=='2': 
            break 
        else:
            print('Invalid Input !!!')

def main_menu():
    while True:
        pilihanMenu=input('''
-------------------------------------------
Selamat Datang Admin Toko Oli Motor
                          
List Menu:
1. Menampilkan Daftar Oli
2. Menambah Data Oli
3. Menghapus Data Oli
4. Update Data Oli
5. Exit Program
                          
Masukkan angka Menu yang ingin dijalankan : ''').strip()
        if pilihanMenu=='1': 
            submenu_daftar_oli()
        elif pilihanMenu=='2':
            submenu_tambah_oli()
        elif pilihanMenu =='3': 
            submenu_hapus_oli()        
        elif pilihanMenu =='4': 
            update_data_oli()
        elif pilihanMenu =='5': 
            print('Keluar dari Program !!!') 
            break
        else:
            print('Invalid Input !!!')
 

main_menu()
