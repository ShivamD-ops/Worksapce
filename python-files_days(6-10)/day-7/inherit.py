# Inheritence

# Parent Class

class Person:
    def __init__(self,emp_name,emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def getInfo(self):
        print(self.emp_name, " " , self.emp_id)
per1 = Person("SD",12)
per1.getInfo()
class Employee(Person):
    def __init__(self,emp_name,emp_id,emp_salary,emp_designation):
        self.emp_salary = emp_salary
        self.emp_designation = emp_designation

        Person.__init__(self,emp_name,emp_id)


    def getEmpoyee(self):
        print(f"employee name is {self.emp_name}")
        print(f"employee emp ID is {self.emp_id}")
        print(f"employee Salary is {self.emp_salary}")
        print(f"employee Designation is {self.emp_designation}")

# creating object

emp1 = Employee("sam",1,10000,"SDE")    
emp1.getEmpoyee()    
