# AREA AND PERIMETER OF SQUARE AND CIRCLE

from abc import ABC, abstractmethod

#inheritance 
class Shape(ABC):        # parent class
    
    #abstracted method
    @abstractmethod          # convert area to abstractedmethod
    def area(self):          # area
        pass
     
    @abstractmethod          # convert perimeter to abstractedmethod
    def perimeter(self):     # perimeter
        pass
    
    # overriding and polimorphism
    def toString(self):
        pass
    
class Square(Shape):         # child class
    
    def __init__(self, edge):    # edge of the square
        self.__edge = edge       # make private (encapsulation/ private attribute)
        
    def area(self):                        # area of square  -- since abstractedmethod has been defined before, it needs to be written here as well.
        result = self.__edge ** 2          # area = edge ** 2
        print("Square area: ", result)     # print result
        
    def perimeter(self):                    # perimeter of square -- since abstractedmethod has been defined before, it needs to be written here as well.
        result = self.__edge * 4            # perimeter = edge * 4
        print("Square perimeter: ", result) # print result

    def toString(self):                     # overriding and polimorphism    
        print("Square edge: ", self.__edge)  # print edge
        

class Circle(Shape):         # child class
    
    PI = 3.14                # constant variable -- value whose result will not change
    
    def __init__(self, radius):  # radius of the Circle
        self.__radius = radius   # make private (encapsulation/ private attribute)
        
    def area(self):                            # area of circle -- since abstractedmethod has been defined before, it needs to be written here as well.
        result = self.PI * self.__radius**2    # circle = PI * radius**2
        print("Circle area: ", result)         # print result
        
    def perimeter(self):                       # perimeter of circle -- since abstractedmethod has been defined before, it needs to be written here as well.
        result = 2 * self.PI * self.__radius   # perimeter = PI * radius
        print("Circle perimeter: ", result)    # print result
        
    def toString(self):                         # overriding and polimorphism
        print("Circle radius: ", self.__radius)  # print radius
        



s = Square(4)      # call class and create an object
s.area()           # result -> area of square with area() method
s.perimeter()      # result -> perimeter of circle with perimeter() method
s.toString()       # print square edge value

print("---------------------------")

c = Circle(3)       # call class and create an object
c.area()            # result -> area of circle with area() method
c.perimeter()       # result -> perimeter of circle with perimeter() method
c.toString()        # print circle edge value





