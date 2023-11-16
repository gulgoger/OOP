class Ana_1:
    pass


class Ana_2:
    pass

class Ana_3(Ana_1,Ana_2):
    pass


class Saat:
    def __init__(self, saat, dakika, saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye

    def saati_kur(self, saat, dakika, saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye

    def saat_kac(self):
        return "{0}:{1}:{2}".format(self.__saat,self.__dakika,self.__saniye)


clock = Saat(0, 0, 0)
print(clock.saat_kac())
clock.saati_kur(12, 3,55)
print(clock.saat_kac())


class Takvim(object):
    def __init__(self, d, m,y):
        self.takvim_kur(d,m,y)

    def takvim_kur(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y

    def bugun_ne(self):
        return "{d}:{m}:{y}".format(d= self.d,m=self.m,y=self.y)

print("------- Takvim ------")
takvim = Takvim(6,12,2020)
print(takvim.bugun_ne())
takvim.takvim_kur(23,6,2022)
print(takvim.bugun_ne())

class SaatliTakvim(Saat,Takvim):

    def __init__(self,gun,ay,yil,saat,dakika,saniye):
        Saat.__init__(self,saat,dakika,saniye)
        Takvim.__init__(self,gun,ay,yil)

print("------------ saaatli takvim ------------")
saatli_takvim = SaatliTakvim(27,3,2023,13,34,44)
print(saatli_takvim)
print(saatli_takvim.saat_kac())
print(saatli_takvim.bugun_ne())

















































