class AnaSinif:
    pass

class AltSinif1(AnaSinif):
    pass

class AltSinif2(AnaSinif):
    pass

import math

class Sekil:
    def __init__(self, renk ="kırmızı"):
        self.renk = renk

class Daire(Sekil):
    def __init__(self, yaricap, renk ="mavi"):
        super().__init__(renk = renk)
        self.yaricap = yaricap

    def alan(self):
        return math.pi**self.yaricap**2

class Dikdortgen(Sekil):
    def __init__(self, kisa=1.0, uzun =1.0, renk = "turuncu" ):
        super().__init__(renk=renk)
        self.kisa = kisa
        self.uzun = uzun

    def alan(self):
        return self.kisa* self.uzun

class Kare(Sekil):
    def __init__(self,kenar=1.0,renk ="beyaz"):
        super().__init__(renk=renk)
        self.kenar = kenar

    def alan(self):
        return self.kenar**2

se = Sekil("mor")
print("Sekil nesnesi olan se'nin rengi :", se.renk)

da = Daire(yaricap =5)
print("Daire nesnesi olan da'nin yarıçapı :", da.yaricap)

print("Daire nesnesi olan da'nin rengi :", da.renk)
# daire classının renk özelliği hata verdi AttributeError: 'Daire' object has no attribute 'renk'


dk = Dikdortgen(kisa=2, uzun=8,renk="sarı")
print("Dikdörtgen nesnesi olan dk'nin rengi :", dk.renk)
print("Diksörtgenin alanı: ",dk.alan())


print("Sekil sınıfı, object sınıfının alt sınıfı mı? ",isinstance(se,object))

print("Kare, Sekil'in  alt sınıfı mı?: ",issubclass(Kare,Sekil))




































































