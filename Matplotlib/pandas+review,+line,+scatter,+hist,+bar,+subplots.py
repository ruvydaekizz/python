# MATPLOTLIB

# matplotlib kutuphanesi
# line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df = pd.read_csv("iris.csv")   # csv dosyasını import ettik

print(df.head())

print(df.columns)        # feature'larına baktık. kolonlarına yani

print(df.Species.unique())    # benzersiz türleri bulduk

print(df.info())           # data hakkında bilgi edinmeye çalışıyoruz-- data tipleri ne? vs.

print(df.describe())      # count,mean,std,min,25%,50%,75%,max  bunları bulur

setosa = df[df.Species == "Iris-setosa"]   # sadece Iris-setosa'lardan oluşan bir dataframe yarattık-- dataframe'den çek ve setaso'ya ekle
print(setosa)                     

versicolor = df[df.Species == "Iris-versicolor"]   # sadece Iris-versicolor'lardan oluşan bir dataframe yarattık
print(versicolor)

virginia = df[df.Species == "Iris-virginica"]     # sadece Iris-virginica'lardan oluşan bir dataframe yarattık
print(virginia)


# değerlerine detaylıca bakıyoruz
print(setosa.describe())              # count,mean,std,min,25%,50%,75%,max  bunları bulur
print(versicolor.describe())          
print(virginia.describe())            



# line plot
import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis=1)    # Id'yi drop ediyoruz, df1 isimli yeni bir dataframe oluşturuyoruz
print(df1)     # ekranda göster


setosa = df[df.Species == "Iris-setosa"]   # sadece Iris-setosa'lardan oluşan bir dataframe yarattık-- dataframe'den çek ve setaso'ya ekle
versicolor = df[df.Species == "Iris-versicolor"]   # sadece Iris-versicolor'lardan oluşan bir dataframe yarattık
virginica = df[df.Species == "Iris-virginica"]     # sadece Iris-virginica'lardan oluşan bir dataframe yarattık


plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label="setosa - PetalLengthCm") # setosa türünü kırmızı renk olarak görselleştirelim
plt.legend()                            # yazdırdığın label'ı yazdırmanı sağlar- default olarak en uygun yere koyar
plt.xlabel("Id")               # Xlabel ismi verdik
plt.ylabel("PetalLengthCm")    # Ylabel ismi verdik
plt.grid()
plt.show()


plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="green", label= "versicolor - PetalLengthCm")   #versicolor türünü yeşil renk olarak görselleştirelim
plt.legend()                            
plt.xlabel("Id")               
plt.ylabel("PetalLengthCm")     
plt.grid()
plt.show()

plt.plot(virginica.Id, virginica.PetalLengthCm, color="blue", label= "virginica - PetalLengthCm")       # virginica türünü mavi renk olarak görselleştirelim
plt.legend()                           
plt.xlabel("Id")                   
plt.ylabel("PetalLengthCm")        
plt.grid()
plt.show()


df1.plot(grid=True, linestyle=":", alpha= 0.9)          # grid ekledik / çizgi stili ekledik bunlar :, dotted, dashed, dashdot  / alpha: lineların saydamlığını belirleyen bir değerdir
plt.show()




# scatter plot    - nokta nokta gösterir grafikte

setosa = df[df.Species == "Iris-setosa"]   # sadece Iris-setosa'lardan oluşan bir dataframe yarattık-- dataframe'den çek ve setaso'ya ekle
versicolor = df[df.Species == "Iris-versicolor"]   # sadece Iris-versicolor'lardan oluşan bir dataframe yarattık
virginica = df[df.Species == "Iris-virginica"]     # sadece Iris-virginica'lardan oluşan bir dataframe yarattık


plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm ,color="red", label="setosa")  # yazdırdığın label'ı yazdırmanı sağlar- default olarak en uygun yere koyar
plt.legend()                           
plt.xlabel("PetalLengthCm")           
plt.ylabel("PetalWidthCm")            
plt.title("scatter plot")                     # başlık vermeye yarar
plt.show()

plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color="green", label="versicolor")      # versicolor türünü yeşil renk olarak görselleştirelim
plt.legend()                             
plt.xlabel("PetalLengthCm")         
plt.ylabel("PetalWidthCm")          
plt.title("scatter plot")                
plt.show()

plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color="blue", label="virginica")           # virginica türünü mavi renk olarak görselleştirelim
plt.legend()                           
plt.xlabel("PetalLengthCm")       
plt.ylabel("PetalWidthCm")        
plt.title("scatter plot")             
plt.show()



# histogram

plt.hist(setosa.PetalLengthCm, bins=10)          # bu değişkeni histograma dökelim, bins bar sayısıdır
plt.xlabel("PetalLengthCm values")              
plt.ylabel("frekans")                            
plt.title("hist")                               
plt.show()



# bar plot
import numpy as np              # sadece pandas değil numpy ile de kullanabiliriz

x = np.array([1,2,3,4,5,6,7])
y = x*2+5

plt.bar(x,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


x = np.array([1,2,3,4,5,6,7])                              # numpy üzerinden örneği
a = ["turkey","usa","a","b","v","d","s"]
y = x*2+5

plt.bar(a,y) 
plt.title("bar plot")                     
plt.xlabel("x değerleri")                
plt.ylabel("y değerleri")           
plt.show()




# subplots --  # birden fazla satırda veya sütunda aynı grafikte gösterme 

df1.plot(grid=True, alpha= 0.9, subplots = True)        # grid: arkaya ızgara ekler, alpha: saydamlığı belirler, subplots: birden fazla satırda grafiği gösterir
plt.show()

setosa = df[df.Species == "Iris-setosa"]   # sadece Iris-setosa'lardan oluşan bir dataframe yarattık-- dataframe'den çek ve setaso'ya ekle
plt.subplot(3,1,1)                        # satırda 3 bölmeli, 1 sütunlu, 1.grafik
plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label= "setosa")
plt.legend()  
plt.ylabel("setosa -PetalLengthCm")        
plt.show()


versicolor = df[df.Species == "Iris-versicolor"]   # sadece Iris-versicolor'lardan oluşan bir dataframe yarattık
plt.subplot(3,1,2)                        # satırda 3 bölmeli, 1 sütunlu, 2.grafik
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="green", label= "versicolor")
plt.legend()  
plt.ylabel("versicolor -PetalLengthCm")      
plt.show()

virginica = df[df.Species == "Iris-virginica"]     # sadece Iris-virginica'lardan oluşan bir dataframe yarattık
plt.subplot(3,1,3)                       # satırda 3 bölmeli, 1 sütunlu, 3.grafik 
plt.plot(virginica.Id, virginica.PetalLengthCm, color="blue", label= "virginica")
plt.legend()  
plt.ylabel("virginica -PetalLengthCm")     
plt.show()