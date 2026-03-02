# calculator project
# class -> init -> method-attribute -> function vs method öğrendik

class Calculator(object):
    "calculator"                 # docstring
    
    # init metodu 
    def __init__(self, a, b):          # a ve b parametresini alsın
        "initialize values"
        # içerisinde attributeler olacak
        self.value1 = a
        self.value2 = b
        # pass    --  def içinde hiçbirşey yazmazsa kullanılır  
    
    #toplama metodu
    def add(self):
        "addition a+b= result -> return result "      # docstring
        return self.value1 + self.value2 
        
    
    
    #çarpma metodu
    def multiply(self):
        "multiplication a*b= result -> return result"
        return self.value1 * self.value2

v1 = 5
v2 = 3
c1 = Calculator(v1, v2)       # yeni bir hesap makinesi yarattık.  a ve b değerlerine v1 ve v2 değerlerini atadık, yarattık
add_result = c1.add()               # add metodunu çağırdık
multiply_result = c1.multiply()     # multiply metodunu çağırdık

print("Add: {}, Multiply: {}".format(add_result, multiply_result))   # print'in format ile kullanımı

#-----------------------------------------------------------------------
# değerleri kullanıcıdan input alarak yapalım

class Calculator(object):
    "calculator"                 # docstring
    
    # init metodu 
    def __init__(self, a, b):          # a ve b parametresini alsın
        "initialize values"
        # içerisinde attributeler olacak
        self.value1 = a
        self.value2 = b
        # pass    --  def içinde hiçbirşey yazmazsa kullanılır  
    
    #toplama metodu
    def add(self):
        "addition a+b= result -> return result "      # docstring
        return self.value1 + self.value2 
    
    #çarpma metodu
    def multiply(self):
        "multiplication a*b= result -> return result"
        return self.value1 * self.value2
    
    #bölme metodu
    def divison(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2


print("Choose add(1), multiply(2), divison(3)")
selection = input("select 1 or 2 or 3: ")            # hangi işlemi yapmak istediğini seç

v1 = int(input("enter first value: "))
v2 = int(input("enter second value: "))
    

c1 = Calculator(v1, v2)       # yeni bir hesap makinesi yarattık

if selection == "1":
    add_result = c1.add()               # add metodunu çağırdık
    print("Add: {}".format(add_result))
elif selection == "2":
    multiply_result = c1.multiply()     # multiply metodunu çağırdık
    print("Multiply: {}".format(multiply_result))
elif selection == "3":
    division_result = c1.divison()
    print("Divison: {}".format(division_result))
else: 
    print("ERROR!!! There is no proper selection")    
