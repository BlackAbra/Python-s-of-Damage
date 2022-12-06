
# Cok basit bir sinif/ class /kalip
class Daire:
 #   r = 3
    def __init__(self,r):# nesnenin degisken lerini  belirlenmesi // Self kendi classini tanimlar // INIT - IALIZE
            self.r = r # Daire nesnesinin r degiskeni r ' den gelecek
            pass

# yukarida olusturulan siniftan nesne/object olusturalim
d1 = Daire()
print(d1.r)

d2 = Daire()
d2.r=5
print(d2.r)

