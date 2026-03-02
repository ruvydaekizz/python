# CLASS

integer = 33
string = "messi"


# classes----- ortak özelliklere sahip nesnelerin bir arada tutulmasıdır -- Genelde adı büyük harfle başlar

employee1_name = "messi"
employee1_age = 33
employee1_address = "ahsahsahshah"


class Employee:                   
    #attribute /nitelikler(özellikler- yaşı, adresi, isim vs) olacak içerisinde
    #behaviour (davranışları --  pass verebilmesi)
    pass


employee1 = Employee()       # bu şekilde yaratılır


# Nitelikler/ Attributes

class Footboller:
    
    football_club = "barcelona" 
    age = 30
    
f1 = Footboller()                 # 1 tane futbolcu yarattık
print(f1)
print(f1.age)                           
print(f1.football_club)           # yarattığımız futbolcunun 2 farklı attribute'ünü ekrana yazdırdık

f1.football_club = "real madrid"    # bu şekilde yeni değer ataması yaptık
print(f1.football_club)            # çalıştırırsak real madrid olarak değiştiğini görebiliriz. BU DOĞRU BİR KULLANIM DEĞİL



# Metotlar-- Hem classlar içerisinde olabiliyor hemde classlar dışındada kullanabiliriz

class Square(object):           #metot yazıyoruz- object--class içerisinde yaratmış olduğumuz metotları, variableları attributeleri tutan/ifade eden yapıdır
    
    edge = 5     # kenarı metre cinsinden
    area = 0     # burada area çağırırsak aşağıda onu da self.area şekilde çağırmalıyız
    
    #karenin alanını hesaplamak için metot yazacağız
    def area1(self):            # burada edge görebilmesi için self yazısı yazıyoruz-- self objecti ifade ediyor
       self.area = self.edge*self.edge     # 5 * 5 ----- çağırırken de self.edge yazmalıyız
       print("Area: ", self.area)
       
       
####################

s1 = Square()     # 1 tane kare yaratıyoruz
print(s1)
print(s1.edge)    # çıktısı 5 olur

print(s1.area)      # çıktısı bize area variable'ın yarattığı yeri dööndürür

print(s1.area1())     # çıktısı Area: 25 olur


# •karenin bir kenarının uzunluğunu 7 yaptık daha sonra alanını hesaplayalım
s1.edge = 7  
s1.area1()               # burada hata alırız



# methods vs. functions   --- NOTE: methodlar classlar içerisinde,functions classlar dışında kullanılabiliyor

class Emp(object):
    
    age = 25        # attribute 
    salary = 1000   # attribute--- $ olarak
        
    # metot yazalım ---- class içerinde yazmam gereken bir modüldür
    def ageSalaryRatio(self):       # self ifadesi burada class'ı ifade eder
        a = self.age / self.salary
        print("METHOD: ", a)

e1 = Emp()    # 1 tane işçi yarattık
e1.ageSalaryRatio()   # oranını versin -- METODU KULLANMAK İÇİN BU ŞEKİLDE ÇAĞIRIRIZ

#----------------------------------------------------------------------------------

# bir fonksiyon yazalım
def ageSalaryRatio(age, salary):       # fonksiyonları class dışında tanımlarız -- fonksiyonun class'la hiçbir alakası yok demektir
    b = age / salary
    print("FUNCTİON: ", b)
    
ageSalaryRatio(30, 3000)   #FONKSİYONU BU ŞEKİLDE ÇAĞIRIRIZ 

#----------------------------------------------------------------------------------
# Örn: 

def findArea(a, b):        # a = pi , b = r = 5
    area = a * b ** 2
    print("ALAN: ", area)
    return area              # findArea fonksiyonunun sonucunda çıkan değeri bana döndürecek- dışarıdan ulaşabileceğim


pi = 3.14
r = 5

findArea(pi, r)

findArea(pi, 10)     # başka bir dairenin alanının bulduk

# şimdi bu iki sonucu toplayalım

result1 = findArea(pi, r)
result2 = findArea(pi, 10) 

print(result1)             # return kullanınca dışarıdan erişebildim
print(result2)

print("Toplam Alan:", result1 + result2)



# initializer or constructor

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