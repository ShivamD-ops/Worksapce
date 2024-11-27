class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f" i am a cat My name is {self.name}, i am {self.age} years old")

    def make_sound(self):
        print("Meaow")
    
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f" i am a Dog My name is {self.name}, i am {self.age} years old")

    def make_sound(self):
        print("BArk")

cat1 = Cat("abc",9)
dog1 = Dog("def",2)

cat1.info()
cat1.make_sound()

dog1.info()
dog1.make_sound()
for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
        