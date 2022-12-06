'''
def  merhabe(n):
    for i in range(n):
        print('merhaba')

x = int(input('kac defa >> '))
merhabe(x)

def cift_sayi_yaz(n):
    for i in range (0,n,2):
        print(i)

        
x = int(input('sayi gir'))
cift_sayi_yaz(x)

# x - y arasi sayilari yaz

def x_y_arasi_yaz(x,y):
    for i in range (x,y+1):
        print(i)


x = int(input('x : '))
y = int(input('y : '))

x_y_arasi_yaz(x,y)

# 1 den n e kadar olan sayilarin toplami 

def n_1_top(n):
    topla = 0
    for i in range(1,n+1):
        topla = topla + i
    return topla
         
n = int(input('  n  '))
print('  bir n arasi topla  ',n_1_top(n))



# n faktoriyel

def fakt(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

n = int(input(' n : '))

print('n!=',fakt(n))

'''

# 
