class Mobil:
    stock: int = 0 #class variable shared with all class
    #constructor
    def __init__(self, nama: str, merek : str, harga : float):
        self.nama = nama #instance variable unique betwen class
        self.merek = merek
        self.harga = harga
        
    #method
    def info(self):
        print("Nama : ", self.nama, "Merek : ", self.merek, "Harga : ", self.harga)
    
    def jumlah_stock(self):
        print("Stock : ", Mobil.stock)

    def add_stock(self, count: int = 0):
        self.stock += count










car = Mobil('d', 'ds', 32423)
print(car.stock)
car.add_stock(31)

car_b = Mobil('ds', 'dsad', 432432)
print(car.stock)




l = [ 'even' if x % 2 == 0 else 'odd' for x in range(5)] #list comperhension
print(l)