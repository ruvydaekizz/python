# VERI YAPILARI

# 1. LISTELER  --   kapsayicidir(farkli tipte verileri tutabilir), siralidir, degistirilebilir.

# Python'da liste olusturmak icin 2 yol var.    --  1. []   2. list()

notlar = [90, 80, 70, 50]

# string ve numerik tipler de olabilir icerisinde 

type(notlar)
type() 

liste = ["a", 19.3, 90]
liste_genis = ["a", 19.3, 90, notlar]

len(liste_genis)   # sonucu 4 olur. eleman sayisi 4'tur

# ---------------------------------------------------------------------------------------------

# Liste Ici Tip Sorgulama

type(liste_genis)

liste_genis[0]
liste_genis[1]
liste_genis[2]
liste_genis[3]

type(liste_genis[0])
type(liste_genis[1])
type(liste_genis[2])
type(liste_genis[3])

type(liste_genis[3][1])    # liste_genis içerisindeki notlar listesinin 1.elemanina erişmek istersek


tum_liste = [liste, liste_genis]    # 2 ayri listeyi kullanip tamamini kapsayan yeni bir liste olusturduk

# bir listeyi silmek istersek
# del tum_liste

# ---------------------------------------------------------------------------------------------

# Liste Elemanlarina Erismek

liste1 = [10, 20, 30, 40, 50]

liste1[0]
liste1[1]

liste1[6]    # IndexError aliriz içerisinde 6 indexli bir eleman degil

liste1[0:2]
liste1[:2]

liste1[2:]


yeni_liste = ["a", 10, [20,30,40,50]]
yeni_liste

yeni_liste[3]    # IndexError aliriz içerisinde 3 indexli bir eleman degil

yeni_liste[2]
yeni_liste[0:2]

yeni_liste[2][1]   # yeni_liste icerisindeki 2.indeksindeki listenin 1.elemanina erismek istersek

# ---------------------------------------------------------------------------------------------

# Listelere Eleman Ekleme, Degistirme, Silme islemleri

liste2 = ["ali", "veli", "berkcan", "ayse"]
liste2

liste2[1] = "velinin_babasi" # veli yerine velinin_babasi ifadesini eleman olarak ekledik
liste2


liste2[1] = "veli"      # tekrar eski haline getirdik
liste2

liste2[0:3] = "alinin_babasi", "velinin_babasi", "aysenin_babasi"      # toplu secerek onlara eleman degistirdik
liste2

liste2 = ["ali", "veli", "berkcan", "ayse"]

# listeye yeni eleman ekleme
liste2 = liste2 + ["kemal"]
liste2

#liste icerisinden eleman silme
del liste2[2]          # berkcan'i listeden sildik
liste2

# ---------------------------------------------------------------------------------------------

# Metotlar ile Eleman Ekleme & Silme:   append()  &  remove()

dir(list)             #list ile kullanilan metotlara eriselim

liste3 = ["ali", "veli", "isik"]

liste3.append("berkcan")          # liste3'e berkcan'i ekledik. kalici degisikligi kendisi yapti
liste3

liste3.remove("berkcan")          # liste3'ten berkcan'i sildik.  kalici degisikligi kendisi yapti
liste3



# ---------------------------------------------------------------------------------------------

# Indekse Gore Eleman Ekleme & Silme:  insert()  &  pop()

# insert()

liste4 = ["ali", "veli", "isik"]

liste4.insert(0, "ayse")            # 0.indekse ayse elemanini ekle, yerindekini silmez bir sonraki indekse kaydirir
liste4


liste4 = ["ali", "veli", "isik"]           
liste[0] = "ayse"                   # ayni islemler degil. listenin 0. elemanini degistirdik burada. listeye ekleme yapmadi
liste4

liste4.insert(0, "ayse")            # tekrar 0.indekse ayse elemanini ekle
liste4


liste4.insert(2, "mehmet")          # 2.indekse mehmet elemanini ekle, yerindekini silmez bir sonraki indekse kaydirir
liste4


liste4.insert(5, "berk")            # liste4'in sonunda 5.indekse berk'i ekledik
liste4


# listenin sonuna len(liste4) 'i kullanarak ekleme -- kullanişli importanttt :)

liste4.insert(len(liste4), "beren")
liste4

# pop()
liste4.pop(0)            # 0.indekse sahip olani sil.
liste4

liste4.pop(4)            # 4.indekse sahip olani sil.
liste4

# ---------------------------------------------------------------------------------------------

# Diger Liste Metotlari

dir(list)                  # list ile kullanilan metotlara eriselim


# count()  - listede belirli bir elemanin frekans bilgisini verir
liste5 = ["ali", "veli", "isik", "ali", "veli"]

liste5.count("ali")                    #cıktisi : 2 -- alinin 2 tane oldugu bilgisini verdi

