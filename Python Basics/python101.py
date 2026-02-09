# SAYILAR VE STRİNGLERE GİRİŞ

9
9.2
9+9
9*9

print("HELLO AI ERA")

type(9)
type(9.2)
type("Hello AI ERA")

# ---------------------------------------------------------------------------------------------
# STRINGLERE YAKINDAN BAKALIM
123
type(123)

"123"
type("123")

"a" + "b"
"a" "b"
"a" " b"

"a" + "-b"      # yan yana ekler (toplamak anlamında değil)
"a" - "b"       # TypeError hatası verir sebebi string değerleri birbirinden çıkartamaz

"a"*3           # çıktısı : aaa olur
"a "*3          # çıktısı: a a a olur  (çoğaltmak anlamında kullanılır)

"a"/3           # typeError hatası verir sebebi string değerleri bölemez

# ---------------------------------------------------------------------------------------------

# METOT- FONKSİYON

# metot nedir? -veri yapıları veya belirli yapılar üzerine uygulanan çeşitli fonksiyonlardır.(kabaca fonksiyon demektir)
# fonksiyon nedir? - belirli görevleri/ amaçları yerine getiren yapılardır.


# ---------------------------------------------------------------------------------------------
# STRING METOTLARI  - len() : verilen ifadenin boyutuna baksın istiyoruz

gel_yaz = "gelecegi_yazanlar"    # atama işlemi

a = 9
b = 10

a * b

# mvk = "gelecegi_yazanlar"       -- önceden atamıştık buraya bunu variable explorer kısmından silmek istersek del mvk denir
# del mvk     

len("geleceği_yazanlar")
len(gel_yaz)      # gel_yaz'ın uzunluğuna baktık


# ---------------------------------------------------------------------------------------------

# STRING METOTLARI  -  upper() & lower()

gel_yaz = "geleceği_yazanlar"

gel_yaz.upper()       # tüm karakterleri büyük harfe çevirir
gel_yaz.lower()       # tüm karakterleri küçük harfe çevirir

#gel_yaz.center(50,"-")  #-- çıktısı:  '----------------gelecegi_yazanlar-----------------'   # kendim denedim


# ---------------------------------------------------------------------------------------------

# STRING METOTLARI  -  isupper() & islower()    --- gelen karakterler büyük harf mi? küçük harf mi?

gel_yaz.islower()
gel_yaz.isupper()

B = gel_yaz.upper()   
B.isupper()
B.islower()


# ---------------------------------------------------------------------------------------------

# STRING METOTLARI  -  replace()
# Karakter dizilerinde karakter değiştirme işlemleri için kullanılan replace metodu ele alınıyor.

gel_yaz = "gelecegi_yazanlar"

gel_yaz.replace("e", "a")    # e harflerini a ile değiştir

# kalıcı değişiklik yapmak istersen gel_yaz' a tekrardan ata bu çıktıyı

gel_yaz.replace("a", "i")    # a harflerini i ile değiştir


# ---------------------------------------------------------------------------------------------

#  STRING METOTLARI  -  strip() --  sadece baştan sondan varsa onları kırpıyor
# karekter dizilerinde istenmeyen karakterleri kırpma işlemleri için strip metodu kullanılır.

gel_yaz = " gelecegi_yazanlar "   # kenarlara boşluk koyduk. onları kırpacağız

gel_yaz.strip()            # kendisi kenardaki boşlukları direk alarak kırpma/ silme işlemini gerçekleştirdi
                           # ön tanımlı(default) değeri boşluk kırpma şeklindedir
                           
gel_yaz = "*gelecegi_yazanlar*" 

gel_yaz.strip("*")

gel_yaz = "*gelecegi_y*azanlar*" 

gel_yaz.strip("*")


# ---------------------------------------------------------------------------------------------

# METOTLARA GENEL BAKIŞ

gel_yaz = "gelecegi_yazanlar" 

dir(gel_yaz)                 # dir() ile oluşturduğumuz değişkene hangi metot/ fonksiyon uygulanır onun genel bilgisini verir
                             # veri tipinin üzerine uygulanabilecek olan metotlara gitmektir
dir(str)

dir(int)
dir(float)

# sorgulanan ekranda capitalize() metodunu gördük diyelim deneyelim
gel_yaz.capitalize()     # ilk karakterleri büyütür gerisi küçük olarak kalır

# sorgulanan ekranda count() metodunu gördük diyelim deneyelim
gel_yaz.count("e", 1, 16)           # e harfi şu aralıklarda kaç tane var onun bilgisini getirir. 
gel_yaz[0]                          # (index numaraları 0'dan başlıyor)

gel_yaz.title()         # her kelimenin ilk harfini büyütür - başlık gibi


# ---------------------------------------------------------------------------------------------

# SUBSTRINGLER - Karakter Dizilerinde Alt Küme İşlemleri

gel_yaz = "gelecegi_yazanlar" 

gel_yaz[0]

gel_yaz[20]           # IndexError verir - sebebi 17 karakterimiz var 20 değil ondan dolayı

gel_yaz[0:3]          # gel ifadesini yazdırdık - sol dahil sağ hariç şeklinde çalışır. 3'e kadar

gel_yaz[3:8]

# ---------------------------------------------------------------------------------------------

# DEĞİŞKENLER

a = 9                # değişken oluşturduk- tipi int
b = "ali_uzaya_git"      # değişken oluşturduk- tipi string

c = a * 2

a/c
a*c
a*5

type(100)       # sayısal int tipinde
type(100.2)     # sayısal float tipinde
type(1 + 2j)    # sayısal ama complex tipinde


# ---------------------------------------------------------------------------------------------

# TİP(TYPE) DÖNÜŞÜMLERİ 



# Not: input() fonksiyonu kullanıcıdan bilgi almak için kullanılır.

toplama_bir = input()
toplama_iki = input()


# kullanıcıdan bir değer alınırsa bu değer ilk olarak string olarak gelir. bu ifadeyi dönüştürmemiz gerekebilir.
type(toplama_bir)         # str olur çıktısı
type(toplama_iki)         # str olur çıktısı

toplama_bir + toplama_iki   # çıktısı:  1020   oldu. bu hatalı iki ifadeyi yan yana ekledi toplamadı birleştirme işlemi yaptı sadece

int(toplama_bir) + int(toplama_iki)  # çıktısı:  30     - matematiksel anlamda toplama yapmış olduk 


# float'ı int'e çevirme
11.0
int(11.0)


# int'i float'a çevirme
12
float(12)

# int'i str'ye çevirme
12
str(12)
type(str(12))



# ---------------------------------------------------------------------------------------------

# Kod Çıktısını Ekrana Yazdırmak: print() Fonksiyonu

print("Hello AI ERA")

print("geleceği", "yazanlar")

print("geleceği", "yazanlar", sep="_")     # sep argümanı ile iki kelime arasına _ veya başka bir karakter eklemek

# argüman nedir? - Fonksiyonların genel amaçlarını biçimlendirmek için kullanılan alt görev belirticilere argüman denir

print()      # yazınca editörün help kısmında kullancağın metodun argümanlarına ulaşabilirsin
             # veya
             # ?print, ? type vs yazarak o metodun argümanlarına erişebilirsin








