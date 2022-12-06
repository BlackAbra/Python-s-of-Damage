try:
    x1 = 2
    x2 = 0
    print(x1/x2)

except: # hata olursa  calisir
    print('sifira bolme hatasi !!!')

else: # hata olmazsa calisir
    print('hata oldu ')

finally: # hata olsa da olmasa da calisir
    print('her durumda calisir ')