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

## Looping with for 
# range(start,stop,step)
# print(list(range(1,5)))
# print(list(range(1,6,2)))
# print(list(range(6,-2,-1)))
# print(list(range(5)))

# list, numpy --> array
# list_angka = list(range(1,10,2))
# # mau ambil angka 5 di list angka
# ## Indexing akan dimulai dari 0 
# print(list_angka)
# print(list_angka[2])

list_makanan = ['ice cream', 'ayam', 'tahu', 'tempe', 'timbel']
list_angka = list(range(5))
# print(list_angka)

# for item in list_angka:
#     print(item) 

# for makanan in list_makanan :
#     print(makanan)

# for item in list(range(1,11)) :
#     print('Nomor urut ' + str(item))

# out = ''
# for i in list(range(5)):
#     out += '*' + '\n'
# print(out) 

# # Nested Loop
# for i in range(5):
#     for j in range(5):
#         print(j)

# * * * * *
# * * * * 
# * * * 
# * * 
# * 

# variabel temp
out = ''
for item in range(5,0,-1):
    for j in range(0,item):
        out += ' * '
    out += '\n'
print(out)

# 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1
# 2 2 2 2 2 2 2 
# 3 3 3 3 3 3 3 
# 4 4 4 4 4 4 4

x = list(range(8))

z = ''
for i in x:
    for j in range(8):
        z += str(i)
    z += '\n'
print (z)

# out = ''
# for i in range(5, 0, -1):
#     if (i > 1):
#         for j in range (0, i):
#             out += ' * '
#         out += '\n'
#     elif i == 1:
#         for k in range (0,5):
#             for l in range (0,k+1):
#                 out += ' * '
#             if k == 4:
#                 break
#             out += '\n'        
# print (out) 

# Aplikasi Membuat Segitiga 
# Pilih Menu :
# 1) Segitiga siku-siku 
# 2) Segitiga Sama kaki
# 3) Persegi 

ketika pilih 1 
Pilih siku : 1) siku atas 2) siku bawah :

ketika pilih siku bawah 
Mau berapa panjang rowsnya (1-10)

ketika pilih 2
Berapa panjang rows (1-10)

ketika pilih 3
Berapa kali berapa 



#      *
#     * *
#    * * *