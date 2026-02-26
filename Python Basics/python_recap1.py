# PYTHON
# variables
# functions
# List
# Tuple
# Dictionary
# Conditionals
# For Loop
# While Loop
# OOP
# Classes
# Errors
# Exceptions

# variable(degisken)
# yorum satırı yapmak için kullanılır

var1 = 10    #integer
var2 = 15
 
gun="bugün günlerden salı"   #string

var3 = 10.0

# 3var = 10

#  3var =10.2 şeklinde tanımlanamaz çünkü sayılar başa gelemez değişken isimlerinde



#string
s = "string tanımlama"

variable_type = type(s)  # str = stringin kısaltmasıdır

print(s) #ekrana yazdırma

var1 = "izmir"
var2 = "ankara"
var3 = var1 + var2

print(var3)

var4 = "600"
var5 = "100"
var6 = var4 + var5

print(var6)

uzunluk = len(var6)  #uzunluğuna bakılır bu şekilde

# var6[3] = 3.indexi nedir diye sorar? çıktısı 2 olur



# numbers
integer_deneme = -50

# double = float = ondalikli sayilar
float_deneme = -30.7

# float = 10 şeklinde bir tanımlama yapılmaz çünkü float bir metot ismi variable olarak tanımlanmıyor


#  built-in functions -- 
str1 = "deneme"

float1 = 10.6  
#float(10)--- floata çevirir
# int(float1)--- int'e çevirir
# round(float1)--- 11'e yuvarlar


str2 = "1005"
# int(str2) --Out[10]: 1005  // type(int(str2))-- Out[11]: int


# user defined functions  -- kullanıcı tarafından istediğimiz özellikte fonksiyonlar tanımlamak

var1 = 20
var2 = 200

output = (((var1+var2)*50)/100.0)*var1/var2

var3 = 30
var4 = 50

output1 = (((var3+var4)*50)/100.0)*var3/var4

var5 = 40
var6 = 20

output2 = (((var5+var6)*50)/100.0)*var5/var6



# def= definition kısatlması-- bu bizim kendi yazdığımız fonksiyonumuz
def benim_ilk_func(var1,var2):   
    """
    bu benim ilk denemem---ne yaptığımızı açıklamak için kullandığımız satırlardır
   
    parametre:
       
    return:    
    """
    #yukarıdaki kısım bizim fonsiyonumuzun tanımı olacak başka bir insan okuduğunda bilecek ne old.
    
    output = (((var1+var2)*50)/100.0)*var1/var2
    return output

sonuc=benim_ilk_func(var1, var2)  #tanımlanan fonsiyonu burada kullandık



def benim_ilk_func(a,b):   
    """
    bu benim ilk denemem---ne yaptığımızı açıklamak için kullandığımız satırlardır
   
    parametre:
       
    return:    
    """
    
    output = (((a+b)*50)/100.0)*a/b   #burada a ve b diyebiliriz bunlar fonk. tanımlamak içindi bunları görmez sadece formül gibi düşün sonuc kısmında değerlerini atadık
    
    return output

sonuc=benim_ilk_func(var1, var2)  #tanımlanan fonsiyonu burada kullandık



def deneme1():
    print("bu benim ikinci denemem")
    
# default and flexible functions

# default f: çemberin çevre uzunluğu = 2 * pi * r

def cember_cevresi_hesapla(r , pi=3.14):  # pi=3.14 değerini atarsam default bir değer verilmiş olur
    """
    çember çevresi hesaplama
    input(parametre): r , pi
    output = çemberin çevresi
    """
    output = 2 * pi * r    
    return output


# flexible f: 
    
def hesapla(boy, kilo): 
    output = boy + kilo
    return output    


# toplu yorum satırına almak için CTRL + Ö (VSCode) kullanılır
def hesapla(boy,kilo,yas):
    output = (boy + kilo)* yas
    return output

def hesapla(boy, kilo, *args):
    print(len(args))
    output = boy + kilo
    return output

