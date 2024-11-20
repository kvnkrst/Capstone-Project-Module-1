listKaryawan = [
    {
        'nama': 'Budi',
        'umur': '27'
    },
    {
        'nama': 'Mawar',
        'umur': '27'
    }
]

#READ MENU
#menampilkan read menu
#1. menampilkan seluruh data karyawan
#2. mencari data dan profil karyawan
#3. menampilkan jumlah karyawan
#4. kembali ke menu utama
#notifikasi bahwa masukkan yang dimasukkan pengguna tidak valid
def readMenu():
    while True:
        try:
            pilihanReadMenu = int(input('''
                1. menampilkan seluruh data karyawan
                2. mencari data dan profil karyawan
                3. menampilkan jumlah karyawan
                4. kembali ke menu utama
                Masukkan pilihan anda:'''
            ))
            if pilihanReadMenu == 1:
                menampilkanSeluruhData()
            elif pilihanReadMenu == 2:
                mencariData()
            elif pilihanReadMenu == 3:
                menampilkanJumlahData()
            elif pilihanReadMenu == 4:
                return
        except ValueError:
            print("Input anda tidak valid")

def menampilkanSeluruhData():
    print('Daftar Karyawan\n')
    print('Index\t| Nama  \t| Umur')
    for i in range(len(listKaryawan)) :
        print('{}\t| {}  \t| {}'.format(i,listKaryawan[i]['nama'],listKaryawan[i]['umur']))

def mencariData():
    #while True:
        try:
            menampilkanSeluruhData()
            dataYangDicari = input('''
                Masukkan nama atau indeks yang dicari:'''
            )

            if dataYangDicari.isdigit(): #isinstance(dataYangDicari, int):
                found = False
                dataYangDicari = int(dataYangDicari)
                if 0 <= dataYangDicari < len(listKaryawan):
                    print(f"Data ditemukan: Index: {dataYangDicari} Nama: {listKaryawan[dataYangDicari]['nama']}, Umur: {listKaryawan[dataYangDicari]['umur']}")
                    found = True
                if not found: #else:
                    print("Index tidak ditemukan dalam list")
            elif isinstance(dataYangDicari, str):
                found = False
                for i, karyawan in enumerate(listKaryawan):
                    if dataYangDicari.lower() == karyawan['nama'].lower():
                        print(f"Data ditemukan: {i} Nama: {karyawan['nama']} Umur: {karyawan['umur']}")
                        found = True
                if not found:
                    print("nama tidak ditemukan dalam list")
            else:
                print("Input anda tidak valid")
        except ValueError:
            print("Input anda tidak valid")
                
def menampilkanJumlahData():
    print(len(listKaryawan))


#CREATE MENU
#menampilkan create menu
#1. menambahkan data karyawan baru
#2. kembali ke menu utama
#notifikasi bahwa masukkan yang dimasukkan pengguna tidak valid
def createMenu():
    while True:
        try:
            pilihanCreateMenu = int(input('''
                1. menambahkan data karyawan baru
                2. kembali ke menu utama
                Masukkan pilihan anda'''
            ))
            if pilihanCreateMenu == 1:
                menambahData()
            elif pilihanCreateMenu == 2:
                return
        except ValueError:
            print("Input anda tidak valid")

def menambahData():
    #while True:
        print(menampilkanSeluruhData())
        try:
            dataNama = str(input('Masukkan nama karyawan : '))
            #dataUmur = str(input('Masukkan umur karyawan : '))
            if dataNama.isalpha():
                found = False
                for i, karyawan in enumerate(listKaryawan):
                    if dataNama.lower() == karyawan['nama'].lower():
                        print(f"Data sudah ada: Index: {i} Nama: {karyawan['nama']} Umur: {karyawan['umur']}")
                        found = True
                if not found:
                    dataUmur = input('Masukkan umur karyawan : ')
                    if dataUmur == "":
                        dataUmur = 18
                    elif dataUmur.isdigit():
                        dataUmur = int(dataUmur)
                    else:
                        print("Input umur anda tidak valid")
                    if dataUmur is not None:
                        listKaryawan.append({
                            'nama': dataNama,
                            'umur': dataUmur
                        })
                        menampilkanSeluruhData()
                        print("data nama {dataNama} dan umur {dataUmur} telah ditambahkan")
                #else:   
            else:
                print("Input anda tidak valid")
        except ValueError:
            print("Input anda tidak valid")

