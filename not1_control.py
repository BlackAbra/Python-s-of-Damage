not1=input('0 - 100 ')
if not1.isnumeric():
    not1  = int(not1)
    print('sayisal')
    if not1 >= 0 and not1 >= 100:
        print('not 1 gecerli ')
    else:
        print('not 1 gcersiz')
else:
    print('sayisal degil')