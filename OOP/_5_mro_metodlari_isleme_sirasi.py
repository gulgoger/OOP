"""
Çok seviyeli kalıtım

mro: method resolution order
"""

class AnneAnne(object):
    pass

class Anne(AnneAnne):
    pass

class Cocuk(Anne):
    pass

class KumSaati(object):
    def __init__(self):
        self.kum_saati_baslasin()

    def kum_saati_baslasin(self):
        print("Kum Saaati başladı")


class Saat(KumSaati):
    def __init__(self, saat, dakika, saniye):
        super().__init__()
        self.saati_kur(saat,dakika,saniye)

    def saati_kur(self, saat, dakika, saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye

    def saat_kac(self):
        return "{0}:{1}:{2}".format(self.__saat,self.__dakika,self.__saniye)


class Takvim(object):
    def __init__(self, d, m,y):
        self.takvim_kur(d,m,y)

    def takvim_kur(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y

    def bugun_ne(self):
        return "{d}:{m}:{y}".format(d= self.d,m=self.m,y=self.y)


class SaatliTakvim(Saat,Takvim):
    def __init__(self,gun, ay,yil, saat, dakika,saniye):
        Saat.__init__(self,saat,dakika,saniye)
        Takvim.__init__(self,gun,ay,yil)

saatli_takvim = SaatliTakvim(12,2,2020,13,24,45)
saatli_takvim.kum_saati_baslasin()


#class'ların mro
for m in SaatliTakvim.__mro__:
    print(m)




















































