#UPDATE MENU
#1. mengubah data karyawan
#2. kembali ke menu utama
#notifikasi bahwa masukkan yang dimasukkan pengguna tidak valid
def updateMenu():
    while True:
        try:
            pilihanUpdateMenu = int(input('''
                1. mengubah data karyawan
                2. kembali ke menu utama
                Masukkan pilihan anda:'''
            ))
            if pilihanUpdateMenu == 1:
                mengubahData()
            elif pilihanUpdateMenu == 2:
                return
        except ValueError:
            print("Input anda tidak valid")

def mengubahData():
    try:
        print(menampilkanSeluruhData())
        dataYangInginDiupdate = input('''Masukkan data yang ingin diubah:''')
        if dataYangInginDiupdate.isdigit():
            dataYangInginDiupdate = int(dataYangInginDiupdate)
            if 0 <= dataYangInginDiupdate < len(listKaryawan):
                print(f"Index: {dataYangInginDiupdate} Nama: {listKaryawan[dataYangInginDiupdate]['nama']}, Umur: {listKaryawan[dataYangInginDiupdate]['umur']}")
                dataNamaBaru = input("Masukkan nama baru (tekan Enter jika tidak ingin mengubah nama): ")
                dataUmurBaru = input("Masukkan data umur baru (tekan Enter jika tidak ingin mengubah umur): ")
                if dataNamaBaru:
                    if dataNamaBaru.isalpha():
                    #dataUmurBaru = input("Masukkan data umur baru (tekan Enter jika tidak ingin mengubah umur): ")
                        listKaryawan[dataYangInginDiupdate]['nama'] = dataNamaBaru
                        #listKaryawan[dataYangInginDiupdate]['umur'] = int(dataUmurBaru)
                        #print(f"Data karyawan berhasil diperbarui: {listKaryawan[dataYangInginDiupdate]['nama']}")
                    else:
                        print("Input nama tidak valid. Harap masukkan huruf")
                if dataUmurBaru:
                    if dataUmurBaru.isdigit():
                        listKaryawan[dataYangInginDiupdate]['umur'] = int(dataUmurBaru)
                    else:
                        print("Input umur tidak valid. Harap masukkan angka")
                menampilkanSeluruhData()
                print(f"Data karyawan berhasil diperbarui: Nama {listKaryawan[dataYangInginDiupdate]['nama']} Umur {listKaryawan[dataYangInginDiupdate]['umur']}")
                #else:
                #    print("Input nama tidak valid. Harap masukkan nama yang hanya berisi huruf.")
            else:
                print("Index tidak ditemukan dalam daftar.")
            
        #elif isinstance(dataYangInginDiupdate, str):
        elif dataYangInginDiupdate.isalpha():
            found = False
            for i, karyawan in enumerate(listKaryawan):
                if dataYangInginDiupdate.lower() == karyawan['nama'].lower():
                    print(f"{i} Nama: {karyawan['nama']} Umur: {karyawan['umur']}")
                    found = True
                    dataNamaBaru = input("Masukkan nama baru (tekan Enter jika tidak ingin mengubah nama): ")
                    dataUmurBaru = input("Masukkan umur baru (tekan Enter jika tidak ingin mengubah umur): ")
                    if dataNamaBaru:
                        if dataNamaBaru.isalpha():
                            #dataUmurBaru = input("Masukkan data umur baru (tekan Enter jika tidak ingin mengubah umur): ")
                            listKaryawan[dataYangInginDiupdate]['nama'] = dataNamaBaru
                            #listKaryawan[dataYangInginDiupdate]['umur'] = int(dataUmurBaru)
                            #print(f"Data karyawan berhasil diperbarui: {listKaryawan[dataYangInginDiupdate]['nama']}")
                        else:
                            print("Input nama tidak valid. Harap masukkan huruf")
                    if dataUmurBaru:
                        if dataUmurBaru.isdigit():
                            listKaryawan[dataYangInginDiupdate]['umur'] = int(dataUmurBaru)
                        else:
                            print("Input umur tidak valid. Harap masukkan angka")
                    menampilkanSeluruhData()
                    print(f"Data karyawan berhasil diperbarui: Nama {listKaryawan[dataYangInginDiupdate]['nama']} Umur {listKaryawan[dataYangInginDiupdate]['umur']}")
            if not found:
                print("nama tidak ditemukan dalam list")
        else:
            print("Input anda tidak valid")
    except:
        print("Input anda tidak valid")