def hesapla(boy, kilo, *args):  # args birçok değer girilebilir parametrelerdir
    print(args)     # boy , kilodan sonra girilecek değerleri ekrana yazdır
    output = boy + kilo  # boy , kilo toplamlarını yazdır
    return output

#args tübülünün işlemde kullanma

def hesapla(boy, kilo, *args):
    print(args)
    output = (boy + kilo)* args[0] #args tübülünün 0.indexi ile işleme dahil ettik
    return output



age = 10
name = "ali"
lastname = "veli"

def function_quiz(age,name,*args,ayakkabi_numarasi= 35):  #default parametreler sona yazılır
    print("Çocuğun adı: ",name, "Çocuğun yaşı: ",age, "Ayakkabı numarası: ", ayakkabi_numarasi)
    print(type(name))
    print(float(age))
    
    output = args[0] * age
    
    return output

sonuc = function_quiz(age,name,lastname)  # bu kısıma ayakkabi_numarasi=35 yazılmaz default değer old. için
print ("args[0]* age:  ", sonuc)

#yukarıdakinin çıktısı bu olur
# Çocuğun adı:  ali Çocuğun yaşı:  10 Ayakkabı numarası:  35
# <class 'str'>
# 10.0
# args[0]* age:   veliveliveliveliveliveliveliveliveliveli
# burada 10 defa veli yazdırmasının nedeni args yerine verilen değer soyisim girildi o yüzden
    
#Not :consoleda bir string sayıyla çarpılırsa "abc" *2 ---->  Sonuç: Out[10]: 'abcabc' olur



# %% Lambda Function -- amacı daha hızlı bir şekilde fonsiyon yazabilmek
def hesapla(x):
    output = x*x       #def hesapla(x):   return x*x  -- şekilnde de yazılabilir bu kısım-- outputa gerek kalmadan yani
    return output

sonuc= hesapla(3)

sonuc2 = lambda x: x*x
print(sonuc2(3))



# LIST

var1 = 15
var2 = 21
var3 = 35

#yukarıdaki gibi tek tek oluşturmak yerine bunlar için bir liste oluştururuz

liste = [1,2,3,4,5,6] 
type(liste)               #tiplerine baktık
 
list = ["pazartesi" , "salı" , "çarşamba"]      #console'da list[2] yazarsak enter -- çarşamba yazar ekrana
type(list)

value = liste[1]    #listenin 2.elemanına erişmek istersek
print(value)

#listenin son elemanını çağırmak istersek -- consoleda liste[-1] yazarsak ekrana 6 yazar 
last_value = liste[-1]

#birden fazla değer seçmek istersek --- listenin ilk 3 elemanını seçmek istersek  liste[0:3] ile bulunur
liste_divide = liste[0:3]    # 0.,1.,2. index dahil 3.index dahil değildir  --çıktısı 1,2,3 olur 

#listenin kendine özgü build in functionları

# liste[1,2,3,4,5,6]  bu listeyi daha önce tanımlamıştık. console yapıştırdık/tanıttık.  --- 
#  dir(liste)     yazıp Enter'a basılırsa  liste ile kullanabileceğimiz metotları bize yazdırır

#yukarıdakilerden -- append ile listeye yeni bir eleman ekleme

liste.append(7)    #listeye 7 elemanını ekleme
liste.remove(7)    #listeden 7 elemanını kaldırsın
liste.reverse()    #listeyi ters çevirir 1,2,3,4,5,6 yı  6,5,4,3,2,1 şeklinde çevirir

liste2 = [1,5,4,3,6,7,2]
liste2.sort()            #karışık listeyi sıralar-- küçükten büyüğe

# hem integer hem string liste oluşturabilir miyiz? Evet

karısık_list3 = [1,2,3,"aa","bb"]



# TUPLE  -- liste gibi--  çok kullanılmaz

t = (1,2,3,3,4,5,6)

