
#  dongu sayisinin belli olmadigi yerlerde 'While ' kullannilir 

# isim ahmet oluncaya kadar ismi aln
'''

isim = int(input('Isim Girniz'))
while isim != "ahmet":
    isim = int(input('Isim Girniz'))
print('giris basarili')
pass


# Not 100 olmadigi surece not alinsin 

'''

not1 = int(input('not1 giriniz'))
while not1 < 0 or not1 > 100 :
        not1 =int(input('not griniz'))
print('not girisi basarili')