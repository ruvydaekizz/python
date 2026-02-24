# CALCULATOR

class Calculator(object):      # create a class
    "Calculator"               # docstring
    
    # initialize method
    def __init__(self, a, b):
        "Initialize values"
        
        # attributes 
        self.first_value = a
        self.second_value = b
    
    # addition method
    def add(self):
        "addition a+b= result -> return result " 
        return self.first_value + self.second_value       # return additional result 
    
    # subtraction method
    def subtraction(self):
        "subraction a-b= result -> return result"
        return self.first_value - self.second_value       # return subtraction result
    
    # multiply method
    def multiply(self):
        "multiplication a*b= result -> return result"
        return self.first_value * self.second_value       # return multiply result
    
    # division method
    def division(self):
        "division a/b = result -> return result"
        return self.first_value / self.second_value       # return division result
    
    
print("Enter add(1), subtraction(2), multiply(3), division(4)")  # user choose which action they want to take
select = input("Select 1 or 2 or 3 or 4: ")

first_v1 = int(input("Enter first value: "))      # get the first value from the user
second_v2 = int(input("Enter second value: "))    # get the second value from the user


result = Calculator(first_v1, second_v2)       # call class and create an object

if select == "1":                            # if user choose 1 -> additional 
    add_result = result.add()
    print("Add: {}".format(add_result))

elif select == "2":                          # if user choose 2 -> subtraction
    subt_result = result.subtraction()
    print("Subtraction: {}".format(subt_result))
    
elif select == "3":                          # if user choose 3 -> multiply 
    mult_result = result.multiply()
    print("Multiply: {}".format(mult_result))

elif select == "4":                          # if user choose 4 -> division
    divi_result = int(result.division())
    print("Division: {}".format(divi_result))
    
else:                                        # if user choose another value -> show error message
    print("ERROR!!! There is no proper selection!")


    
    