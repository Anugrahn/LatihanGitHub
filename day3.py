# Soal nomer 1
# import math 
# input_number  = int(input('Masukan angka : '))
# print(input_number % 100 * 100 + input_number // 100)

# Soal Nomer 2
# from math import pi
# # pi * r2
# r = float(input("Input the radius of the circle : "))
# formula = pi * r**2
# print("The area of the circle with radius " + str(r) + ' is ' + str(formula))

# # Soal Nomer 3 
# x = int(input("Input first number (2 digit): "))
# y = int(input("Input second number (2 digit): "))

# a = x // 10 # ambil angka awal di 2 angka pertama 
# b = x % 10 # ambil angka akhir di 2 angka pertama
# c = y // 10 # ambil angka awal di 2 angka kedua 
# d = y % 10 # ambil angka akhir di 2 angka kedua

# print(a*1000 + c*100 + b * 10 + d)

# # Soal Nomer 4 
# input_kalimat = input("Input your sentence : ")
# replace = input('remove word: ')
# print(input_kalimat.replace(replace,""))

# # Soal nomer 5 
# input_kalimat = input("Input your sentence : ")
# list_kata = input_kalimat.split()
# print( list_kata[1] + " " + list_kata[0])

# Assignment Operator 
# Logical Operator 
# Comparasion Operator 
# If Else (Conditional Expression)

# Assignment Operator
# *=, /=, +=, -=, %=

# Example Assgn Oprt.
# a = 8
# a -= 4
# a += 10
# a /= 7
# a *= 2
# a %= 2

# nama = "lingard"
# nama += " Wayne"

# print(nama)

# Comparasion Operator (akan menghasilkan nilai True atau False)
## == (punya nilai yg sama & type data sama)
## > (lebih dari)
## < (kurang dari)
## >= (lebih besar sama dengan)
## <= (kurang dari sama dengan)
## != (tidak sama dengan)

a = 7
b = 'wayne'
c = '8'

# # print(a == b)
# print(a > int(c))
# print(a >= int(c))
# print(a < int(c))
# print(a <= int(c))

# Logical Operators
## and (both of them, if both expression true, result True)
## or (if one of them true, result True)
## not (reverse sebuah boole True/False)
## not in (not inside in condition)
## in (inside of condition)
 
# print(a == b and int(c) < a)
# print(a == b or int(c) > a)
# print(a == b and int(c) > a or int(c) < a)

# a = 7
# b = [8,7,8,8] 

# print(a in b)

# Conditional Expression (If, Else, Else if)
## ketika di execute biasanya ada sebuah conditional statement

# kerangka Conditional Expression
# if (condition A) :
#     Syntaxx
# else if conditon B :
#     syntaxx
# else :
#     syntax 

# if (condition A) :
#     if condition :
#         if condition :
#             if condition :
#     else :

# else if conditon B :
#     syntaxx
# else :
#     syntax

# Membuat 2 kondisi 
# a = 50 

# if a > 50 :
#     print('Good')
# else : 
#     print('Bad')

# a = 70 
# # lulus harus diatas 70
# if a >= 70 :
#     print('Lulus')
# # tidak lulus nilainya dibawah 70
# elif a < 70 :
#     print('Tidak Lulus')
# # selain 2 kondisi di atas
# else :
#     print('Not define')

# inputannya, input angka pertama  & angka 2 
## Pilih operasi +,- ,/ ,% ,* 

# angka1 = float(input ('Masukan Angka Pertama = '))
# angka2 = float(input('Masukan Angka Kedua = '))
# Ops = input('Pilih operator + , - , / , * % : ') ## *

# if (Ops == '+') :
#     print('Hasil pertambahannya adalah ' + str(angka1 + angka2))
# elif (Ops == '-') : 
#     print('Hasil pengurangannya adalah ' + str(angka1 - angka2))
# elif (Ops == '/') : 
#     print('Hasil pembagian adalah ' + str(angka1 / angka2)) #untuk pembagian spasi harus di perhatikan 
# elif (Ops == '*') : 
#     print('Hasil perkaliannya adalah ' + str(angka1 * angka2))
# elif (Ops == '%') : 
#     print('Hasil modulus adalah ' + str(angka1 * angka2))
# else :
#     print('Operation not define')

# # Soal Slide 1 
# angka = input('Masukan angka : ')

# if angka.isdigit() == True:
#     if int(angka) % 2  == 0 : 
#         print(f'Angka {angka} tergolong bilangan Genap!')
#     elif int(angka) % 2 != 0 : 
#         print(f'Angka {angka} tergolong bilangan Ganjil!')      
# else:
#     print('Tolong masukan Angka')

# if int(angka) % 2  == 0 : 
#     print(f'Angka {angka} tergolong bilangan Genap!')
# else : 
#     print(f'Angka {angka} tergolong bilangan Ganjil!')

# massa = int(input( 'Masukan Massa Badan (kg) : '))
# tinggi = int(input ( 'Masukan Tinggi Badan (cm) : '))/100
# imt = round(massa / (tinggi * tinggi),2)
# massa_tinggi = 'Massa ' + str(massa) + ' kg & ' + 'Tinggi ' + str(tinggi) + ' m'
# hasil = 'imt anda adalah ' + str(imt) + ' Berat Badan '

# if (imt < 18.5) :
#     hasil += 'Kurang' # print(imt anda adalah + str(imt) + Berat badan + Kurang)
# elif (18.5 <= imt < 25 ) :
#     hasil += 'Ideal'
# elif (25 <= imt < 30 ) :
#     hasil += 'Berlebih'
# elif (30 <= imt < 39.9 ) :
#     hasil += 'Sangat Berlebih'
# elif (imt >= 39.9 ) :
#     hasil += 'Obesitas'
# print(massa_tinggi)
# print(hasil)

# Looping 
## While Loop 
## For Loop
### while - > Always execute when the condition or statement true
### Dont forget to give an exit way 
# List, Array,

# angka = 0

# while angka <= 10 :
#     print(angka)
#     angka += 2

menu = input('Pilih Menu \n 1.Belanja \n 2.Belajar \n 3.Exit \n Pilih Menu nomor : ')
if(menu.isdigit()==True):
    if(int(menu)>0 and int(menu)<=3):
        check=True
    else:
        print('input salah, masukan pilihan 1-3')
        print('-----------------------------------')
else:
    print('input salah, masukan pilihan 1-3')   
    print('-----------------------------------')

menu = input('Pilih Menu yang anda inginkan \n 1.Home \n 2. About \n 3. Exit \n Pilih Menu Nomor : ')
if (int(menu) >= 0 or int(menu) <=3 ):
    print(True)
else :
    print('Input hanya angka 1 sampai dengan angka 3')








