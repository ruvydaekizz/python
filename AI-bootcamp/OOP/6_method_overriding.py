# overriding: geçersiz kılma olarak adlandırılır

class Animal:   # parent/ superclass

    def toString(self):
        print("animal")
        
class Monkey(Animal):   # child/ subclass --- monkey animal'ın bir alt kümesi
    
    def toString(self):
        print("monkey")
         
a1 = Animal()     # animal1 yarattık
a1.toString()     # animal1'in toString metoduna ulaştık-- çıktısı: animal olur


m1 = Monkey()   # monkey1 yarattık
m1.toString()   # monkey1'in toString metoduna ulaştık-- çıktısı: monkey olur
                # monkey calls overriding methods  -- parent'ın toString'ini değil de kendi toString metodunu çağırır



