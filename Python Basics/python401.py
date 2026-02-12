# NESNE YONELIMLI PROGRAMLAMA (Object Oriented Programming)

# Nesne yonelimli programlamanin temelini olusturan yapi siniflardir.

##################################################################################################

# SINIFLARA GIRIS VE SINIF TANIMLAMAK

# Sinif nedir?  - benzer ozellikleri tutan, ortak amac tasiyan, icerisinde metod ve degiskenler olan yapilardir.

class VeriBilimci():
    print("Bu bir siniftir.")

#################################################################################################

# SINIF OZELLIKLERI (Class Attributes)

# burada veri bilimcilere ait olan ortak ozellikleri ve  kisiden kisiye degisen ozellikleri tutmak istiyoruz

class VeriBilimci1():
    bolum = " "                   # sinifin ozellikleri bunlar
    sql = "Evet"
    deneyim_yili = 0
    bildigi_diller = []    


# Siniflarin ozelliklerine erisme --- VeriBilimci1() sinifi icerisindeki bu ozelliklere eriselim

VeriBilimci1().bolum
VeriBilimci1().sql
VeriBilimci1.deneyim_yili      # parantez olmadan da erisilebilir
VeriBilimci1.bildigi_diller


# Siniflarin ozelliklerini disaridan degistirme 
 
VeriBilimci1.sql ="Hayir"           # () 'li yazınca ozelligini degistirmeme izin vermedi. Evet olarak kalmisti cevabı
VeriBilimci1.sql                    # ancak simdi () olmadan yazinca degistirebildim


#################################################################################################

# SINIF ORNEKLENDIRMESI (instantiation)

# ali objesi
ali = VeriBilimci1()             # ali isimli bir obje yarattik

ali.sql                          # ozelliklerine eristik
ali.deneyim_yili
ali.bolum

# alinin ozelliklerini nasil degistirecegiz?
ali.bildigi_diller.append("Python")            # Python dilini bildigi dillere eklemis olduk
ali.bildigi_diller

# veli objesi
veli = VeriBilimci1()
veli.sql
 
veli.bildigi_diller          # burada direk bildigi dillerde Pyhton geldi ama biz Pyhton girmedik ki veli icin???
                             # yukarıda alide yapilan bir degisiklik butun sinifa mal oldu 
                             # deger atamasi yapinca sinifin tum ozelliklerini degistirdi. 
                             # Diger bolumde bunu giderecegiz.
                            

################################################################################################

# ORNEK OZELLIKLERI
# Yani orneklerin her birisinin kendi icinde degisebilir ozelliklerden olustugu bilgisini Python'a vermemiz gerekiyor

class VeriBilimci2():
    def __init__(self):            # __init__ ile her bir ornegin kendi icerisinde degisen ozelliklerden olusabildigi bilgisini vermis oluyoruz 
        self.bildigi_diller = []
        
ali = VeriBilimci2()
ali.bildigi_diller

veli = VeriBilimci2()
veli.bildigi_diller


# alinin bildigi dillere Java'yi ekleyelim
ali.bildigi_diller.append("Java")
ali.bildigi_diller                                # aliye ekledi
veli.bildigi_diller                               # ama veliye eklemedi istedigimiz sey buydu


veli.bildigi_diller.append("R")                 # veli ye R eklendi 
veli.bildigi_diller                           
ali.bildigi_diller                              # ama aliye R eklenmedi ve bunu düzelttik

# VeriBilimci2 sinifinin ozellikleri degisti mi ona bakalim
VeriBilimci2().bildigi_diller                      # bos liste olarak gelir. bir ozellik/dil yok yani icinde

# ---------------------------------------------------------------------------------------------------

# bu ozellikleri ve hem ornek ozellikleri hem de VeriBilimci3()'un kendi sinif ozelligini tanimlamaliyiz
class VeriBilimci3():
    
    bildigi_diller = ["R", "PYTHON"] # VeriBilimci3() sinifinin da ozelligini tanimlamis olduk
    
    def __init__(self):            # __init__ ile her bir ornegin kendi icerisinde degisen ozelliklerden olusabildigi bilgisini vermis oluyoruz 
        self.bildigi_diller = []

ali = VeriBilimci3()
ali.bildigi_diller

veli = VeriBilimci3()
veli.bildigi_diller


