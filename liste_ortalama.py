size= int(input('eleman sayisi >>>'))
dizi=[]

# Diziye eleman ekleme 

for i in range(size):
    dizi.append(int(input('sayi >>>')))

#  Dizi Toplami 

toplam = 0
for i in dizi:
    toplam = toplam + i

# Ortalama 

ort = toplam / size
print( 'ortalama >> ',ort)