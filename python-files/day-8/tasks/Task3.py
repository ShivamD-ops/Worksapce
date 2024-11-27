from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        Shape.__init__(self,"Circle")
    def area(self):
        return (22/7)*(self.radius**2)
    

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        Shape.__init__(self,"Rectangle")
    def area(self):
        return self.length*self.width

def print_area(Shape):
    print(f"area of {Shape.name} is {Shape.area()}")

circle1 = Circle(5)
rectangle1 = Rectangle(5,4)

print_area(circle1)
print_area(rectangle1)

'''
Ques1->
as print_area takes shape as input
and shape(parent of circle and rectangle) has
both atribute name and area it works
also name is initiated in the both child classes
and area is overrided thus pollymorphism allows


Ques2->
Followin error occurs if we do not create area function in Rectangle Class
    rectangle1 = Rectangle(5,4)
TypeError: Can't instantiate abstract class Rec
tangle without an implementation for abstract m
ethod 'area

'''
