# NUMPY

# importing
import numpy as np

# numpy basics
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  # 1*15 vector

print(array.shape)          # çıktısı : (15, )   olur boyut bilgisini verir
  
a = array.reshape(3,5)                   # yeniden biçimlendir, 3'e 5'lik bir biçimde
print("shape: ",a.shape) 
print("dimension: ", a.ndim)        # 2 boyutlu der

print("data type: ",a.dtype.name)
print("size: ",a.size)

print("type: ",type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])      # reshap olmadan da bu şekildede 3e 4'lük bir matrise çevrilir
array1     

zeros = np.zeros((3,4))          # 0'lardan oluşan 3'e 4'lük bir matris
zeros

zeros[0,0] = 5                    # ilk değerini 5 yaptık
print(zeros)

np.ones((3,4))                      # 1lerden oluşan bir matris yarattık

np.empty((2,3))                    # 2ye 3lük boş bir array

a = np.arange(10,50,5)            # 10 ile 50 arası 5'er 5'er artan bir array 
print(a)

a = np.linspace(10,50,20)            # 10'dan 50'ye sayılar 20 tane sayı üret--üretir
print(a)



# numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))                # sinüsünü alır

print(a<2)                     # sonucu true false döner


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

# element wise prodcut  ---- 1le 1'i çarp,2 ile 2'yi çarp vs demek--- çarpımları sonucu 2ye 2lik bir matrise dönüşür
print(a*b)

# matrix prodcut   -- matrislerin çarpımını yaptık
a.dot(b.T)             # b'nin transpozunu alırsak tamamlanır

print(np.exp(a))

a = np.random.random((5,5))         # 5e 5llik bir random oluşturur
print(a)

print(a.sum())
print(a.max())
print(a.min())


print(a.sum(axis=0))   #kolonları/sütunları alt alta hepsini toplar
print(a.sum(axis=1))   #satırları yan yana toplar

print(np.sqrt(a))   #karekökünü alır 
print(np.square(a)) # a**2---- karesini alır


print(np.add(a,a))    # a ile a'yı topluyoruz



# indexing and slicing
array = np.array([1,2,3,4,5,6,7])   #  vector dimension = 1

print(array[0])

print(array[0:4])

reverse_array = array[::-1]  # arrayi tersine çevirir. çıktısı:  [7 6 5 4 3 2 1]

print(reverse_array)

array[::2]        # çıktısı:  array([1, 3, 5, 7])
array[::-2]       #çıktısı:    array([7, 5, 3, 1])

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1)

print(array1[1,1])

print(array1[:,1])       # çıktısı: [2 7] ---- satırların hepsini al. sütunlardan 1. olanı al


print(array1[1,1:4])    # 1.satırı full al 1sütundan 4.sütuna kadar al   çıktısı:  [7 8 9]


print(array1[-1,:])    # sondan 1. satırı ve tüm sütunları al  çıktısı :  [ 6  7  8  9 10]
print(array1[:,-1])    # tüm satırları al ve sondan tüm sütunu al .  çıktısı:  [ 5 10]    



# shape manipulation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])      # 3'e 3'lük bir array
print(array)

# flatten       !!!!! ÖNEMLİ 
a = array.ravel()               # array'i düz hale getirdik(bir vektör haline) çıktısı: [1 2 3 4 5 6 7 8 9]
print(a)

array2 = a.reshape(3,3)       # 3'e 3lük bir matrise çevirme
print(array2)

arrayT = array2.T          #transpozunu alıyoruz. 
print(arrayT)
print(arrayT.shape)          # çıktısı: (3, 3) olur


array5 = np.array([[1,2],[3,4],[4,5]])   #3satır 2 sütundan oluşan bir arraydir
print(array5)

print(array5.reshape(2,3))              # 2 satır 3 satırdan oluşan bir arraye çevirdik

print(array5.resize(2,3))
# array5 = np.column_stack((array1,array1))



# stacking arrays--- arrayleri birleştirme öğreneceğiz

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# veritical    - dikey birleştirme
#array([[1, 2],
#       [3, 4]])
#array([[-1, -2],
#       [-3, -4]])
array3 = np.vstack((array1,array2))        # dikey olarak birleştirir
print(array3)

# horizontal    - yatay birleştirme
#array([[1, 2],[-1, -2],
#       [3, 4]],[-3, -4]]

array4 = np.hstack((array1,array2))         # yatay olarak birleştirir
print(array4)



# convert and copy

liste = [1,2,3,4]   # list
print(liste)

array = np.array(liste) #np.array     ---- listeden arraya geçme 
print(array)

liste2 = list(array)                 # ---- arrayen listeye geçme
print(liste2)
type(liste2)

a = np.array([1,2,3])
print(a)

b = a                # b değiştirince a ve c de değişiyor. Ne alakaaaa? çünkü memoryde aynı alan ayrılyor.
print(b)             # çözümü copy ile yapılması. çünkü copy ile hepsine yeni alan ayrılır- birisini değiştirince diğerleri bundan etkilenmez

b[0] = 5                # 0.elemanı 5 ile değiştirme
print(b)

c = a
print(c)


d =  np.array([1,2,3])
print(d)

e = d.copy()                        # d arrayini e değişkenine kopyaladık
print(e)

f = d.copy()                       # d arrayini f değişkenine kopyaladık

print(f)
