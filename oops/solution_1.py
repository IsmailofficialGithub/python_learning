print('Create a Car class with attributes like brand , model, then create an instane of this class')

class Car:
    # __init__ = constructor = first function calls in class 
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model


my_car = Car("Toyota","Corolla")

print(my_car.model)
print(my_car.brand)

my_new_car=Car('Suzuki','Mehran')
print(my_new_car.brand)
print(my_new_car.model)
