"""
OOP: OBJECT ORİENTED PROGRAMİNG
kod tekrarını önler
"""

#class Penguen:

#    tur = "Kuş"

#    def __int__(self, ad, yas, renk):
#        self.ad = ad
#        self.yas = yas
#        self.renk = renk


#kral = Penguen("Kral Penguen",4, "Turuncu")
#sari_goz = Penguen("Sarı Gözlü Penguen",1, "Kahverengi")

#print("{0}'ın bilimsel türü: {1}".format(kral.ad, kral.__class__.tur)



class Penguen:
    tur = 'Kuş'

    def __init__(self,ad,yas,renk):
        self.ad = ad
        self.yas = yas
        self.renk = renk

    def yuzme(self):
        return f"{self.ad} yüzebilir."

    def sarki_soyle(self, soyleyebilir_mi =False):
        if soyleyebilir_mi:
            return f"{self.ad} şarkı söyleyebilir"
        else:
            return f"{self.ad} şarkı söyleyemez."

    def dans_et(self, dans_edebilir_mi =False):
        if dans_edebilir_mi:
            return f"{self.ad} dans edebilir."
        else:
            return f"{self.ad} dans edemez."

#makaroni = Penguen('Makaroni Pengueni', 8, 'Sarı-Siyah')

#print(makaroni.yuzme())

#print(makaroni.sarki_soyle(soyleyebilir_mi=True))

#print(makaroni.dans_et(False))

neseli_ayaklar = Penguen("Neşeli Ayaklar", 1, "Gri-Papyon")
#print(neseli_ayaklar.yuzme())

#print(neseli_ayaklar.sarki_soyle(False))

#print(neseli_ayaklar.dans_et(True))



class Kus:
    def __init__(self):
        print("Kuş yaratıldı.")

    def kimimBen(self):
        print("Ben bir Kuşum.")

    def ucma(self):
        print("Kuşlar uçabilir.")

    def yuzme(self):
        print("Kuşlar yüzebilir.")

#minik_kus = Kus()
#minik_kus.kimimBen()
#minik_kus.ucma()
#minik_kus.yuzme()


class Baykus(Kus):

    def __init__(self):
        super().__int__()
        print("Baykuş yaratıldı.")

    def kimimBen(self):
        print("Ben bir Baykuşum.")

    def yuzme(self):
        print("Baykuşlar yüzemez.")

    def gece_gorusu(self):
        print("Baykuşun gece görüşü vardır.")

#kucuk_baykus = Baykus()
#kucuk_baykus.kimimBen()
#kucuk_baykus.ucma()
#kucuk_baykus.yuzme()
#kucuk_baykus.gece_gorusu()


"""
ENCAPSULATION _ KAPSÜLLEME _ GİZLEME
"""
class Telefon:

    def __init__(self):
        self.__fiyat = 1000

    def sat(self):
        print("Satış fiyatı: {} TL".format(self.__fiyat))

    def set_fiyat(self, yeni_fiyat):
        if yeni_fiyat <= 0:
            print("Negatif fiyat olamaz.")
        else:
            self.__fiyat = yeni_fiyat

    def get_fiyat(self):
        return self.__fiyat
tel = Telefon()
# AttributeError: 'Telefon' object has no attribute '__fiyat'
# Hata vermesinin nedeni __fiyat private olduğu için
#print(tel.__fiyat)

#tel.sat()

#tel.__fiyat = 5000
#tel.sat()
#print(tel.__fiyat)
#tel.renk = "Siyah"
#print(tel.renk)


tel.set_fiyat(8000)
#tel.sat()

fiyat = tel.get_fiyat()
#print(fiyat)

#tel.set_fiyat(-2000)
#print(tel.get_fiyat())


# ------------- POLYMORPHISM --------------------
"""
Polymorphism :
çok şekillilik
"""

class Kus:
    def __init__(self):
        print("Kuş yaratıldı.")

    def kimimBen(self):
        print("Ben bir Kuşum.")

    def ucma(self):
        print("Kuşlar uçabilir.")

    def yuzme(self):
        print("Kuşlar yüzebilir.")


class Baykus(Kus):

    def __init__(self):
        #super().__int__()
        print("Baykuş yaratıldı.")

    def kimimBen(self):
        print("Ben bir Baykuşum.")

    def yuzme(self):
        print("Baykuşlar yüzemez.")

    def gece_gorusu(self):
        print("Baykuşun gece görüşü vardır.")

class Penguen(Kus):
    def __init__(self):
        #super().__init__()
        print("Penguen yaratıldı.")

    def kimimBen(self):
        print("Ben bir Penguenim.")

    def ucma(self):
        print("Penguenler uçamaz.")


def ucabilir_mi(kus):
    kus.ucma()

kus = Kus()
baykus = Baykus()
penguen = Penguen()

print("---------- uçma testi -----------")

ucabilir_mi(kus)
ucabilir_mi(baykus)
ucabilir_mi(penguen)














