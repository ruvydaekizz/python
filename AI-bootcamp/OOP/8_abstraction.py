# parent class-- superclass
# child class -- subclass

# abstract classlar -- subclasslar için şablon görevi görürler ve kullanılacak ortak fonk. kendi içlerinde tutarlar
# yani superclass subclass için gerekli olan fonk. bir şablon niteliğinde kendi içinde barındırır

from abc import ABC, abstractmethod      # abc = abstract basic class


class Animal(ABC):    #superclass  - abstract class'ım hiçbir şekilde instanchite edilemez. bunun anlamı ben Animal class'ından hiçbir şekilde obje yaratamam
     @abstractmethod       # animal class bir abstract class olmuş oluyor
     def walk(self): pass
 
     @abstractmethod 
     def run(self): pass 

class Bird(Animal):    #Animal'ın subclass'ı
    pass

a = Animal()   # normalde bir obje yaratacaktık-- - abstract class'ım hiçbir şekilde instanchite edilemez. bunun anlamı ben Animal class'ından hiçbir şekilde obje yaratamam
#bunu düzeltmemiz lazım-- abs kütüphanesini import edeceğiz
# 1.şart-- bu obje yaratılmaz hata alırız. Animal abstarct methodu old. için biz bunu instanchite edemedik
# Animal ile ilgili obje yaratamadık der. Bunu sileriz 

# -----------------------------------------------
# 2.şart -- abstract class'ta kullanılan herhangi bir method benim subclass'ım olan bir yerde kullanılmak zorundadır
from abc import ABC, abstractmethod      # abc = abstract basic class


class Animal(ABC):    #superclass  - abstract class'ım hiçbir şekilde instanchite edilemez. bunun anlamı ben Animal class'ından hiçbir şekilde obje yaratamam
     @abstractmethod       # animal class bir abstract class olmuş oluyor
     def walk(self): pass
 
     @abstractmethod 
     def run(self): pass 


class Bird(Animal):
    def __init__(self): 
        print("bird")
        
    def walk(self):      # bu özellikleri de sonradan ekledik
        print("walk")
 
    def run(self):       # bu özellikleri de sonradan ekledik
        print("run")

        
b1 = Bird() # bir hata aldık. sebbei senin subclass'ın superclass'ın özelliklerini aldığı için bunların ikisini de kullanmak zorundasın diyor
            # çünkü abstract method diyoruz biz bunlara --
            # tekrardan çalıştırdık hatalar düzeldi
            
        
#NOTE: 1.şart--- abstract class'ım(parent classım) hiçbir şekilde obje yaratmayacak -- a = Animal()    bu şekilde
     # 2.sat --- Animal class(superclassta) kullandığım metotları subclass'ta da kullanmak zorundayız
     # 3.şart --- ben run'ı abstractmethod olmaktan çıkarırsam subclass'ta run'ı kullanmak zorunda değilim. 1 tane abstarcted method olması da yeterlidir







 