class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def info(self):
        print(f'make-> {self.make} \nmodel-> {self.model} \nyear-> {self.year}')
    
    def update_model(self,new_model):
        self.model = new_model

new_car = Car("India","Tata Alteroz", "2024")
new_car.info()
#to update model create new method in class Car
# def update_model(Self,new_model):
        # self.model = new_model
new_car.update_model("Tata Harrier")
new_car.info()
