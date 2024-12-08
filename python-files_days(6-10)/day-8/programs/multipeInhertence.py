class Mammal:
    def mammal_info(self):
        print(f'Mammals can give direct birth')
    def same(self):
        print(f'in mammal')

class WingedAnimal:
    def WingedAnimal_info(self):
        print(f"winged animal can flap")
    def same(self):
        print(f'in Winged')

class Bat(WingedAnimal,Mammal):
    pass

b1 = Bat()
b1.mammal_info()
b1.WingedAnimal_info()
b1.same()
# multilevel inheritence
class SupperClass:
    def supper_method(self):
        print(f'Super class method called')


class DerivedClass1(SupperClass):
    def derived_medthod1(self):
        print(f'Derived class 1 method called')

class DerivedClass2(DerivedClass1):
    def derived_medthod2(self):
        print(f'Derrived class 2 method called')


d2 = DerivedClass2()
d2.supper_method()
d2.derived_medthod1()
d2.derived_medthod2()



