# PANDAS

# 1) pandas hizli ve etkili for dataframes
# 2) csv ve text dosyalarına acip inceleyip sonuclarimizı da bu dosya tiplerine rahat bir sekilde kaydedebilir.
# 3) pandas bizim isimizi kolaylastiriyor for missing data -- NaN
# 4) reshape yapip datayi daha etkili bir sekilde kullanabiliriz
# 5) slicing indexing kolay
# 6) time series data analizinde cok yardimci
# 7) ayrica herseyden onemlisi hiz pandas hiz acisindan optimize edilmis hizli bir kutuphane

import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 

dataFrame1 = pd.DataFrame(dictionary)
print(dataFrame1)

head = dataFrame1.head()
print(head)
tail = dataFrame1.tail()
print(tail)



# pandas basic method

print(dataFrame1.columns)          # sütunların isimlerini yazdırır

print(dataFrame1.info())            # veri, veri tipleri ile ilgili bilgi yazdırır

print(dataFrame1.dtypes)           # datatipleri ile ilgili bilgi verir

print(dataFrame1.describe())  # numeric feature/columns (age,maas)
# describe(), count, mean, std, min, 25%, 50%, 75%, max değerlerini hesaplar- sadece nümeric olanlar için 



# indexing and slicing

print(dataFrame1["NAME"])            # isimlerini getirir

print(dataFrame1["AGE"])             # yaş bilgisini getirir
print(dataFrame1.AGE)                # yaş bilgisini getirir

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]        # yeni sütun/kolon ekleme yapar
print(dataFrame1)

print(dataFrame1["yeni_feature"])    # dataframe ismi tanımlarken ismi birleşik olsun arada boşluk olmamalı

print(dataFrame1.loc[:, "AGE"])     # tüm satırları, AGE sütununu al

print(dataFrame1.loc[:3, "AGE"])    # 0'dan 3 arası olan(3 dahil) sütunları al, AGE sütununu al

print(dataFrame1.loc[:3, "NAME":"MAAS"])    # 0'dan 3'e kadar olan sütunları al, NAME'den MAAS sütununa kadar al

print(dataFrame1.loc[:3, ["AGE","NAME"]])   # 0'dan 3'e kadar olan sütunları al, AGE ve NAME sütunlarını getir

print(dataFrame1.loc[::-1,:])     # tersten yazdır(reverse yazdır) ve tüm sütunları getir

print(dataFrame1.loc[:,:"MAAS"])    # tüm satırları yazdır, sütunlarda MAAS'e kadar(MAAS dahil) olanları yazdır

print(dataFrame1.loc[:,"MAAS"])# tüm satırları alsın ve MAAS'ı alsın
 
# loc -- location ---- string değerler girersin
# iloc -- integer location   ---- integer değerler girersin
print(dataFrame1.iloc[:, 2])    # tüm satırları al, indeksi 2 olan sütunda ne varsa onu getir
print(dataFrame1.iloc[:, 1])   # tüm satırları al, indeksi 1 olan sütunda ne varsa onu getir




# filtering

filtre1 = dataFrame1.MAAS > 200         # maası 200den büyük olanları filtrele, 200 den büyükse True değilse False değer alacak
print(filtre1)
type((filtre1))     # pandas serisi elde etmiş olduk


filtrelenmis_data = dataFrame1[filtre1]    # filtelediğimiz datayı dataframe'e çevirdik
print(filtrelenmis_data)

filtre2 = dataFrame1.AGE <20      # yaşı 20 den küçük olanları da filtreliyoruz. yaşı 20den küçükse True, değilse False değer döner
print(filtre2)

dataFrame1[filtre1 & filtre2]    # maaşı 200'den büyük olan ve yaşı 20'den küçük olan, genç yeteneği getirir. VE ile birleştirdik

print(dataFrame1[dataFrame1.AGE > 60])    # yaşı 60'dan büyük olanı getir

# yaşı 60'dan büyük ve maaşı 200'den fazla olanı yaz
filtre3 =dataFrame1.AGE > 60
dataFrame1[filtre1 & filtre3]   # yaşı 60'dan büyük ve maaşı 200'den fazla olanı getirdik




# list comprehension
import numpy as np
import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 

dataFrame1 = pd.DataFrame(dictionary)
print(dataFrame1)

dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]        # yeni sütun/kolon ekleme yapar
print(dataFrame1)

ortalama_maas = dataFrame1.MAAS.mean()      # maasların ortalamasını buluruz-- PANDAS'ın bir metotudur
print(ortalama_maas)

ortalama_maas_np = np.mean(dataFrame1.MAAS)     # maasların ortalamasını buluruz-- NUMPY ile bulunabilir bir metotudur
print(ortalama_maas_np)



# LIST COMPREHENSIONS KULLANIMI ile YAZIMI
# yeni bir column oluşturup yazdık
dataFrame1["maas_seviyesi"] = ["dusuk" if ortalama_maas > each else "yuksek" for each in dataFrame1.MAAS]
print(dataFrame1)

# ÖNCEKİ YAZIMI 
#for each in dataFrame1.MAAS:
#    if(ortalama_maas > each):
#        print("dusuk")
#    else:
#        print("yuksek")
        

dataFrame1.columns       # dataframe'in kolonlarına bakıyoruz        

dataFrame1.columns = [each.lower() for each in dataFrame1.columns]       # her each'i gez ve kolon isimlerini küçük harfe çevir
print(dataFrame1.columns)

# yeni feature isimli kolonda boşluk var onu istemiyoruz
"yeni feature".split()          # split metodu bir boşluk varsa o boşluktan ayırır ve iki yeni kelime gibi bir listeye ekler

# eğer iki kelime varsa bu listede uzunluğu 1'den büyükse, bunun 0.'sını seç __ ile 1.'sini birleştir dedik altta
dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]
print(dataFrame1.columns)




# drop and concatenating

dataFrame1.drop(["yeni_feature"],axis=1,inplace = True)     # bir sütunu nasıl drop edebiliriz. yeni_feature kolonunu düşürdük
print(dataFrame1)                                          # axis=0 satır, axis=1 sütunu temsil eder. inplace= True bunu kalıcı hale getir

# dataFrame1 = dataFrame1.drop(["yeni_feature"],axis=1)

data1 = dataFrame1.head() 
print(data1)
data2 = dataFrame1.tail()
print(data2)

# vertical -- dikey olarak alt alta ekler
data_concat = pd.concat([data1,data2],axis=0)      # data1 ve data2'yi birleştir ve bunu satıra yaz
print(data_concat)


# horizontal -- yatay olarak yan yana ekler
maas = dataFrame1.maas
age = dataFrame1.age

data_h_concat = pd.concat([maas,age],axis=1)          # maas ve yaşı yan yana birleştir , bunları sütuna yaz
print(data_h_concat)



# transforming data
dataFrame1["list_comp"] = [ each*2 for each in dataFrame1.age]     # age'in her bir değişkenini 2 ile çarpıp bunlar için yeni bir değişken oluşturup onun içine atadık
print(dataFrame1)


# apply()   -- metodu ile de yapılabilir
def multiply(age):           # fonksiyon oluşturduk
    return age*3            # return ile istediğimiz değeri döndürdük
    

dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)           # apply metodu ile yeni eklenmiş bir değişken(age değişkeni üzerinden)
print(dataFrame1)