t.count(3)  # tuple içinde kaç tane 3 olduğunu bize döndürür 
t.index(5)  # 5 in indexini bulur sonuç 5 döner
t.index(3)  # 3 ün indexi 2 olur--- bulduğu ilk3 ü döndürür




# DICTIONARY -- sözlük demek -- local database yaratmak istersen kullanabilirsin-- multiple return kullanabilirsin
dictionary = {"ali":35, "veli":45, "ayse":13}

# dictionary["ali"]       ---   Out[14]: 35   --- alinin yaşını bulur
# type(dictionary["ali"])      ---     Out[15]: int  ---alinin typeını bulur

#hepsine erişmek istersek
# ali, veli, ayse = keys 
# 35,  45,  13 = values 

#  dictionary.keys()    --  Out[16]: dict_keys(['ali', 'veli', 'ayse'])   olur
#  dictionary.values()  --  Out[17]: dict_values([35, 45, 13])    verir

#deneme fonksiyonu oluşturduk
def deneme():
    dictionary = {"ali":35, "veli":45, "ayse":13}
    return dictionary

dic = deneme()


# örnek soru

d1 = {"datai" : 40,"team" : 45}

d2 = {"datai" : 55,"team" : 45}
# d1 == d2 mi? False



# CONDITIONALS

# if- else statement
 
var1 = 10
var2 = 20

if (var1 > var2):
    print("var1 büyüktür var2")
elif(var1 == var2):
    print("var1 ve var2 eşittir")
else:                                 # bu kısıma elif(var1<var2):  şeklindede yazabilirdik
    print("var1 küçüktür var2")
    

#örnek-- listenin içinde 6 değeri var mı yok mu anlamak istersek
liste= [1,2,3,4,5]

value=3

if value in liste:
    print("evet {} değeri listenin içinde".format(value))  # print ederken {} bu kısıma value değeri gelir 
else :
    print("hayır")


#örnek  ----  
dictionary = {"ali":35, "veli":45, "ayse":13}
keys = dictionary.keys()

if "ali" in keys:
    print("evet")
else:
    print("hayır")
    
    

# QUIZ

#yılları verecek kaçıncı yüzyıl olduğunu döndürecek  
# ör:  1640.yıl == 17.yy    ,   109.yıl == 2.yy  , 
# sorunun kolay olması adına 2000. yıl == normalde 21.yy ama soruda 20.yy kabul edilecektir-sadece bu kısım 

#metot yazın
    #input integer yıllar olsun
    #output integer yüzyıl döndürsün
    
    #kısıtlama :  input year  :  1 >= year <= 2005
  
def year2Century(year):
    """
    year to century    
    """
    
    str_year= str(year)  #year değerini stringe çevirdik
    
    
    if(len(str_year) < 3):    #girilen sayının uzunluğu 3 den küçükse 1 yazsın(yani 1.yy)
        return 1 
    elif(len(str_year) == 3): #yani 100 den 999 a kadarsa 2 durum var 
        if(str_year[1:3] == "00"):    #100,200,300,400....900 ---- [1:3] --- 1.,2. index dahil 3.index dahil değil demek
            return int(str_year[0])      #0.indexini döndür demek yani 100 ün 1 ini, 200 ün 2 sini, 300 ün 3 ünü vs.----- çıktı olarak int istediğimiz için cast ettik
       
        else:                             #190,250,450
            return int(str_year[0]) + 1   #indexi inte çevirip +1 eklendi ---- 190 2.yy old. için +1 dendi
        
    else:                                 #1750-- 18.yy eder, 1700 -- 17.yy eder, 1805--- yani 2 tane durum var
        if(str_year[2:4] == "00"): #2. ve3. indexlerini al  --son iki basamağı eşitse 00 a ---1700,1900,1100 gibi
            return int(str_year[:2]) # 00 ise ilk iki sayı değerini döndür-- yy olacak nu kısım --- [:2] ilk ikisi demek 
        
        else :                    #1705, 1645,1258
            return int(str_year[:2]) + 1
    



# FOR LOOP

