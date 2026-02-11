# FONKSIYONLARA GIRIS VE FONKSIYON OKURYAZARLIGI

# fonksiyon: cok tekrar eden ve her defasinda yapmak istemedigimiz islemler icin fonksiyonlar kullanilir
# arguman: fonksiyonlarin genel amaclarini ozellestirip o genel amaclari farkli sekillerde bicimlendirmeye yarayan gorevciler

print()
print            # calistirinca bunun bir fonksiyon old. bilgisini verdi

?print           # bu fonksiyonun dokumantasyonuna ulasmis oluruz

print("a", "b", sep="_")          # sep argumanini kullandik

len("a")

# A.strip("*"), A stringinin başında veya sonunda bulunan * karakterlerini kaldırır.

# ------------------------------------------------------------------------------------------------

# FONKSIYON NASIL YAZILIR?

def kare_al(x):
    print(x ** 2)
    
kare_al(3)

# ------------------------------------------------------------------------------------------------

# BILGI NOTUYLA CIKTI URETMEK

def kare_al(x):
    print("Girilen Sayının Karesi: ", x ** 2)         # virgul yerine + yaparsan hata alirsin, veya str(x**2) yazarak da tamamlayabilirsin
    
kare_al(3)


def kare_al(x):
    print("Girilen sayi: " + str(x) + "\nKaresi: " + str(x**2))
    
kare_al(3)

# ------------------------------------------------------------------------------------------------

# IKI ARGUMANLI FONKSIYON TANIMLAMAK

def carpma_yap(x, y):                          # argumanlar x ve y
    print("x degeri: ", x)
    print("y degeri: ", y)
    print("Carpma islemi sonucu: ", x*y)

carpma_yap(5,8) 

# ------------------------------------------------------------------------------------------------

# ON TANIMLI ARGUMANLAR

?print

def carpma_yap(x, y=1):                          # argumanlar x ve y --> y on tanimli arguman
    print("x degeri: ", x)
    print("y degeri: ", y)
    print("Carpma islemi sonucu: ", x*y)

carpma_yap(5)               # sen buraya y için yeni bir deger girersen on tanımlı yerine yeni degeri kullanir


print("hello" , "AI ERA", sep="_", end="*")

# Argumanlarin Siralamasi

def carpma_yap(x, y=1):  # argumanlar x ve y --> y on tanimli arguman
    print("x değeri: ", x)       
    print("y değeri: ", y)                 
    print("Carpma islemi sonucu: ", x*y)

carpma_yap(y = 2, x = 3)                     # argumanların sirasini bilmiyorsan bu sekildede yazabilirsin

# ------------------------------------------------------------------------------------------------

# NE ZAMAN FONKSIYON YAZILIR?

# tekrar eden gorevleri yerine getirmek ve var olan isleri daha programatik sekilde gerceklestirir

# isi = 40, nem = 25, sarj = 90

(40+25)/90

# tek tek yapmak mantikli degildir. fonksiyon gerekli

def direk_hesap(isi, nem, sarj):
    print((isi + nem) / sarj)

direk_hesap(40, 25, 90)

# ------------------------------------------------------------------------------------------------

# FONKSIYON CIKTILARINI GIRDI OLARAK KULLANMAK(return)

def direk_hesap(isi, nem, sarj):
    return (isi + nem) / sarj                    # return kendinden sonraki alt satirlari calistirmaz. o yuzden ayni satirda yazmak onemlidir

direk_hesap(40, 25, 90) * 9                      # return ile cıktiyi baska islemlerde kullanabiliriz


# ------------------------------------------------------------------------------------------------

# LOCAL VE GLOBAL DEGİSKENLER

# global
x = 10
y = 20

# local = fonk. icinde tanimlanan tanimlanan x ve y benzeri degiskenlerdir

def carpma_yap(x, y):             # x ve y local degiskendir. etki alani fonk. icinde gecerlidir. on tanimli deger olsa dahi local olanlari kullanir, global olanları değil
    return x * y

carpma_yap(2, 3)
    

# ------------------------------------------------------------------------------------------------

# LOCAL ETKI ALANINDAN GLOBAL ETKI ALANINI DEGISTIRMEK

x = []

x.append(1)               # listeye eleman ekledik. bunu fonksiyon ile yapalim
x



k = []

def eleman_ekle(y):
    k.append(y)
    print(str(y) + " İfadesi eklendi")

eleman_ekle("ali")
eleman_ekle("veli")

k

# NOT: python oncelikle local etki alanindaki degiskenleri arar ve bulmaya calisir ve local etki alaninda bulursa oradan kullanir
#      bulamazsa global etki alanini etkilemek adina global etki alanina cikacaktir. ve boylece listeye eklemis olacak.


######################################################################################

# KARAR & KONTROL YAPILARINA GİRİS (KOSULLAR)

# TRUE - FALSE SORGULAMALARI

border = 5000

border == 4000       # 4000 mi? - false döner
border == 5000

5 == 4
5 == 5


# ------------------------------------------------------------------------------------------------

# IF YAPISI

fiyat = 50000
gelir = 40000

gelir < fiyat

if gelir < fiyat:
    print("Gelir fiyattan kucuk")
    print(gelir*2)

# ------------------------------------------------------------------------------------------------

