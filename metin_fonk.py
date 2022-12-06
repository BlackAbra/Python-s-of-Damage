metin = input('deger giriniz')
print(type(metin))
print(metin.capitalize())
print(metin)
print(metin.lower())
print(metin.upper())


#deger sayisal mi 

# if metin.isnumeric()==True:
#     print('deger sayisal')
# else :
#     print('deger alfasayiisal ')

if metin.isalpha()==True:
    print('deger alfasayisal')
else :
    print('deger sayiisal ')