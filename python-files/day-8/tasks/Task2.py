class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"Animal named {self.name} is eating and is of {self.age} years old")

class Dog(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,name,age)
    
    def bark(self):
        print(f"Woof {self.name} this side")

class Cat(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,name,age)
    def meow(self):
        print(f"Meow {self.name} this side")

dog1 = Dog("tommy",5)
cat1 = Cat("kitty",7)

dog1.bark()
dog1.eat()

cat1.meow()
cat1.eat()

'''
Ques1->
Using Inheritence in this example led code simpilar
as redundant code for eat is common for both
cat and the dog so a common animal parent class can 
contain all the common traits methods a animal can have 
and the child class will only have the methods and data unique 
to that animal

Ques-2->
calling the eat() method calls the eat method of the animal class
as cat does not have a eat method of its own so
the method is inherited from the parent class
'''