#DELETE MENU
#1. menghapus data dalam list (list karyawan ditampilkan lalu pengguna memasukkan nama atau index yang akan dihapus)
#2. menghapus semua data dalam list
#3. kembali ke menu utama
#notifikasi bahwa masukkan yang dimasukkan pengguna tidak valid
def deleteMenu():
    while True:
        try:
            pilihanDeleteMenu = int(input('''
                1. menghapus sebuah data dalam list
                2. menghapus semua data dalam list
                3. kembali ke menu utama
                Masukkan pilihan anda:'''
            ))
            if pilihanDeleteMenu == 1:
                menghapusData()
            elif pilihanDeleteMenu == 2:
                menghapusSemuaData()
            elif pilihanDeleteMenu == 3:
                return
        except ValueError:
            print("Input anda tidak valid")

def menghapusData():
    try:
        dataYangInginDihapus = input('''Masukkan data yang ingin dihapus:''')
        if dataYangInginDihapus.isdigit():
            dataYangInginDihapus = int(dataYangInginDihapus)
            if 0 <= dataYangInginDihapus < len(listKaryawan):
                print(f"Data yang akan dihapus adalah {dataYangInginDihapus} Nama: {listKaryawan[dataYangInginDihapus]['nama']}, Umur: {listKaryawan[dataYangInginDihapus]['umur']}")
                del listKaryawan[dataYangInginDihapus]
                menampilkanSeluruhData()
                print(f"Data berhasil dihapus.")
            else:
                print("Indeks tidak ditemukan di dalam list")
        elif dataYangInginDihapus.isalpha():
            found = False
            for i, karyawan in enumerate(listKaryawan):
                if dataYangInginDihapus.lower() == karyawan['nama'].lower():
                    print(f"Data yang akan dihapus adalah {i} Nama: {karyawan['nama']} Umur: {karyawan['umur']}")
                    found = True
                    del listKaryawan[dataYangInginDihapus]
                    menampilkanSeluruhData()
                    print(f"Data berhasil dihapus.")
            if not found:
                print("nama tidak ditemukan dalam list")
        else:
            print("Input anda tidak valid")
    except:
        print("Input anda tidak valid")

def menghapusSemuaData():
    listKaryawan.clear()
    menampilkanSeluruhData()
    print("Semua data karyawan telah dihapus")


#menampilkan pilihan menu program data karyawan perusahaan
#menerima masukan pilihan dari pengguna
#percabangan dari setiap pilihan
#notifikasi bahwa masukkan yang dimasukkan pengguna tidak valid

while True:
    try:
        pilihanMenu = int(input('''
            Selamat Datang di Program Data Karyawan Perusahaan
            1. Read menu
            2. Create menu
            3. Update menu
            4. Delete menu
            5. Keluar program
            Masukkan pilihan anda'''
        ))
        if (pilihanMenu == 1):
            readMenu()
        elif (pilihanMenu == 2):
            createMenu()
        elif (pilihanMenu == 3):
            updateMenu()
        elif (pilihanMenu == 4):
            deleteMenu()
        elif (pilihanMenu == 5):
            break
    except ValueError:
        print("Input anda tidak valid")