liste5.count("veli")

liste5.count("isik")


# copy()    -  verinin ilk halini korumak/ yedeklemek/ kopyalamak icin kullanilir
liste_yedek = liste5.copy()


# extend()   -  iki listeyi birlestirmek icin kullanilir
liste5.extend(["a","b",10])              # eklemek istedigin listeyi gir direk. degistirerek birlestirme islemi yapmis oldu
liste5


# index()   -  bir elemanin hangi indekste oldugu bilgisini                 
liste5.index("ali")       # ali hangi indekste. cıktısı: 0


# reverse()  - listenin elemanlari tersine cevirme islemi gerceklestirir
liste5.reverse()
liste5

# sort()  - sialama yapmak icin kullanilir

liste6 = [10, 40, 5, 90]
liste6.sort()               # kucukten buyuge siralamıs oldu
liste6

liste6.sort(reverse=True)     # buyukten kucuge siralamis oldu
liste6

# clear()  - listeyi temizleme islemi gerceklestirir

liste6.clear()         # icerisindeki elemanlarin hepsini temizledi
liste6

#############################################################################################

# 2. TUPLE (demet) :    kapsayicidir(farkli tipte verileri tutabilir), siralidir, degistirilemezdir

# tuple() olusturma
t = ("ali", "veli", 1, 2, 3.2, [1, 2, 3, 4])

t = "ali", "veli", 1, 2, 3.2, [1, 2, 3, 4]       # yine olusturabildik

# tuple()

t1 = ("eleman")

type(t1)        # cıktısı str oldu ama tuple vermistik. tuple olmasini istersen yanına bir virgül koyman gerekiyor

t2 = ("eleman", )

type(t2)        # cıktısı tuple oldu bu defa


# ------------------------------------------------------------------------------------------
# tuple() Eleman İslemleri

t3 = ("ali", "veli", 1, 2, 3.2, [1, 2, 3, 4])

t3[1]
t3[0:3]

t3[2] = 99       # TypeError hatasi aldik. Sebebi tuple() degistirilemez
  
#############################################################################################

# 3. DICTIONARY  (sozlukler)  :  kapsayicidir(farkli tipte verileri tutabilir), sirasizdir, degistirilebilir

# Listelerde oldugu gibi index islemleri yapılamaz
# key : value  şeklinde olusturulurlar

# Sozluk olusturma
sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk

len(sozluk)        # cıktisi 3, burada eleman 6 degil 3 eleman vardir


sozluk1 = {"REG": 10,
          "LOJ": 4.2,
          "CART": "cart deger"}

sozluk1


sozluk2 = {"REG": ["RMSE", 10],
          "LOJ": ["MSE", 20],
          "CART": ["SSE", 30]}
sozluk2

# ------------------------------------------------------------------------------------------

# Sozluk Eleman Secme Islemleri

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk[0]     # KeyError hatasi aldik sebebi sozlukler sirasizdir.

sozluk["REG"]
sozluk["LOJ"]


sozluk2 = {"REG": ["RMSE", 10],
          "LOJ": ["MSE", 20],
          "CART": ["SSE", 30]}

sozluk2["REG"]

sozluk3 = {"REG": {"RMSE": 10,                 # sozluk yapisi icerisinde sozluk olusturduk
                   "MSE": 20,
                   "SSE": 30},
           
          "LOJ": {"RMSE": 10,                 # sozluk yapisi icerisinde sozluk olusturduk
                  "MSE": 20,
                  "SSE": 30},
          
          "CART": {"RMSE": 10,                 # sozluk yapisi icerisinde sozluk olusturduk
                   "MSE": 20,
                   "SSE": 30}}

sozluk3

sozluk3["REG"]
sozluk3["REG"]["SSE"]

# ------------------------------------------------------------------------------------------

# Sozluk Eleman Ekleme ve Değistirme

sozluk4 = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}
    
sozluk4["GBM"] = "Gradient Boosting Mac"     # eleman ekleme
sozluk4

sozluk4[1]  =   "Yapay Sinir Aglari"         # eleman ekleme
sozluk4

# listeyi eleman olarak sozluk'e ekleme  
l = [1]
l

sozluk4[l] = "yeni bir sey"         # TypeError hatasi aldik. listelerle key degeri olusturulamaz
                                    # NOT: sozluklerde key degerleri ancak sabit veri yapilariyla olusturulabilir(yani string ve sayilarla)
                                    # keyler sabit kalir, values'ler degistirilebilir

# tuple'i eleman olarak sozluk'e ekleme

t = ("tuple",)                        # tek elemanli bir tuple olusturduk. tuple sabit veri yapisidir. bununla oldu.
sozluk4[t] = "yeni bir sey"           # tuple'i sozluk'e    ekleyebildik
sozluk4


 # var olan bir sozluk elemanini degistirme/guncelleme
