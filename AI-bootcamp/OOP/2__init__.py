# %%   initializer or constructor

# Python'daki __init__ metodu bir sınıfın nesnelerini başlatmak için kullanılır. Aynı zamanda bir kurucu olarak da adlandırılır.
# __init__ bir sınıf türünden nesne yaratıldığında otomatik olarak çağrılan bir metottur.
# Constructor'lar, sınıfın ismiyle aynı adı taşıyan metotlardır ve genellikle sınıfın içinde tanımlanır. 
# Bir sınıf birden fazla constructor'a sahip olabilir ve bu, farklı parametre listeleri ile oluşturma işlemini destekler. Bu durum, aynı sınıftan farklı şekillerde örnekler oluşturmanızı sağlar.


class Animal(object):
    
    name = "dog"
    age = 2
    
    def getAge(self): #metot yarattık  # buradaki self object demek aslında-- object'e ulaşmamı sağlayan şeydi
    
        return self.age
    
a1 = Animal()                 # 1 tane hayvan yarattık
print(a1)

a1_age = a1.getAge()
print("animal age: ", a1_age)

# bu şekilde her defasında düzenleyemeyiz o yüzden initializer kullanmalıyız.   ÖRNEK

class Animal(object):
    
    def __init__(self, name, age): # (name,age) = ("dog", 2)    # attribute'ları burada tanımlıyoruz,  # init metodu, constructur yarattık
       self.name = name           # self.name objenin name'i, buna dışarıdan gelen bir name'i eşitledik
       self.age = age
       
    def getAge(self): #metot yarattık  # buradaki self object demek aslında-- object'e ulaşmamı sağlayan şeydi
       return self.age
   
    def getName(self):
        print(self.name)

a1 = Animal("dog", 2)        # 1 hayvan yarattık
print(a1)               # adresini döndürür

print(a1.age)
print(a1.name)
print(a1.getAge())
print(a1.getName())

a2 = Animal("kedi", 4)       # 2.hayvanı yarattık  -- init ve constructor sayesinde bu şekilde değerler girildi
print(a2)                  # adresini döndürür

print(a2.age)
print(a2.name)
print(a2.getAge())
print(a2.getName())

a3 = Animal("kuş", 6)
print(a3)

print(a3.age)
print(a3.name)
print(a3.getAge())
print(a3.getName())
