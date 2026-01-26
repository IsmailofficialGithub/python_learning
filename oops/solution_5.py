print("Polymorphism : Polymorphism  by defining a method fuel_type for both Car and ElectricCar but different behavours")


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
    def fuel_type(self):
        return f"{self.__brand} {self.model} fuel type is 'Petrol or Diesel' "
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def fuel_type(self):
        return f"{self.getter_brand()} {self.model} fuel type is 'Electric Fuel'"

    

        
        

my_car=Car('Toyota','Corolla')
my_electric_car=ElectricCar("Tesla","Eve1","10kwm")

print(my_electric_car.fuel_type())
print(my_car.fuel_type())

        
        