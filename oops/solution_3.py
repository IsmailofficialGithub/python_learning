print("Inheritance : Create a Eletric Car class that inherit from the Car class and has an additional attribute battery_size")

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar (Car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery=battery

        
        

my_car=Car('Toyota','Corolla')
my_electric_car=ElectricCar("Tesla","Eve1","10kwm")

print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.full_name())
# print(my_car.model)
# print(my_car.full_name())
        
        