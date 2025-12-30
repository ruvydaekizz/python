# Inheritance (kalıtım/miras) --- daha önceden yapılmış bir class'ın özelliklerini yada metotlarını, variablellarını
# kullanarak yeni bir class yaratmaktır.

# eğerki yeni yazacağın class'ın özellikleri önceki class'ta bulunuyorsa bunları inheritance/kalıtım yoluyla alıyoruz

# Inheritance'de 2 farklı class yapısı vardır- bunlardan birisi PARENT class, diğeri CHILD class
# CHILD class- PARENT class'ın attributelerini, metotlarını kullanabilen bir alt classtır  -- Parent class'tan türetilmiş class da denir. - istediğin sayıda üretilebilir sınırı yok


#ÖRN:
#PARENT class(ANIMAL isimli) içinde - diyelim ki run metodu, walk metodu olsun (tüm hayvanların ortak özellikleri)
#CHILD class(MONKEY isimli) olsun - diğer hayvalardan ayıran özelliği climb metodu'dur, geri kalan run ve walk metodunu ANIMAL'dan alabilir
#CHILD class(BIRD isimli) olsun - diğer hayvalardan ayıran özelliği fly metodu'dur, geri kalan run ve walk metodunu ANIMAL'dan alabilir


# PARENT class'ımız    ---- superclass
class Animal():
    def __init__(self):
        print("animal is created")
    
    def toString():
        print("animal")
        
    def walk(self):
        print("animal walk")
    
    def run(self):
        print("animal run")

# CHILD class'ımız Monkey    --- subclass
class Monkey(Animal):        # Animal class'ından türeteceğimiz için Animal yazdık -- Monkey Animal'ın bir child'ı oldu
    def __init__(self):
        super().__init__()    # parent class'ın içeriğini chil class'a aktarmamızı sağlıyor--- use init of parent(animal) class
        print("monkey is created")
    
    def toString(self):
        print("monkey")
    
    def climb(self):
        print("monkey can climb")
        
    # walk metodunu- yürüyebiliri parent kısmında tanımladık artık monkey kısmında yazmamıza gerek kalmadı
    

# CHILD class'ımız Bird()    ---   subclass
class Bird(Animal):         # Animal class'ından türeteceğimiz için Animal yazdık -- Bird Animal'ın bir child'ı oldu
    def __init__(self):
        super().__init__()
        print("bird is created")
        
    def fly(self):
        print("bird can fly")
    

# maymun yaratıyoruz
m1 = Monkey()         # maymun 1'i yarattık-- çıktısı   animal is created, monkey is created yazıları ekrana geldi
     
m1.toString()       # çıktısı ---- monkey olur  

# NOTE:
# monkey'in yürüyebilmesi lazım-- monkey class'ında walk metodu yok. -- 
# class Monkey(Animal): bu kısıma class Monkey(object) yazsaydık hata alırdık burada, çünkü walk metodu yok Monkey sınıfı içinde

m1.walk()    # çıktısı : animal walk --- Neden? çünkü class Monkey(Animal): classından bu metodu çağırabildik

m1.climb()    # çıktısı: monkey can climb

print("-----------------------")
# kuş yaratalım
b1 = Bird()      # çıktısı: animal is created , bird is created  olur

b1.walk()       # çıktısı: animal walk --- Neden? çünkü class Monkey(Animal): classından bu metodu çağırabildik

b1.fly()        # çıktısı: bird can fly   yazar.

b1.climb()      # buna erişemez çünkü o monkey'in özelliğidir.  hatası alır:  AttributeError: 'Bird' object has no attribute 'climb'


class Bird(Monkey):         # Monkey class'ından türeteceğimiz için Monkey yazdık -- Bird Monkey'ın bir child'ı oldu
    def __init__(self):
        super().__init__()
        print("bird is created")
        
    def fly(self):
        print("bird can fly")
        
b2 = Bird()

b2.climb()       # çıktısı : monkey can climb  olurdu. 
                 # Saçma oldu ama classların her birini birbirine bağlayabiliriz