sozluk4["REG"] = "Coklu Dogrusal Regresyon"  
sozluk4


sozluk4.keys()                # sadece key'lere erişme
sozluk4.values()              # sadece value'lere erişme

##############################################################################################

# 4. SETLER   (kume):   sirasizidir, degerleri essizdir(unique), degistirilebilirdir, farkli tipleri barindirabilir

# setler essiz elemanlardan olusur

# Set olusturmak

s = set()
s

l = [1, "a", "ali", 123]
s = set(l)                    # liste uzerinden set olusturma
s

t = ("a", "ali")
s = set(t)                    # tuple uzerinden set olusturma
s

ali = "lutfen_ata_bak ma_uza ya_git"
type(ali)

s = set(ali)          # bu cumleyi her bir karakter sadece 1 defa gececek sekilde almis ve hepsini karakterlere bolmus, alfabetik sirayla yazmis
s


l = ["ali", "lutfen", "ata", "bakma", "uzaya", "git", "git", "ali", "git"]

s = set(l)
s               # her bir elemani bir defa yazdirir

len(s)
l[0]
s[0]   # TypeError hatasi aliriz, set nesnesi index islemini desteklemiyor 

# ------------------------------------------------------------------------------------------

# Set Eleman Ekleme ve Cıkarma

l = ["gelecegi", "yazanlar"]
s = set(l)


dir(set)         # set için kullanilan metotlar nelerdir

# eleman ekleme
s.add("ile")     # add ile yeni eleman ekledik
s

s.add("gelecege_git")      # add ile yeni eleman ekledik. cıktida bunlari alfabetik siraya gore ekler
s

s.add("ali")
s

s.add("ile")          # ile'yi bi defa yukarida eklemistik, bi daha ekledik ama ciktida bi defa eklenir. var olan deger bi defa eklenir
s

# eleman silme
s.remove("ali")
s

s.remove("ali")            # ali'yi bi daha silmek istersek hata verir. Neden? cünkü daha once sildik ali bi daha yok
# hata almadan devam etmek istersek(KeyError)

s.discard("ali")     # varsa siler yoksa uyari vermez- kod akisi devam eder

# --------------------------------------------------------------------------------------------------

# Setlerde Fark İslemleri : difference & symmetric_difference

# =============================================================================
# NOT: secilen araligin tumunu topluca comment'e almak istersek   --->> CRTL + 4 
#
# difference() :  iki kumenin farkini ya da "-" ifadesi
# symmetric_difference() : ikisindede olmayanlari
# 
# =============================================================================

# difference() 

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.difference(set2)     # set1'de olup set2'de olmayan degerleri getirir. ciktisi:  {5}

set2.difference(set1)     # set2'de olup set1'de olmayan degerleri getirir.  ciktisi:  {2}

set1 - set2               # ciktisi : {5}
set2 - set1               # ciktisi : {2}

# symmetric_difference()
set1.symmetric_difference(set2)      # ikisinde olmayanlari getirir. ciktisi: {2, 5}
set2.symmetric_difference(set1)      # ikisinde olmayanlari getirir. ciktisi: {2, 5}

# --------------------------------------------------------------------------------------------------

# Setlerde Kesisim ve Birlesim İslemleri : intersection() & union() 

# intersection() : iki kume kesisimi ya da "&" ifadesi
# union() : iki kumenin birlesimi

# intersection()
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)       # iki kume kesisimi, ciktisi: {1, 3}
set2.intersection(set1)        # iki kume kesisimi, ciktisi: {1, 3}      -- ciktilari ayni olur.

kesisim = set1 & set2                   # iki kume kesisimi, ciktisi: {1, 3}
kesisim

# union()
set1.union(set2)             # iki kume birlesimi, ciktisi: {1, 2, 3, 5}
set2.union(set1)             # iki kume birlesimi, ciktisi: {1, 2, 3, 5}

birlesim = set1.union(set2)
birlesim


kesisim = set1 & set2                   # iki kume kesisimi, ciktisi: {1, 3}
kesisim

# intersection_update()     --- sadece keşişimleri alır. onu set1 üzerinden gösterir.

set1.intersection_update(set2)
set1


# ------------------------------------------------------------------------------------------------

# Setlerde Sorgu İslemleri

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

# iki kumenin kesisiminin bos olup olmadigini sorgulayacagiz
set1.isdisjoint(set2)                    # iki kumenin kesisimi bos mu?,   ciktisi: False --> yani kesisim bos degil


# bir kumenin butun elemanlarinin baska bir kume icerisinde yer alip almadigini sorgulayalim
set1.issubset(set2)                      # set1 set2'nin alt kümesi midir?,  ciktisi: True 


# bir kumenin diger bir kumeyi kapsayip kapsamadigi
set2.issuperset(set1)                    # set2 set'i kapsiyor mu?










