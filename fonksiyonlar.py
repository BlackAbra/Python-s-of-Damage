# # Fonksiyon olustur
''''
def selam():
    print('hi')
    pass

selam()

#Fonksiyonun calistirilmasi

selam()

tek parametreli  Kare  Fonksiyonu

def sqr(x):
    print("karesi = ", x*x)


sqr(4)
sqr(3.14)

 
def kare(y):
    return y * y

print(kare(5))    

iki paramaetreli fonksiyon 



def topla(a,b):
    return a+b

x = 6
y = 4

print(topla(x,y))




#  ekrandan alinan iki sayinin carpimi

def carp(x1,x2):
    return x1 * x2 

sayi1 = int(input('Sayi 1 >>>>'))
sayi2 = int(input("Sayi 2 >>>>"))

print('Sayilarin carpimi = ',carp(sayi1,sayi2))



def mult(x1,x2=2):
    return x1*x2

s1 = 3
print(mult(s1))


def repeat(loop):
    for  i in range (0,loop):
        print('N',i , 'Merhaba')

loop = int(input("Loop Counter"))

repeat(loop)


#Fonk siyonu tanimla

def yaz(n):
    for i in range (0,n):
        print('Merhaba')

# Fonksiyonu kullanalim

N = int(input("kac defa yazalim   .."))
yaz(N)

x = int(input('kac kere yazalim  .. '))
yaz(x)




def ndefayaz(n):
    x=0
    while x < n:
        print('hi')
        x=x+1


#fonksiyonu cagiralim

z = input('kac kere yaz')
z=int(z)
ndefayaz(z)

'''