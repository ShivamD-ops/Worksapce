class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
    
    def perimetre(self):
        return 2 * (self.__length + self.__width)


rect = Rectangle(5,6)

print(f'area -> {rect.area()}')
print(f'perimetre -> {rect.perimetre()}')




