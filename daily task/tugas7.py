# Pilih Menu 
# 1) Show Dictionary 
# 2) Add Dictionary 
# 3) Search Dictionary (keys)
# 4) Exit 

firstDictionary = {
}

def menuDictionary(input):
    # key | value 
    print('|   key   |   value   |')
    hasil = '' 
    i = 0
    for key,value in input.items():
        i += 1
        hasil += f'{i}. {key}     {value}\n'
    return hasil 

def showDictionary():
    print(menuDictionary(firstDictionary))

def addDictionary():
    inputDic = int(input('Berapa kali akan memasukan dictionary anda : '))
    for i in range(inputDic):
        print('Pilih tipe dictionary \n1) String \n2) Number')
        pilihDictionary = input('Pilih tipe Nomor : ')
        if pilihDictionary == '1':
            key = input('Key : ')
            value = input('Value : ')
            firstDictionary[key] = value
        elif pilihDictionary == '2':
            key2 = input('Key : ')
            value2 = int(input('Value : '))
            firstDictionary[key2] = value2
        print()

def searchDictionary():
    search = input('Cari keys : ')
    ## Proses untuk filter dari sebuah dictionary 
    filter_dic = filter(lambda item : search.lower() in item.lower(), firstDictionary.keys())
    newDic = {}
    for item in filter_dic :
        newDic[item] = firstDictionary[item]
    print(menuDictionary(newDic))

def outAplikasi():
    print()

# backToMenu = 'y'
# while backToMenu == 'y':
#     print('Pilih Menu \n1) Show Dictionary \n2) Add Dictionary \n3) Search Dictionary \n4) Exit') 
#     pilihMenu = input('Pilih menu nomor  : ')
#     index = int(pilihMenu) - 1
#     menu = [showDictionary,addDictionary,searchDictionary,outAplikasi]
#     menu[index]()
#     if pilihMenu == '4' : 
#         print('Terima kasih telah menggunakan aplikasi sederhana ini!')
#         break
#     backToMenu = input('Kembali ke Menu awal ? (y/n)')
#     print()
#     print('Terima kasih telah menggunakan aplikasi sederhana ini!')

# Lambda 
## versi simpel dari sebuah function 




# search = input('Cari Value : ')

# def filterKeys(item):
#     search.lower()

# list_keys = x.keys()
# filter_dic= filter(lambda item: 'nama' in 'nono' ,list_keys)

x = {
    'uga' : 1,
    'nono' :2
}

list_keys = x.keys()
search = input('Cari Keys : ')
search_lower = search.lower()

filter_dic = filter(lambda item : search_lower in item.lower(), list_keys)

print(list(filter_dic))
# print(x.keys())

# tahun = [1995,2000,2005,2010,2015,2020]

# filter_tahun = filter(lambda years : years % 2 == 0, tahun)

# print(list(filter_tahun))

## Coba buat duplikasi function filter
### duplicateFilter(function,list/tuple/sets, etc)







# search = input('Cari Value : ')
# ## Proses untuk filter dari sebuah dictionary 
# filter_dic = filter(lambda item : search.lower() in item.lower(), firstDictionary.value())
# newDic = {}
# for item in filter_dic :
#     if item  == firstDictionary[item]
#     newDic[item] = firstDictionary[item]
# print(menuDictionary(newDic))
# x['dani'] = 3
# print(x)







