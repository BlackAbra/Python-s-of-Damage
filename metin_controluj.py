not1 = input('0 100 arasi sayi  >>> ')
if  not1.isnumeric():
    not1 = int(not1)
    print('deger sayisal >>>> ')
    if not1 >= 0 and  not1 <= 100:
        print('not gececrli >>>>> ')
    else:
        print('not1 gecersiz >>>> ')
else:
    print('deger sayisakl degil >>>  ')