# alinin bildigi dillere Java'yi ekleyelim
ali.bildigi_diller.append("Java")
ali.bildigi_diller                                # aliye ekledi
veli.bildigi_diller                               # ama veliye eklemedi istedigimiz sey buydu


veli.bildigi_diller.append("R")                 # veli ye R eklendi 
veli.bildigi_diller                           
ali.bildigi_diller                              # ama aliye R eklenmedi ve bunu düzelttik


# VeriBilimci3 sinifinin ozellikleri degisti mi ona bakalim
VeriBilimci3.bildigi_diller                      # yukarida tanimlanan ['R', 'PYTHON'] degerleri gelir sadece -- () olmadan yap islemleri
# burada VeriBilimci sinif ozelliklerinde R ve PYTHON vardir

# Dolayisiyla burada birbirleriyle olan etkilesimleri kesilmis durumda

#----------------------------------------------------------------------------------------------------
class VeriBilimci4():
    
    bildigi_diller = ["R", "PYTHON"] # VeriBilimci4() sinifinin da ozelligini tanimlamis olduk
    # sinifa yeni ozellikler ekledik
    bolum = " "                   # sinifin ozellikleri bunlar
    sql = " "
    deneyim_yili = 0
    
    def __init__(self):            # __init__ ile her bir ornegin kendi icerisinde degisen ozelliklerden olusabildigi bilgisini vermis oluyoruz 
        self.bildigi_diller = []
        self.bolum = " "              # siniflar icin tanimlanan ozellikler, ornekler icin degistirilebilir bir formata getiriliyor burada. sebebi bir ornekte yapilan degisiklik digerlerini etilemesin diye
        

ali = VeriBilimci4()
ali.bildigi_diller
ali.bolum
ali.deneyim_yili
ali.sql


veli = VeriBilimci4()
veli.bildigi_diller
veli.bolum
veli.deneyim_yili
veli.sql



# alinin bildigi dillere Java'yi ekleyelim
ali.bildigi_diller.append("Java")
ali.bildigi_diller                                # aliye ekledi
veli.bildigi_diller                               # ama veliye eklemedi istedigimiz sey buydu


veli.bildigi_diller.append("R")                 # veli ye R eklendi 
veli.bildigi_diller                           
ali.bildigi_diller                              # ama aliye R eklenmedi ve bunu düzelttik


VeriBilimci4.bildigi_diller  


VeriBilimci4.bolum
ali.bolum = 'istatistik'
VeriBilimci4.bolum              # alinin bolumune istatistik eklenmesi VeriBilimci4'un bolum kismini etkilemedi

veli.bolum = "end_muh."
veli.bolum
ali.bolum                      # velinin bolumune end_muh eklenmesi VeriBilimci4'un bolum kismini etkilemedi
VeriBilimci4.bolum             # velinin bolumune end_muh eklenmesi VeriBilimci4'un bolum kismini etkilemedi


# self neyi temsil eder??  -- olusturdugumuz ornekleri temsil eder

# Biz burada sinif ozellikleri ile ornek ozelliklerin isimlerini ayni verdik ama genelde Sinif ozelliklerin ismini farkli isimlendirmeler vermek gerekir

#################################################################################################

# ORNEK METODLARI

# sinif yapisi icerisine fonksiyon eklemek istiyoruz- dil ekleyen bir metot olsun bu

class VeriBilimci5():
    calisanlar = []       # VeriBilimci5() sinifinin bir ozelligi calisanlar oldu
    
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = " "
        
    def dil_ekle(self, yeni_dil):              # metot tanimladik - buradaki self bunu ornekler uzerinde calistiracak. ali veli vs. uzerinde yani
        self.bildigi_diller.append(yeni_dil)
    
    
ali = VeriBilimci5()
ali.bildigi_diller
ali.bolum    
    
veli = VeriBilimci5()
veli.bildigi_diller    
veli.bolum
    

dir(VeriBilimci5)        # sinif nesnemizin kullanilabilir degerlerine baktıgımız zaman burada calisanlar ve dil_ekle'yi(metot) goruruz
dir(VeriBilimci5())      # () ile bakarsak --sinif nesnemizin kullanilabilir degerlerine baktıgımız zaman burada calisanlar ve dil_ekle(metot)  +++ olarak bolum ve bildigi_diller de gelir () ile baktıgımız zaman
    
    
# ali ve veli de dil yok - ekleyelim dil_ekle metodunu kullanarak

