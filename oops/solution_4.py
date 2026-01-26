print("Encapsulation : Modify the Car class to encapsulate the brand attribute , making it private and provide a getter method of it ")

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def getter_brand(self):
        return f"{self.__brand} !"
    
    def setter_brand(self,brand):
        self.__brand=brand
        return brand
    
class ElectricCar (Car):
    def __init__(self,__brand,model,battery):
        super().__init__(__brand,model)
        self.battery=battery

        
        

my_car=Car('Toyota','Corolla')
my_electric_car=ElectricCar("Tesla","Eve1","10kwm")

print(my_car.setter_brand('Mustang'))
print(my_car.getter_brand())

        
        