# kapsülleme/ encapsulation ----> metot yada variable'lara doğrudan erişimi kısıtlamak

class BankAccount(object):                           # class yarattık 
    
    def __init__(self, name, money, address):            # init metodu, constructur yarattık
        self.name1 = name
        self.money1 = money
        self.address1 = address
        
        
p1 = BankAccount("messi", 1000, "barcelona")                  # kişileri yarattık
p2 = BankAccount("neymar", 2000, "paris")                 

print(p1.name1, p1.money1, p1.address1)
print(p2.name1, p2.money1, p2.address1)


# diyelim ki messinin parasını sıfırlayıp neymara aktarmak istiyoruz

p2.money1 = p2.money1 + p1.money1      # 2000 + 1000  # neymarın parasına messinin parasını ekledik
p1.money1 = 0                          # messinin parasını sıfırladık
print("neymar new money: ", p2.money1)
print("messi new money: ", p1.money1)

# bu yukarıdaki işlemler mantıklı değil çünkü banka hesabından aktarma olmamalı
#----------------------------------------------------------------------------------
# KAPSÜLLEME BURADA DEVREYE GİRER

# KAPSÜLLEME: classlara, attribute'lara, variable'lara dışarıdan erişimin kısıtlanmasıdır. PRİVATE yapmamız gerekiyor

# attributeleri yaratırken __ (iki altçizgi) koyarsak o attribute artık private olmuş oldu


class BankAccount(object):                           # class yarattık 
    
    def __init__(self, name, money, address):            # init metodu, constructur yarattık
        self.name1 = name
        self.__money1 = money                        # __ ile private yapmış olduk
        self.address1 = address
        
        
p1 = BankAccount("messi", 1000, "barcelona")                  # kişileri yarattık
p2 = BankAccount("neymar", 2000, "paris")           


print(p1.name1)
print(p1.__money)        # AttributeError: 'BankAccount' object has no attribute '__money'
print(p1.address1)       
print(p2.name1, p2.money1, p2.address1)      # AttributeError: 'BankAccount' object has no attribute 'money1'

# __money değişkenini çağırdık ancak AttributeError aldık. 
# Aslında bu şekilde bir objeye sahibiz ama private artık olduğu için erişim yoktur ve DEĞİŞTİRİLEMEZ 

#--------------------------------------------------------------------------------------------------

# Peki bir şekilde banka hesabına erişmemiz lazım bunu nasıl sağlarız?
# attribute'leri alabilmemiz için GET ve SET metotlarını kullanırız


class BankAccount(object):                           # class yarattık 
    
    def __init__(self, name, money, address):            # init metodu, constructur yarattık
        self.name1 = name               # global/public variable
        self.__money1 = money           # private variable
        self.address1 = address
        
    # get ve set global/ public 
    def getMoney(self):     # object içerisinde bulunan money variable'ını almak/ erişim sağlamak istiyorum
        return self.__money1   # miktarı aldık/eriştik
    
    def setMoney(self, amount):  #  object içerdeki money variable'ını set etmek düzenlemek istiyorum
        self.__money1 = amount   #  dışarıdan gelen miktar eşitle
        
    # private
    def __increase(self):        # private metot yaptık
        self.__money1 = self.__money1 + 500              # 500'lük bir zam yapmak istiyoruz
        
        
p1 = BankAccount("messi", 1000, "barcelona")                  # kişileri yarattık
p2 = BankAccount("neymar", 2000, "paris")      

print("messi para mikt: ", p1.__money1)  # get metodu olmadan erişim sağlayamayız
print("get method: ", p1.getMoney())   #messinin ne kadar parası var ona bakıyoruz. çıktısı: get method:  1000

p1.setMoney(5000) # parayı set ettik. yeni miktarı 5000 olarak güncelledik
print("after set money: ", p1.getMoney())     # set ettikten sonra money'i getir dedik. 
                                              # çıktısı:after set money:  5000


p1.increase()                               # zam yaptık
print("after raise: ", p1.getMoney())       #çıktısı: after raise:  5500

# zammı private yaptık yukarıdaki işlemlerden sonra öncesinde public'di

p1.__increase()                                 # __increase() metodunu bulamadı neden??? çünkü private :)
print("after private increase: ", p1.getMoney())