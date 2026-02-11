#1
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

specific = Car("Toyota", "Black")

print(specific.brand)
print(specific.color)

#2
class Car:
    def __init__(self, brand, color="White"):
        self.brand = brand
        self.color = color

specific = Car("Inova")

print(specific.brand)
print(specific.color)

#3
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

specific = Car("Toyota", "Black")
specific2 = Car("Avanza", "Yellow")

print(specific.brand)
print(specific.color)
print(specific2.brand, specific2.color)

'''
MyCar = Pascal case, menggunakan huruf kapital di awal kata pada setiap penamaan
ubah_merek = Snake case, menggunakan underscore untuk menggabungkan dua kata
self = Merujuk pada dirinya sendiri, atau objek yang dibuat oleh kita sendiri
class adalah blueprint, object adalah hasil jadi
self.brand, self.color = Atribut
Python sangat sensitif dengan indentasi atau tab
'''