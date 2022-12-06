'''
#fonk tanimlama

def  yaz():  #parametresiz fonksiyon
    print('merhaba')

#Fonk kullanma 
yaz()
yaz()


once fonksiyonu tanimla

def xdefayaz(x):  #tek parameterli fonk
    for i in range(x):
        print("Merhaba")

#fonk calistiralim 
a = int(input('kac defa yaz'))

xdefayaz(a)




#ekrandan alinan iki sayinin toplama

def toopla(x,y):
    return x + y


sayi1 = int(input("x i girin  "))
sayi2 = int(input("y i girin  "))

print('sayilarin toplama',toopla(sayi1,sayi2))



def ort(sayi1,sayi2):
    return sayi2 + sayi1 / 2

print(ort(90,90))


#Version2

def orts(a1,a2):
    print('Ortalama v2',a1+a2/2)

orts(2,3)

#Version 3 


def ort(a1,a2):
    print('ortatlama  >> ',(a1+a2)/2)

a1=int(input("sayi 1 >> "))
a2 = int(input("sqyi2 >> "))
ort(a1,a2) 

# 2 sayyidan buyuk olani yazdiran fonk

def buyuk(x,y):
    if x >y :
        return x
    else:
        return y

print(buyuk(4,5))

'''