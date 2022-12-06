
# # x = int(input('yasinizi girin >>> '))
# # if x < 18 :
# #     print('18 den kucuk uye olamazsin')
# #     print('----------------------------------')
# #     # pass
# # print('\n hosgeldiniz ')

# #  not ort
# # not1= int(input('sayi >>> '))
# # not2 = int(input('sayi >>> '))
# # ort = (not1+not2)/2
# # if ort > 50 :
# #     print("gecti",ort)
# # pass

# #Her iki notta 60 dan buyukse ortalama yaz

# not1= int(input('not 1 >>> '))
# not2 = int(input('not 2 >>> '))
# ort = (not1+not2)/2
# if not1 and not2 > 60 :
#      print("gecti",ort)
# else:
#      print('Vizeye giremez')


# # #if else sorgusu 

# # yas = int(input('yasinizi girniz'))
# # if yas < 18 :
# #     print("Uye olamazsin")
# # else:
# #     print('uye olmazsin')


not1 = int(input('not 1 .>'))
not2 = int(input('not 2 .>'))

if(not1 <0  or not1 > 100) or (not2 <0  or not2 > 100):
    print('Notlar GEcersiz')
else:
    ort = (not1+not2)/2
    if ort < 50:
        print('kaldi')
    elif ort < 70:
        print("orta")
    elif ort < 85:
        print(" iyi")
    else:
        print('pekiyi') 





