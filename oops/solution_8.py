print('Use isinstance() to check if my_electric is instance of Car and ElectricCar')




class Car:
    total_car=0

    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def getter_brand(self):
        return f"{self.__brand} !"
    
    def setter_brand(self,brand):
        self.__brand=brand
        return brand
    def fuel_type(self):
        return f"{self.__brand} {self.__model} fuel type is 'Petrol or Diesel' "
    @staticmethod
    def general_description ():
        return "Car are mean of transport"
    @property
    def model(self):
        return self.__model
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def fuel_type(self):
        return f"{self.getter_brand()} {self.model} fuel type is 'Electric Fuel'"

    

        
        
my_car=Car('Honda',"Corolla")
my_electric=ElectricCar("Tesla","Eve1","10kwm")

print(isinstance(my_electric,Car))
print(isinstance(my_electric,ElectricCar))

        
        