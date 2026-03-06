# WEBSİTE isimli bir Parent Class istiyoruz
# ID ve Email isimli child classlarımız olsun 

class Website:
    "parent class"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def LoginInfo(self):
        print(self.name + " " + self.surname)        
        
p1 = Website("name", "surname")         # p1 insanı yaratıldı
p1.LoginInfo()                            # çıktısı: name surname    olur

        
class Websitesi1(Website):      # Website1 Website'den inherit edecek
    "child class"
    def __init__(self, name, surname, ids):        # parenttan farklı olaraktan buraya bir ID de tanımlayabilirz. name surname almak zorunda
        Website.__init__(self, name, surname)       # Websitesine git name ve surname'i kullanarak __init__ metodunu çağır. self.name ve self.surname metodunu initialize etmiş oluyoruz
                                                      # super().__init__() yerine de bu şekilde de kullanılabilir.
        self.ids = ids                             # ıd tanımladık
        
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)


p2 = Websitesi1("name", "surname", "123")      # p2 insanı yaratıldı
p2.login()                                    # çıktısı: name surname 123 - bu child class'tan gelir

p2.LoginInfo()                           # çıktısı:  name surname    -- bu parent class'tan gelir
p2.name                                   # çıktısı: name --- bu parent class'tan gelir
p2.surname                                # çıktısı: surname ---  bu parent class'tan gelir
                                       

class Websitesi2(Website):      # Website1 Website'den inherit edecek
    "child class"
    def __init__(self, name, surname, email):        # parenttan farklı olaraktan buraya bir email de tanımlayabilirz. name surname almak zorunda 
        Website.__init__(self, name, surname)    #   # Websitesine git name ve surname'i kullanarak __init__ metodunu çağır. self.name ve self.surname metodunu initialize etmiş oluyoruz
                                                      # super().__init__() yerine de bu şekilde de kullanılabilir.
        self.email = email                       # email tanımladık
        
    def login(self):
        print(self.name + " " + self.surname + " " + self.email)

p3 = Websitesi2("name", "surname", "email@email")     # p3 yaratıldı
p3.email                                              # çıktısı: email@email    --- Websitesi2/child classın parametresi
p3.login()                                         # çıktısı: name surname email@email---- Websitesi2/child classın parametresi
p3.LoginInfo()                              #çıktısı:  name surname    -- bu parent class'tan gelir
p3.name                                   # çıktısı: name --- bu parent class'tan gelir
p3.surname                                # çıktısı: surname ---  bu parent class'tan gelir