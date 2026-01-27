print('Add a class variable to car that keeps track of the number of cars created')



class Car:
    total_car=0

    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.total_car+=1

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

    

        
        

Car('Toyota','Corolla')
ElectricCar("Tesla","Eve1","10kwm")

print(Car.total_car)

        
        