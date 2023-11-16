class Araba:
    """
    Bu araba classıdır.
    """

    marka = "BMW"

    def calisma(self):
        print("Bu araba çalışıyor.")

#print(Araba.marka)

"""
dunder(double underscore):
iki alt tire(__) metodlara ve attribute'lara "dunder" adı verilir.
"""
# tanımladığımı araba class'nın docstringine erişmek için
#print(Araba.__doc__)

# calısma metodunun özelliği
#print(Araba.calisma)

# calısma() çağırsak ne olacaktı?
#print(Araba.calisma())
# nesne yaratmadam çağırdığımız için TypeError: calisma() missing 1 required positional argument: 'self'

yeni_araba = Araba()
#print(yeni_araba.marka)

#yeni_araba.calisma()

import math

class Cember:
    def __init__(self, yaricap):
        self.__yaricap = yaricap

    def get_yaricap(self):
        return self.__yaricap

    def set_yaricap(self, yeni_yaricap):
        if yeni_yaricap > 0:
            self.__yaricap = yeni_yaricap
        else:
            print("Yarıçap pozitif olmalı.")

    def cevre(self):
        return math.pi * self.__yaricap**2

#cember_1 = Cember(10)
#print(cember_1.get_yaricap())
#cevre = cember_1.cevre()
#print(cevre)

#print("------- set -------")
#cember_1.set_yaricap(20)
#cevre = cember_1.cevre()
#print(cevre)

class Ogrenci:
    def __init__(self, isim, yas, sinif):
        self.isim = isim
        self.yas = yas
        self.sinif = sinif

ogr = Ogrenci("Cin Ali", 8, "3-A")
print(ogr.isim)
print(ogr.sinif)
print(ogr.yas)

print("------ silme -----")
del ogr.yas
print(ogr.yas)

del ogr
print(ogr.isim)



