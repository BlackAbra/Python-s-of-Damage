# n = int(input('sayi gir'))
# s=1
# f=1
# while s<=n:
#     f=f*s
#     s=s+1
# print('sayi ',n,'fak',f)

def fac(n):
    s=1
    f=1
    while (s<=n):
        f = f * s 
        s = s + 1 
    return f

sayi = int(input('sayi'))
print(fac(5))