for each in range(1,11):  #1 den 11' e kadar yazdır-- 11 dahil değildir-- her birini tek tek ekrana yazdırır
    print(each)
    
for each in "ankara ist":   #ankara ist ekrana dik biçimde yazdırır
    print(each)    

for each in "ankara ist".split():       #default değere göre ayırır(boşluk)
    print(each)
    



liste = [1,4,5,6,8,3,3,4,67]  #toplasın demek istersek-- consoleda sum(liste)  deriz
     
summation = sum(liste)  #1.yol
#----------------------------------
count = 0

for each in liste :      #2.yol  -- listenin içini dolaş demek

    count = count + each    #her defasında listedeki sayıları üst üste ekleyerek toplayacak 
    print(count)            #her birini ekrana yazdıracak           




# WHILE LOOP

i = 0

while(i < 4) :
    print(i)
    i = i + 1 
    
    
#listenin içindeki elemanları toplamış olduk    
    
scale = len(liste)  #scale listenin uzunluğu kadar olsun-- yukarıda tanımlanan liste
each = 0
count = 0
while(each < scale):
    count = count + liste[each]    
    each = each + 1



# liste verilecek-- listenin içindeki en küçük sayıyı bulmamız isteniyor --- 
#min(liste) deyip en küçük değer bulunabilir  -- biz if-else statement ile yapmak istiyoruz


liste = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

mini = 100000

for each in liste :   #listenin içini gezecek
    if(each < mini):     #değer küçükse min değerden
        mini = each      #yeni değer min olsun
    else :             #değilse
        continue         #listeyi gezmeye devam etsin
        
print(mini)     




#  OBJECT ORIENTED PROGRAMMING(Nesne Tabanlı Programlama)

#Class and Constructor

class Calisan:
    def __init__(self,isim1,soyisim1,maas1):    # __init__ metodu constructordır--  biz burada ne yaptık? self metodu ile dışarıdan gelen isim,soyisim,maas,email bilgisine eşitliyor.
        self.isim = isim1
        self.soyisim = soyisim1
        self.maas = maas1
        self.email = isim1 + soyisim1 +"@asd.com"  
    
    def giveNameSurname(self):    # fonksiyon değeri bilmesi için tanımlanması gerekir.içinde geçeli olması için. selfi o yüzden yazdık. 
        return self.isim +" "+ self.soyisim   # bu fonksiyon isim ve soyisimi bize return eder
        
        
#oluşturulan classtan obje yaratıyoruz. genel yapıyı başta oluşturuyoruz. 
isci1 = Calisan("ali","veli",100)   # isci1 çalışan classının bir objesidir.
print(isci1.isim)
print(isci1.maas)
print(isci1.giveNameSurname())



# CLASS VARIABLES

class Calisan:
    
    zam_orani = 1.8  # CLASS VARİABLE budur
    
    counter = 0  # kaç çalışanımız var onu bulmak için yazıyoruz
    
    def __init__(self,isim1,soyisim1,maas1):    # __init__ metodu constructordır--  biz burada ne yaptık? self metodu ile dışarıdan gelen isim,soyisim,maas,email bilgisine eşitliyor.
        self.isim = isim1
        self.soyisim = soyisim1
        self.maas = maas1
        self.email = isim1 + soyisim1 +"@asd.com"  
        
        # self.counter =self.counter + 1   # bu ne zman çalışır? yeni bir çalışan/obje yarattığında
        # Bu sorunu düzeltmek için Calisan classının counter'ını +1 güncellemeliyiz
        Calisan.counter =Calisan.counter + 1    # daha doğru olacaktır
    
    def giveNameSurname(self):    # fonksiyon değeri bilmesi için tanımlanması gerekir.içinde geçeli olması için. selfi o yüzden yazdık. 
        return self.isim +" "+ self.soyisim  
    
    
    def zam_Yap(self):
        self.maas = self.maas + self.maas * self.zam_orani          #NOT: FONKSİYON DIŞARIYA ERİŞEMEZ. CLASS'IN VARİABLEINA ERİŞEBİLMEK İÇİN BAŞINA self yazılmalı