VeriBilimci5.dil_ekle("R")            # bunu VeriBilimci5 sinifi uzerine ekleyelim dedik hata aldik.sebebi bu metot ornekler uzerinde calisacak cunku
    
# bunu ornekler uzerine ekleyebiliriz
ali.dil_ekle("R")             # aliye dil_ekle metodunu kullanarak R dilini ekledik
ali.bildigi_diller            # buraya gelmis oldu

veli.dil_ekle("Python")        # veliye dil_ekle metodunu kullanarak Python dilini ekledik
veli.bildigi_diller    
    
#################################################################################################   
    
# MİRAS YAPILARI (inheritance)

# tanimlamis oldugumuz class, daha once tanimlamis oldugumuz baska bir class'in ozelliklerini barindiriyorsa
# ve onlari kullanmak istiyorsak, iste bu class'in ozelliklerini miras olarak kullanabiliriz

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
    
class DataScience(Employees):
    def __init__(self):
        self.Programming = ""
        

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""


veribilimci1 = DataScience()          # obje yarattık
veribilimci1.Programming              # burada verdiği ozellik sadece Programming oldu    

# inheritance yapinca FirstName, LastName ve Address ozellikleri de gelmis oldu
veribilimci1.FirstName
veribilimci1.LastName        
veribilimci1.Address

# ayni sekilde marketing icinde miras yaptik
mar1 = Marketing()
mar1.StoryTelling
mar1.FirstName
mar1.LastName
mar1.Address

# ---------------- dogru kullanim  --------------------

# bir sinifi tipki bir fonksiyon gibi belirli argumanlar alarak olusturabilmek adina bu sekilde tanimlamis olduk -- onceki tanimladigimiz sekli sabit degerlerden olusuyor

class Employees_new():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        
ali = Employees_new("Ali", "Uçan", "Istanbul")       # ali isimli objemizi yaratmış olduk
ali.Address
ali.FirstName
ali.LastName

#####################################################################################################
#####################################################################################################

# FONKSIYONAL PROGRAMLAMA - daha esnke ve bizi daha iyi anlayan bir programlama yaklasimidir

# fonksiyonlar dilin bas tacidir
# fonksiyonlar birinci sinif nesnelerdir
# yan etkisiz fonksiyonlar(stateless, girdi-cikti)
# yuksek seviye fonksiyonlar
# vektorel operasyonlar

# -----------------------------------------------------------------------------------------------

# Yan Etkisiz Fonksiyonlar (Pure Functions)

# Ornek1 : Yan Etki- Bagimsizlik  -- disaridaki bir nesneden etkilenmesi durumudur

A = 5

def impure_sum(b):           # impure : saf olmayan
    return b + A 

def pure_sum(a, b):          # pure : saf
    return a + b
    

impure_sum(6)        # ciktisi : 11 oldu.
                     # A = 9 olarak tekrar atadik cikti: 15 oldu
                     # yani fonksiyonun disaridan bir sekilde bagimliligi var ve birseyler etkileyebiliyor.
                     # yapisini bozabiliyor
                     
pure_sum(3, 4)       # bu fonksiyonun sonucunun herzaman 7 olacagini biliyoruz, disaridan mudahale yok
                     # ancak bir girdi verdiginde cikti uretecegini biliyoruz ve ciktinin her zaman ayni olacagini biliyoruz
                     

# Ornek2: Olumcul Yan Etkiler
# OOP  ile inceleme

class LineCounter():                        # dosyayi acip icindekileri saymak uzere bir sinif tanimladik
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
    
lc = LineCounter('deneme.txt')

print(lc.lines)            # ciktisi : [] -bos
print(lc.count())          # count dedigimizde 0 degeri geldi  - bos

# simdi dosyamizi okuma islemi yapalim

lc.read()                    # dosyayi okudu

print(lc.lines)                    # lines'lari getirdi
print(lc.count())                  # toplam kac satirdan olustugunu sayisini dondurdu

                                    # bu duruma ic nesnenin degismesi denir
                                    

# FP  ile inceleme

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read("deneme.txt")              # dosyayi okudu
lines_count = count(example_lines)              # satirlarin toplamini bulur
lines_count

# burada birbirini etkileyen herhangi bir yapi yok, ancak verdigimiz girdi ile cikti uretmesini bekliyoruz
# verdigimiz girdi disinda bir cikti uretemez. cunku yandan etkileyen yapisini bozan birsey yok


