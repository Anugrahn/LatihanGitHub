# Bikin kondisi keluar 
## syntax filter untuk inputan yang dimasukan 
# Pilih Menu 
# 1) Belajar
# 2) Belanja
# 3) Exit

# Syntax filter untuk inputan yang dimasukan 
# if menu yang dinput adalah 1 maka keluar menu.. 
# 1) Hitung luas Trapesium 
# 2) Hitung luas segitiga 

# Syntax filter untuk inputan yang dimasukan 
# if menu belajar yang dipilih adalah 1 maka keluar..
# sisi atas :
# sisi bawah :
# tinggi trapesium : 

# print(Hasil dari luas trapesium adalah..)

# Aplikasi Belanja & Belajar 
## Checking exit way dari aplikasi
Exit  = False 
while Exit == False :
# Checking inputan dari user
    check = False 
    while check == False:
        # Pemilihan menu dan validasi untuk pemilihan user hanya angka 1-3
        menu = input('Pilih Menu \n 1.Belanja \n 2.Belajar \n 3.Exit \n Pilih menu nomor : ')
        # untuk proses validasi hanya string angka yang di inputkan 
        if menu.isdigit() == True :
            # untuk proses filtering hanya angka 1-3
            if int(menu) > 0 and int(menu) <= 3:
                check = True
            else :
                print('Input salah, masukan pilihan 1-3')
                print('---------------------------------')
        else :
            print('Input salah, masukan angka hanya 1-3')
            print('---------------------------------')
    # Proses bila menu 1 yang terpilih 
    if menu == '1':
        # Pemilihan menu belanja dan validasi hanya angka seusai dengan yang di menu.
        check = False 
        while check == False:
            menuBelanja = input('Pilih Makanan \n 1.Ayam Bakar Rp.20,000 \n 2.Ayam Goreng Rp.25,000 \n 3.Ayam Geprek Rp.35,000 \n Pilih makan nomor : ')
            if menuBelanja.isdigit() == True :
                if int(menuBelanja) > 0 and int(menuBelanja)<=3:
                    check = True
                else :
                    print('Inputan salah, hanya pilihan 1-3')
                    print('-------------------------------------')
            else : 
                print('Inputan salah, hanya angka 1-3')
                print('-------------------------------------')
        # Pembuatan variabel harga untuk masing-masing menu belanja yang kita pilih 
        harga = ''
        if menuBelanja =='1' :
            harga = 20000
        elif menuBelanja == '2' :
            harga = 25000
        elif menuBelanja == '3' :
            harga = 35000
        # Input kuantitas untuk pemebelian menu belanja disertai filtering hanya untuk angka lebih dari 0
        check = False
        while check == False :
            quantity = input('Masukan jumlah produk yang akan di beli : ')
            if quantity.isdigit() ==True :
                if int(quantity) > 0 :
                    check = True 
                else :
                    print('Input salah, kuantitas tidak boleh 0')
                    print('-------------------------------------')
            else : 
                print('Input salah, masukan kuantitas hanya dengan angka')
                print('--------------------------------------------------')
        totalHarga = harga * int(quantity)
        print('Pembelian Berhasil! Total Belanjaan anda adalah : ' + 'Rp. ' + str(totalHarga))
        print('------------------------------------------------------------------------')
        # Pertanyaan apakan anda ingin kemabli ke menu awal atau exit dan disertai validasi inputan dari user
        check = False 
        while check == False : 
            ask = input('Pilih menu \n 1.Menu awal \n 2.Exit \n Pilih Nomor : ')
            if (ask.isdigit() == True) :
                if int(ask) > 0 and int(ask) <=2:
                    check = True
                else :
                    print('Input salah, masukan hanya 1 atau 2')
                    print('-------------------------------------')
            else :
                print('Input salah, masukan hanya angka 1 atau 2')
                print('-----------------------------------------')
            if (ask == '2') :
                Exit = True
    elif menu == '2' :
        print('Menu Belajar')
    else :
        Exit = True
print('Terima kasih sudah menggunakan layanan kami')