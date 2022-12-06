
'''
 # X parametresi ile sadece dosya olustur 
#dosya = open('dosya1.txt','x')
# Yazma macli dosya olustur .
dosya2 = open("dosya2.txt","w") 
# yazilip en osn satira eklenir
dosya3 = open('dosya.txt','a')


#Dosya acip veri yazma (w) / veri ekleme (a)

dosya3 = open('dosya3.txt','w')
metin = 'Merhaba Dosya !!!'
dosya3.write(metin)
dosya3.close()


# dosya okuma 
try:
    dosya4 = open('dosya3.txt','r')
    okunan = dosya4.read()
    dosya4.close()
    print(okunan)
except Exception as err :
    print('hata',err)
else:
    print('kodlar hatasiz calisti ')
finally:
    print('islem bitti ... ')
'''
