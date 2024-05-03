
from python.human import human


fiyat=100
indirim=20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def SayHello(name):
    print(f"merhaba {name}")

calculate ()    
calculateWithParams(50,100)
calculateWithParams(100,30)
SayHello("SALİM")
SayHello("ERLİK")
SayHello("BÖRÜ")


def calculateAndReturn(price,discount):
    return price-discount

yeniFiyat= calculateAndReturn(200, 50)

print(yeniFiyat)

def calculatePrice(price, discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("++++++++++++++++++++++++")
fonk1=calculatePrice(100,50)
fonk2=calculatePriceAndReturn(300,100)
print(f"42.satır: {fonk1}")
print(f"43.satır: {fonk2}" )  
print("++++++++++++++++++++++")

####classs####
#paket yönetimi
#self => this
# instance=>örnek
human1=human("erlik")  
human1.talk("Merhaba")
human1.walk()
print(human1)

human2=human("bilge")
human2.talk("Merhaba")
human2.walk()
print(human2)







