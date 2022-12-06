# ucgen sinifi
class ucgen():
    def __init__(self,gen=1,yuk=1):
        self.gen = gen
        self.yuk = yuk

    def alan(self):
        return (self.gen * self.yuk) /2
        

# ucgen 1 nesnesini olusturalim

u1 = ucgen()
u1.gen = float(input('genislik >>'))
u1.yuk = float(input('yukseklik >>'))
print('alan >>' , u1.alan())    