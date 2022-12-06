
'''

liste1 = [0,1,2,3,4,5]

print('liste uzunlug',len(liste1))
print('2 . elelamn',liste1[2])
print([liste1])
print(liste1[2:5])
print(liste1[2:])
print(liste1[:3])
liste1[2] = 22
print(liste1)


liste1.insert(3,33)
print(liste1)
liste1.append(66)
print(liste1)
liste1.pop()
print(liste1)
liste1.remove(3)
print(liste1)
liste1.clear()
print(liste1)
liste1.sort()
print(liste1)
liste1.reverse()
print(liste1)

toplam = 0
for x in liste1 :
    toplam = toplam + x
print('toplam ',toplam)
'''

leleman_saysis = int(input('eleman saiysi >>  '))

dizi = []

for i in range (leleman_saysis):
    dizi.append(int(input('sayi >>  ')))

toplam = 0
for i in dizi:
    toplam = toplam + i 

ort = toplam / i 
print('ortalama ... ',ort)