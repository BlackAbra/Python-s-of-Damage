'''
# Liste olusturma 

ls = [1,2,3,4]

print(ls[2])

ls[2] = 9

print(ls[2]) #listenin 2 indisli elemanin ni yaz 
ls[2]=9         #listenin 2 indisli elemaninin degerini 9 yap
print(ls[2])  #listenin 2 indisli elemanini tekrar yaz
print(ls)   # listeyi yaz

#liste elemanlarini yaz

boyut =len(ls)

for i in range (0,boyut):
    print(ls[i])


liste = [1,'elma',2,'portaktal',3,'portaokal',4.4,True]
for i in liste:
      print(type(i))


print(liste[-3:-1])

liste.insert(2,"mandalin")

print(liste)

liste.append("False")

print(liste)

liste.remove('mandalin')

print(liste)

liste.clear()  #liste elemanlarini sil

print(liste)




sayilar = [1,9,3,12,5]
sayilar.sort()
print(sayilar)
sayilar.reverse()
print(sayilar)


sayilar2 = sayilar.copy()
print (sayilar2)
sayilar2.reverse()
print (sayilar2)



#dizi 1 elemanlarinin karesini dizi 2 ye koy
dizi1 = [1,2,3,4,5,7]
dizi2 = []
for eleman in dizi1:
    dizi2.append(eleman  * eleman)
print(dizi2)


# Klavyeden n adet sayi alip bir diziye ekleyin

n = int(input('sayi adeti '))
dizi = []
for i in range (0,n):
    f = int(input('eleman gir .> '))
    dizi.append(f)

print('dizi ekleme sonrasi',dizi)



# range(baslangic , bitis ,artis)
for x in range (5): #0 - 4 arasi sayilarda islem yap 
    print(x)

for x in range (2,7): # 2 - 6 arasi sayilarda islem yap 
    print(x)

for x in range (2,11,2): # 2 - 10  arasi cift sayilarda islem yap 
    print(x)

'''




