# class - Ortak özelliklere sahip nesnelerin bir arada tutulmasıdır
# Genelde ilk harfi büyük harfle başlar.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} model {self.brand} {self.model}"

# Nesne oluşturma
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("BMW", "X5", 2021)

# Metodu çağırma
print(car1.get_info())  # Çıktı: 2022 model Toyota Corolla
print(car2.get_info())  # Çıktı: 2021 model BMW X5




