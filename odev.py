not1 = input('0 100 arasi sayi  >>> ')
not2 = input('0 100 arasi sayi  >>> ')

if  not1.isnumeric():
    not1 = int(not1)
    not2 = int(not2)
    print('deger sayisal >>>> ')
    if not1 >= 0 and   not1 <= 100 and not2 >= 0 and   not2 <= 100:
        ort = (not1 + not2 / 2) 
        print('not gececrli >>>>> ')
        print('ortalama',ort)
    else:
        print('notlar gecersiz >>>> ')
else:
    print('deger sayisakl degil >>>  ')


