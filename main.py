from platform import system_alias
from mobil import Mobil
from object.life import Human

import sys

def sayhelo(great):
    print(great)



print(sys.argv[1])

toyota = Mobil("aila", "toyota", 100000000)
toyota.harga = 3000
toyota.info()
print(Human.name)

santi = Human('santi', 30)
print(santi.name)
print(santi.age)
toyota.jumlahStock()
print(toyota.stock)
sayhelo("anjayani")


