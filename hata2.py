try:
    x1 = float(input('sayi 1  >>>'))
    x2 = float(input('sayi 2  >>>'))
    print('sonuc',x1/x2)
except Exception as err:
    print('Hata',err)
else:
    print('kodlar hatasiz calisti')
finally:
    print('kodlar bitti')