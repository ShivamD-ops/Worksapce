#encapsulation 
#__ represents private attribute

#base class
class Base:
    def __init__(self):
        self.a = "Encapsulation Done"
        self.__c = "learing oops"

# Derived class
class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        print("calling private attribute")
        print(self.__c)
    
obj1 = base()
print(obj.a)
# print(obj.__c)
obj2 = Derived()


