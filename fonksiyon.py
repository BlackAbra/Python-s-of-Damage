'''
# # parameteresiz fonk 

# def yaz():
#     print('Fonkisyon Calisti')
# yaz()

# # tek parametereli fonk 

def yaz_metin(metin):
    print(metin)

yaz_metin("btk akademmi")



# iki parameterli fonksiyon 

def yaz(metin,kez=3):
    for i in range(kez):
        print(metin)

yaz('btk',5)


# girilen sayinin karesini dondurren fonk

def kare(x):
    return x*x

print(kare(2))


'''

# iki sayinin carpimini donduren fonk 

def carp(x,y):
    return x*y

print(carp(2,5))