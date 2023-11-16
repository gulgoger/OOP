class Nokta:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

n1 = Nokta(2,5)
n2 = Nokta(-1,4)

print("----- overload öncesi -------")
print(n1)
print(n1.__str__())

#print() -> __str__() metodu getirir
# dfault olarak object'en getirir.

class Nokta:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Bu bir noktadır.Koordinatları: {0}x{1}".format(self.x, self.y)


print("----- overload sonrası -------")
n1 = Nokta(2,5)
print(n1)

print(Nokta.__name__)














