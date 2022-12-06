try:
    dosya10 = open('dosya10.txt','w')
    dosya10.write('Python ogrenioyrum')
    dosya10.close()
    dosya10.read()
    print(dosya10)
except Exception as Err:
    print("Hata Olustu", Err)
else:
    print('kod hatasiz calisit')
finally:
    print('islem bitti')