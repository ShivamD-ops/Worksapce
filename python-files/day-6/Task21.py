class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        print(f"area of {self.name} is calculated using integration and this is base class")


class Circle(Shape):
    def __init__(self,radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        super().area()
        return (22/7)*(self.radius**2)
new_circle = Circle(2)
print(new_circle.area())

# we can call the parent from child after method overloadig using super()