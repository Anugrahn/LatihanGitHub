# variabel 

name = 'uga' #string
tanggal_lahir = 9 #integer
married = False # Boolean
berat_badan = 50.5 # float

# Ini adalah fungsi untuk mencetak atau memunculkan apapun yang dimasukan kedalam fungsi print
# print(married)
# print(type(married))
# print(type(name))
# print(type(tanggal_lahir))
# print(type(berat_badan))

# Operasi matematika 
# -, +, *, /, % 

# 6 pangkat 2 

angka_1 = 5
angka_2 = 6
angka_3 = '10'
angka_4 = '5'

x = angka_3 + angka_4

# print(angka_1+angka_3)
# print(angka_3+angka_4)
# print(type(x))
# print(angka_1 - angka_2)

# # integer 
# print('Hasil integer')
# print(angka_1+int(angka_3))
# # string
# print('Hasil string')
# print(str(angka_1)+angka_3)

# perkalian 
# print(angka_1*angka_3)
# print(angka_1*angka_2)

# pembagian 
# print(angka_2/angka_1)

# modulus (sisa hasil bagi dari pembagian tersebut)
# print(angka_2%angka_1)

# Input 
# name = input('Masukan Nama Anda : ')
# age = input('Masukan umur Anda : ')
# jenisKelamin = input('Laki-laki/Perempuan : ')

# print('Nama Saya ' + name +', ' + ' umur saya ' + age + ' tahun, ' + 'dan saya ' + jenisKelamin)
# print(f'Nama saya {name}, umur saya {age} tahun, dan saya adalah {jenisKelamin}')
# print('Nama saya {}, umur saya {} tahun, dan saya adalah {}'.format(name,age,jenisKelamin))


# Hasil print dari input akan seperti ini 
## Nama saya "input nama ", umur saya "input umur", dan saya "input jenis kelamin"

# Name : Lingard 
# Age : 22 tahun 
# Sex : Men
# Position : LMF
# Overall : 67

# name = input('Input your Name : ')
# age = input('Input your age : ')
# sex = input('Input your sex : ')
# position = input('Input your position : ')
# overall = input('Input your over all: ')

# print('Name : ' + name)
# print('Age : ' + age)
# print('Sex : ' + sex)
# print('Position : ' + position)
# print('Overall : ' + overall)

# Function Math in Python
# ceil, pow, floor, sqrt, round

# import math

# # pembulatan keatas untuk angka desimal 
# x = 5.3
# print('Function Ceil from Math')
# print(math.ceil(x))
# # pembulatan kebawah untuk angka desimal
# x = 5.7
# print('Function Floor from Math')
# print(math.floor(x))

# # pemangkatan angka 
# x = 6
# print('Function Pow from Math')
# print(math.pow(7,2))

# # operasi akar di matematika
# x = 49
# print('Function Sqrt from Math')
# print(math.sqrt(x))

# # Function Round (pembulatan untuk angka desimal)
# ## untuk desimal 1-4 dibulatkan ke bawah 
# ## untuk desimal 6-9 dibulatkan ke atas
# y = 5.4
# z = 5.6
# print('')
# print('Pembulatan Ke bawah')
# print(round(y))
# print('Pembulatan Ke atas')
# print(round(z))

# Strings 
# nama = 'marion jola'

# #Hitung karakter termasuk spasi 
# print(len(nama))
# # lower case untuk string
# print(nama.lower())
# # upper case untuk string
# print(nama.upper())
# # Capitalize (huruf depannya saja yang besar)
# print(nama.capitalize())

# Split fucntion untuk membagi string menjadi sebuah list 
## In case split berdasarkan spasi dari string nama
# print(nama.split(' '))

# print(len(nama))
## 10

## speed
## efektivitas 
## maintainability

# nama = 'marion jola'
# akan menjadi sebuah list 
# list_nama = nama.split(' ')
# nama_bersatu = list_nama[0] + list_nama[1]
# print(len(nama_bersatu))

# print(len(nama.split(' ')[0] + nama.split(' ')[1]))

# Strings Indexing 
# name = 'anugrah!anugrah#nurhamid' 
# print(name[8:])
# print(name[7])
# print(name[8:15])
# print(name[:15])
# print(name.split('!'))

# String quotes 
# singleQuotes = 'ini adalah single quotes'
# doubleQuotes = "ini adalah double quotes"
# combineQuotes = "Let's go to the jungle"

# print(singleQuotes)
# print(doubleQuotes)
# print(combineQuotes)

# a = 6
# b = 5 

# # Ketika di print a nya jadi 5 dan b 6 (swipe)
# # Variabel temporary 
# # operasi matematika dulu 

# a,b = b,a 

# print(a)
# print(b)

# Input number with arit opr. 
# angka_1 = input('Masukan angka pertama : ')
# angka_2 = input('Masukan angka kedua : ')
# pertambahan  = int(angka_1) + int(angka_2)
# pengurangan  = int(angka_1) - int(angka_2)
# pembagian  = int(angka_1) / int(angka_2)
# modulus  = int(angka_1) % int(angka_2)

# print(f'Penjumlahan antara angka pertama dan angka kedua adalah {pertambahan}')
# print(f'Pengurangan antara angka pertama dan angka kedua adalah {pengurangan}')
# print(f'Pembagian antara angka pertama dan angka kedua adalah {pembagian}')

# Soal no 1 
# x = 4
# y = 3
# z = 2
# w = ((x+y*z)/(x*y))**z
# print(round(w,2))

# # Soal no 2 
# angka = int(input('Silahkan masukan angka berapapun : '))
# print('Kuadrat dari ' + str(angka) + ' = ' + str(angka**2))

# # Soal no 3 
# ## total 485 hari dijadikan satu persatu ke tahun, ke bulan, ke minggu, ke hari 
# import math

# total_hari  = int(input('Masukan Jumlah hari  : '))
# tahun = str(math.floor(total_hari / 360))
# bulan =  str(math.floor((total_hari % 360)/30))
# minggu =  str(math.floor(((total_hari % 360) % 30 )/7))
# hari = str((math.floor(total_hari % 360) % 30) % 7)

# print()

# print(f'Hasil nya adalah {tahun} tahun, {bulan} bulan, {minggu} minggu, {hari} hari')
## 1 tahun .. bulan .. minggu dan .. hari

num = [5,6,7,8,9]

print(num[::-1])
print(num[::-2])
print(num[::-3])
print(num[::-4])


x = {
    'uga' : 1,
    'nono' :2 ,
    'kharis' : 3
}

y = {
    'uga' : 1,
    'nono' :2 ,
    'kharis' : 3
}

z = {
    'uga' : 1,
    'nono' :2 ,
    'kharis' : 3
}