calisan1 = Calisan("ali", "veli", 100)   # bir çalışan yarattıkş.mö
print("ilk maaş:", calisan1.maas)
calisan1.zam_Yap()
print("Yeni maaş:" , calisan1.maas)

calisan1.counter    # çıktısı 1 olur. 1 çalışanımız var

calisan2 = Calisan("ayse", "hatice", 200)
calisan2.counter    # çıktısı 1 olur nedennnn??? çünkü biz her bir obje için counter'ı sıfırdan başlayıp +1 güncelliyoruz
                    # Bu sorunu düzeltmek için Calisan classının counter'ını +1 güncellemeliyiz

# Calisan'a counter ekledikten sonra çıktı
Calisan.counter                           # calisan1 tanımlıyken çıktısı 1

calisan2 = Calisan("ayse", "hatice", 200)  # calisan2 tanımlandık. yeni çalışan tanımladık
Calisan.counter                            # bu defa 2 çalışanın var dedi sorunu çözdük.çıktısı : 2



# CLASS EXAMPLE 
# 2 tane çalışan yaratmıştık 2 tane daha yaratalım

calisan3 = Calisan("fatma", "hayriye", 300)
calisan4 = Calisan("lale", "çiçek", 500)

#çalışanları liste içinde depolayabilir miyiz?
liste = [calisan1, calisan2, calisan3, calisan4]    # bu liste çalışan objeleri depoluyor/ tutuyor
print(liste)

# şimdi bu listedeki objeleri karşılaştırmak istiyoruz, en yüksek maaş alanı bulmak istiyoruz

maxi_maas = -1    # initial(ilk) değer tanımlıyoruz
index = -1        # initial değer tanımlıyoruz

for each in liste: 
    if(each.maas > maxi_maas):        
        maxi_maas = each.maas   # max maaşı bulduk
        index = each       # indexi eache eşitlersek biz bu indeksi tutmuş oluruz. en yüksek maaaşı kim alıyor onu bulmak için yaptık
                
print("En yüksek maas: ", maxi_maas)
print(index.giveNameSurname())       # index bilgisini kullanarak giveNameSurname() fonksiyonu ile isim soyisim bilgisini getiriyoruz




# -------  syntax errors   --------

print(9)
# print9

int(10.0)
# int 10.0

i = 0
while(i < 10):
    print(i)
    i = i + 1    # bunu yazmazsan sonsuz döngüye girer

# exceptions

a = 10
b = "2"
liste = [1,2,3]
print(sum(liste))
print(a+b)  # bu kısım hata verir string ile integer'ı toplayamazsın der. datatype'ları farklı çünkü
print(str(a) + b)      # bu şekilde tip dönüşümü  ile çözebiliriz

k = 10
zero = 0

print(k)     # k şekilinde bir tanımlı değer olmadığı için hata verir
print(k/zero)   # 0'a bölünme hatası verir. ZeroDivisionError verir

if (zero == 0):
    a = 0
else:
    a = k / zero

print(a)                                 # çıktısı 0 olur.


try:
    a = k / zero
except ZeroDivisionError:
    a = 0

print(a)                           # çıktısı 0 olur.


# index error
list1 = [1,2,3,4]
list[15]   #listenin 15. elemanına erişmez çünkü 15 eleman yok listede
    

# module not found error

#import numpyy   # adını yanlış girdi
import numpy


# file not found
import pandas as pd
pd.read_csv("asd")   #FileNotFoundError hatası


#type error
"2" + 2     # TypeError hatası 


#value error
int("123")   # inte cast eder
int("sad")    # ValueError hatası verir

try:
    1/0                                # 1/0 olsaydı
except:
    print("except")
else:
    print("else")
finally:
    print("done")                        # çıktısı: except done olur 
    
    
try:
    1/1                                # 1/1 olsaydı
except:
    print("except")
else:
    print("else")
finally:
    print("done")                      # çıktısı: else done olur