# ELSE YAPISI


fiyat = 50000
gelir = 60000

gelir > fiyat

if gelir < fiyat:
    print("Gelir fiyattan kucuk")
else:
    print("Gelir fiyattan buyuk")

# ------------------------------------------------------------------------------------------------

# ELIF YAPISI

fiyat = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > fiyat:
    print("Tebrikler")
elif gelir1 < fiyat:
    print("Uyarı!!")
else:
    print("Takibe devam")


if gelir3 > fiyat:
    print("Tebrikler")
elif gelir3 < fiyat:
    print("Uyarı!!")
else:
    print("Takibe devam")


if gelir2 > fiyat:
    print("Tebrikler")
elif gelir2 < fiyat:
    print("Uyarı!!")
else:
    print("Takibe devam")
    

# ------------------------------------------------------------------------------------------------

# if ve input ile Kullanici Etkilesimli Program

# mini uygulama

fiyat = 50000
magaza_adi = input("Magaza adi nedir?: ")
gelir = int(input("Gelirinizi giriniz: "))

if gelir > fiyat:   
    print("Tebrikler" , magaza_adi ,"Promosyon kazandınız!!")
elif gelir < fiyat:
    print("Uyari!!! Geliriniz cok dusuk:", gelir)
else:
    print("Takibe devam.")


######################################################################################

# DONGULER

# FOR Dongusu

ogrenci = ["ali", "veli", "isik", "berk"]

ogrenci[0]
ogrenci[1]
ogrenci[2]


for i in ogrenci:
    print("İsim:", i)

# -------------------------------------------------------------------------------------------

# FOR Dongusu - ornek

maaslar = [1000, 2000, 3000, 4000, 5000]
 
maaslar[0]
maaslar[1]
maaslar[2]


for i in maaslar:
    print("Maas:", i)
    print("Zamlı maaslar: ", int(i * 1.20))           # %20 zam yaptik



# -------------------------------------------------------------------------------------------

# DONGU VE FONKSIYONLARIN BIRLIKTE KULLANIMI

def kare_al(a):
    return a **2

kare_al(2)


liste = [1, 2, 3, 4]

for i in liste:
    print(kare_al(i))
    
#### maaşlara % 20 zam yapınız

maaslar = [1000, 2000, 3000, 4000, 5000]

maaslar[0] * 20/100 + maaslar[0]     # bunu her deger icin tek tek yapamayiz. fonksiyon + dongu ile hepsine uygulayalim


# fonksiyon yazimi
def yeni_maas(x):
    return x * 20/100 + x

yeni_maas(1000)


# dongunun yazimi
for i in maaslar:
    print(yeni_maas(i))


# -------------------------------------------------------------------------------------------

# Uygulama: if, for ve Fonksiyonların Birlikte Kullanımı

# maasi 3000 tlden yuksek olanlara %10 zam, maasi 3000 tlden az olanlara %20 zam yapalim

maaslar = [1000, 2000, 3000, 4000, 5000]


def maas_alt(x):
    return x * 20/100 + x

def maas_ust(x):
    return x * 10/100 + x

for i in maaslar:
    if i < 3000:
        print(maas_alt(i))
    else:
        print(maas_ust(i))


# -------------------------------------------------------------------------------------------

# Break ve Continue

# belirli sarti yakalayan ifade saglandiginda bu dongu bitirilmek istenebilir
# ya da bu sati saglayan eleman gormezden gelinmek istenebilir


# amacimiz su: maasi 3000'den az olanlara zam yapmak istiyoruz ama 3000 degerine geldiginde calismayi biraksin
maaslar = [8000, 5000, 2000, 1000, 3000, 7000, 1000]

dir(maaslar)     # ozelliklerine bakiyoruz. sort metodu ile siralayacagiz

maaslar.sort()
maaslar

# BREAK: bir deger kontrol ifadesinde istedigimiz degere gelirse donduyu kirsin
for i in maaslar:
    if i == 3000:
        print("dongu kesildi")      # 3000'e gelince dongu kesildi yazacaktir
        break                       # istedigimiz degere geldikten sonra donguyu burada kir/kes
    print(i)      #   dongu kesilene kadar ondan onceki degerleri yazdirsin


# CONTINUE: bir deger kontrol ifadesine takildiginda bu degeri atlamak icin kullanilir
for i in maaslar:
    if i == 3000:
        print("dongude 3000 atlandi")      # 3000'e gelince 3000'i atlayıp dongude 3000 atlandi yazıp donguye devam eder
        continue                    # istedigimiz degeri atladıktan sonra donguye devam etsin
    print(i)      #     3000 haric digerlerin yazdirir ekrana



# -------------------------------------------------------------------------------------------

# WHILE  : oldugu surece, bu sart saglandigi surece calis demektir.

sayi = 0      #sayi = 0 ise ciktisi: 1,2,3,4,5,6,7,8,9,10 ## sayi = 1 ise ciktisi : 2,3,4,5,6,7,8,9,10 olur.   

while sayi < 10:        # sayi 10'dan kucuk oldugu surece
    sayi += 1          # sayi = sayi + 1  -- üzerine 1 degerini ekle her defasinda arttirir, sayi 10'a gelene kadar dongu devam eder
    print(sayi)
                       



dir(str)




















