class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f'Animal speaking {self.name} (in class parent)')

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def bark(self):
        print(f'{self.name} Dog barking in dog class')
    def speak(self):
        print(f'i am {self.name} and i am a Dog in dog class parent method overloaded')

new_dog = Dog("Tiger")
new_dog.bark()
new_dog.speak()
# we can do function overloading in dog 
# by declraing similar name method in the Dog Class
# i.e. declaring speak method in dog class again
#other than animal

    