# Aplikasi Perhitungan Matematika

# Aplikasi Membuat Segitiga 
## Kerangka dari pembuatan aplikasi 
# Pilih Menu :
# 1) Segitiga siku-siku 
# 2) Segitiga Sama kaki
# 3) Persegi 

# ketika pilih 1 
# Pilih siku : 1) siku atas 2) siku bawah :

# ketika pilih siku bawah 
# Mau berapa panjang rowsnya (1-10)

# ketika pilih 2
# Berapa panjang rows (1-10)

# ketika pilih 3
# Berapa kali berapa persegi yang diminta 

# back_to_aplikasi = 'y'
# while back_to_aplikasi == 'y':
#     check = False
#     while check == False :
#         # Filter untuk inputan user yang salah 
#         menu = input('Pilih Menu \n 1) Segitiga Siku-siku \n 2. Segitiga Sama Kaki \n 3. Persegi \n Pilih Menu Nomor :')
#         if menu.isalpha() == True or menu.isdecimal() == False :
#             print('Inputan harus berupa integer')
#         else :
#             if (0< int(menu) < 4):
#                 check = True
#             else :
#                 print('Input hanya angka 1-3!')
#     if menu == '1' :
#         check = False
#         while check == False :
#             siku_siku = input("Pilih Segitiga \n 1.Siku atas \n 2.Siku Bawah \n Pilih Segitiga Nomor : ")
#             if menu.isalpha() == True or menu.isdecimal() == False :
#                 print('Inputan harus berupa integer')
#             else :
#                 if (0< int(menu) < 3):
#                     check = True
#                 else :
#                     print('Input hanya angka 1-3!')
#         if siku_siku == '1': 
#             rows = int(input('Berapa panjang rows Siku atas yang diinginkan : '))
#             out = ''
#             for item in range(rows,0,-1): # dia looping range dari 5,4,3,2,1
#                 for j in range(0,item) : # 
#                     out += ' * '
#                 out += '\n'
#             print(out)
#     elif menu == '2' :
#         segitigaSamaKaki = input("Berapa panjang rows (1-10) : ")
#     elif menu == '3' :
#         persegi = input("Berapa panjang sisinya : ")
#     back_to_aplikasi = input("Mau kembali ke menu awal ? (y/n) : ")

## Siku Atas 

# rows = int(input('Berapa panjang rows Siku atas yang diinginkan : '))

# out = ''
# for item in range(rows,0,-1): # dia looping range dari 5,4,3,2,1
#     for j in range(0,item) : # 
#         out += ' * '
#     out += '\n'
# print(out)

# ## another syntax 

# for item in range(rows,0,-1): 
#     print(' * ' * item)

## Siku Bawah 

# rows = int(input('Berapa panjang rows Siku atas yang diinginkan : '))

# out = ''
# for item in range (1,rows+1) : # 1, 5 + 1, 
#     for j in range(0,item):
#         out += ' * ' 
#     out += '\n'
# print(out)

## Segitiga sama kaki 

# rows = int(input('Berapa panjang rows segitiga sama kaki yang diinginkan : '))
# for i in range(rows) :
#     # spasi sebanyak inputan - 1
#     for j in range (rows-1-i):
#         print(end="-")
#     for k in range(i+1):
#         print('*', end="-")
#     for j in range (rows-1):
#         print(end="-")
#     print()

# _ _ * _ _ _  
# _ * _ * _
#
#
#
sisi = int(input('Berapa panjang sisi persegi yang diinginkan : '))
out = ''
for i in range(sisi) : 
    for j in range (sisi) :
        out += ' * '
    out += '\n'
print(out)



##   * 
##  * *
## * * *



# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# # spasi 1 untuk kondisi selain terbanyak 
# # spasi 2 untuk kondisi selanjutnya 

# out = ''
# for item in range(5,0,-1):
#     for item in (0,item):
#         if item <= 5 :
#             out += ' * '
#         elif out 
