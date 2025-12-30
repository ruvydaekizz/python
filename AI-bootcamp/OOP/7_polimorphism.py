# polimorphism: çok şekillilik, çok biçimlilik

# superclasstan subclassa'a kalıtım yoluyla(inheritance) aktarılan ama subclass'ta farklı şekilde kullanılan metotlar varsa buna polimorphism denir

#örnek
# parent class: employee -- z metodu ile her sene zam yapmak istiyoruz %0.1 
# child class: computer engineering -- z metodu ile her sene zam yapmak istiyoruz %0.2
# child class: EE engineering -- z metodu ile her sene zam yapmak istiyoruz %0.3

#bunu overriding ile kullanmıştık. metot aynı ama içindeki oranlar farklı, kullanım şekilleri farklı buna polimorphism denir

class Employee:  # superclass

    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * 0.1
        print("Employee: ", result)


class CompEng(Employee): # subclass

    def raisee(self):
        raise_rate = 0.2             # miktarı farklı yukarıdaki metotan bu konsepte polimorphism denir
        result = 100 + 100 *0.2
        print("CompEng: ", result)
        
        
class EEE(Employee):     # subclass
    
    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * 0.3        # miktarı farklı yukarıdaki metotan bu konsepte polimorphism denir
        print("EEE: ", result)
        
e1 = Employee()   # employee objesi yarattık
e1.raisee()                                       # çıktısı   110.0 olur

ce = CompEng()   # compEng objesi yarattık
ce.raisee()                                      # çıktısı 120.0 olur

eee = EEE()     # EEE objesi yarattık
eee.raisee()                                     # çıktısı 130.0 olur


# 3 tane aynı metot farklı raise_rate'ler kullanarak aynı bilgiyi farklı dallar için yazdıracak
 
employee_list = [e1, ce, eee]    # bir liste oluşturduk. içinde tanımladığımız objeler var

for employee in employee_list:
    employee.raisee()
        
