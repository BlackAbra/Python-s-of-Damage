class Daire:
    def __init__(self,r=1):
        self.r = r
    def alan(self):
        return 3.14 * self.r**2
    def cevre(self):
        return 2 * 3.14 * self.r

# Daire sinifindan d1 nesnesi olusturalim
d1 = Daire(2)
#d1 nesnesinin sinifi
# print('d1',type(d1))
print('d1.r',d1.r)
# print('d1 ram address i ',d1)
print('d1 in alani',d1.alan())


d2 = Daire(5)
print('d2 r si ',d2.r)
print('d2 alani',d2.alan())

d3 = Daire()
d3.r = float(input('r giriniz >>'))
print('d3 alan',d3.alan())


'''

# Daire sinifindan d1 nesnesi olusturalim
d1 = Daire(2)
#d1 nesnesinin sinifi
print('d1',type(d2))
print('d2,r ',d2.r)
print('d1 ram address i ',d2)


a = 2
print('a',type(a))

'''


d4 = Daire()
d4.r = 2.2
print(' d4 alan',d4.alan())
print('d4 cevre',d4.cevre())