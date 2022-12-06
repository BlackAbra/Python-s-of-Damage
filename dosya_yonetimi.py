'''
# Dosya yonetimi 
import os
print('OS turu',os.name)
print('aktif dizin',os.getcwd())

# Dizin listesi 

print('directory')
#mevcyt_dizin = os.getcwd()
for i in os.listdir(os.getcwd()):
    print(i)
'''
import os 
# dizin / klasor olustur
# os.mkdir('dizin1')
# # dizin silmek icin 
# os.rmdir('dizin1')
# # dosya adi degistir
# os.rename('ekle.py','ekle2.pide')
# # dosya silme
#os.remove('dosya_sil.py')
os.system('notepad.exe')