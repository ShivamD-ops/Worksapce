class Bike:
    name = ""
    gear = 0

new_bike = Bike()
new_bike.name = "Honda"
new_bike.gear = 4

print(f"Name: {new_bike.name}, gear: {new_bike.gear}")

class Employee:
    emp_id = 0

emp_obj1 = Employee()
emp_obj2 = Employee()

emp_obj1.emp_id = 1001
emp_obj2.emp_id = 1002

print(f'Employee ID: {emp_obj1.emp_id}')

print(f'Employee ID: {emp_obj2.emp_id}')

class Room:
    length: 0.0
    breadth: 0.0

    def calculate_area(self):
        print(f"Area of Room = {self.length * self.breadth}")

study_room = Room()
study_room.length = 34
study_room.breadth = 30.45
study_room.calculate_area()

class Car:
    name = ""
    def __init__(self,name="",gear = 0):
        self.name = name
        self.gear = gear

c1 = Car("Honda",4)
print(c1.name, " ", c1.gear)




