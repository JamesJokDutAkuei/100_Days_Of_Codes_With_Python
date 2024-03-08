import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        
    @property
    def radius(self):
        return self.__radius
        
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius can't be negative")
        else:
            self.__radius = value 
    
    def area(self):
        return math.pi * (self.__radius ** 2)
        
        

circle1 = Circle(34)

print(circle1.radius)

circle1.radius = 10

print(circle1.radius)

print(circle1.area())
        
        
        
        
