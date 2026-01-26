print('Add a method into car that display full name of car (brand,model)')

class Car :
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"


        
mycar=Car('Toyota','Corolla')
print(mycar.brand)
print(mycar.model)


print(mycar.full_name())