from abc import ABC,abstractmethod

# Abstract class Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

# Car Class inherited from Vehicle
class Car(Vehicle):
    def __init__(self,name,year):
        self.name = name
        self.year = year
    def start(self):
        print(f"Car named {self.name} started")
    def stop(self):
        print(f"Car named {self.name} stopped")
    def drive(self):
        print(f"Car named {self.name} is driving")

#Bike Class inherited from Vehicle
class Bike(Vehicle):
    def __init__(self,name,year):
        self.name = name
        self.year = year
    def start(self):
        print(f"Bike named {self.name} started")
    def stop(self):
        print(f"Bike named {self.name} stopped")
    def drive(self):
        print(f"Bike named {self.name} is driving")

# Driver code

car1 = Car("Audi R8",2024)
bike1 = Bike("Royal Enfield",2022)

car1.start()
car1.drive()
car1.stop()

bike1.start()
bike1.drive()
bike1.stop()

# veh = Vehicle()
# veh.start()

'''
Question-1->
vehicle class is a abstract class as 
it provides a common base class for vehicles
but it cant be initiolized on its own
while it provides abstract methods
for its sub classes.
NonImplementedError is raised to indicate
that implementation is incomplete.


Question-2->
Program gives the following error
if we do not implement start() in car
and calls it anyway
TypeError: Can't instantiate abstract cla
ss Car without an implementation for abst
ract method 'start'
'''