# ------------------------------------------------------------------------------------------------

# İsimsiz Fonksiyonlar (Anonymous Functions)

def old_sum(a, b):
    return a + b
                     
old_sum(4, 5)


new_sum = lambda a,b: a+b 
new_sum(4, 5)


sirasiz_liste = [('b', 3), ('a', 8), ('d', 12), ('c', 1)]
sirasiz_liste

# amacimiz bu tuple'lari siralamak. indexe gore kucukten buyuge gore siralamak istiyoruz

sorted(sirasiz_liste, key=lambda x: x[1])            # hicbir degere atamadan isimlendirme islemi yapmadik


# --------------------------------------------------------------------------------------------------

# Vektorel Operasyonlar

# OOP ile cozumu
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# amacimiz bu iki liste icerindeki her bir elemani birbiri ile carpmak olsun

ab = []

range(0, len(a))

for i in range(0, len(a)):               # a'nin 0.indeksinden 3.indeks git (3.dahil 4.zaten yok) 
    ab.append(a[i] * b[i])
ab


# FP ile cozumu

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a*b                                   # sonuc cok kolay sekilde geldi


# --------------------------------------------------------------------------------------------------

# map & filter & reduce Fonksiyonlari

liste = [1, 2, 3, 4, 5]

# amacimiz su liste'nin her bir elemanina 10 eklemek istiyoruz

for i in liste:
    print(i + 10)


##### map - verilen bir nesnenin icerisinde tanimlanan bir fonk. calistirma imkani verir
list(map(lambda x: x * 10, liste))   



##### filter -- iteratif bir nesne alir bu nesne uzerinden baska bir iteratif nesne olusturulur 
           # iteratif nesne icerisinde aradigi sartin saglandıgı tum elemanlar filtrelenir
           
           
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# amacimiz su ikiye bolundugunda 0 kalan degerlere ulasmak istiyoruz

list(filter(lambda x: x % 2 == 0, liste))



##### reduce - indirgeme islemi yapar

from functools import reduce

liste = [1, 2, 3, 4]
reduce(lambda a,b: a + b, liste)



#####################################################################################################
#####################################################################################################

# Modul Olusturmak ve İstisnalar

# Modul Olusturmak (Kutuphane/Paket)

# modul - belirli bir amaci yerine getirmek icin bulunan fonksiyonlar toplulugudur

# amacimiz su:  maaslarla ilgili islemler gerceklestiren birkac tane fonksiyonumuz old. dusunelim
#               bunu paketleyip bir kullanilabilen bir modul haline getirip kullanisli hale getirelim

# HesapModulu isimli dosyayi olusturduk. altina bir fonksiyon yazdik. 
# bunlara eriselim

import HesapModulu
HesapModulu.yeni_maas(1000)

# farkli kullanim 1
import HesapModulu as hm
hm.yeni_maas(1000)

# farkli kullanim 2
from HesapModulu import yeni_maas
yeni_maas(4000)

import HesapModulu as hm
hm.maaslar

# ---------------------------------------------------------------------------------------------------

# Hatalar(İstisnalar) - Exceptions 


# ZeroDivisionError hatasi 
a = 10
b = 0

a/b            # ZeroDivisionError hatasi aliriz

# buna onlem almak adina try-except yapisi kullanilir

try:
    print(a/b)                 # bunu calistirmaya calis
except ZeroDivisionError:    # calismazsa bu hatayi alirsa bu durumda calismayi surdur ve programi bozma- istisna olarak gor
    print("Paydada sifir olmaz")     # ekrana bunu yazdir
    
# try- except ile oncekindeki gibi bir hata almadi. 


# TypeError hatasi

a = 10
b = "2"

a / b       # TypeError aldik

try:
    print(a/b)                 # bunu calistirmaya calis
except TypeError:    # calismazsa bu hatayi alirsa bu durumda calismayi surdur ve programi bozma- istisna olarak gor
    print("Sayi ve string problemi")     # ekrana bunu yazdir
    
# problem calismayi kesmedi ve calismasina devam etti


# bunlar bolunebilir degerlerden olussaydi

a = 10
b = 2

a / b   

try:
    print(a/b)                          # ayni tipten oldugu icin kolaylikla islem gerceklesti  
except TypeError:
    print("Sayi ve string problemi")













