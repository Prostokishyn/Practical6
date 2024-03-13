class Vehicle():
    def __init__(self, brand):
        self.brand=brand
    def start_engine(self):
        print("engine started")
       
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model=model
    def start_engine(self):
        print("car engine started")
   
class Motorcycle(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type=type
    def start_engine(self):
        print("motorcycle engine started")
       
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def charge_battery(self):
        print("battery charging")
       
class Garage:
    def __init__(self):
        self.vehicles = []
    def start_all_engines(self):
        for vehicle in self.vehicles:
            vehicle.start_engine()
           
garage = Garage()
audi = Car('Audi', 'Q8')
honda = Motorcycle('Honda', 'Rebel1100')
tesla = ElectricCar('Tesla','Model X')
garage.vehicles.append(audi)
garage.vehicles.append(tesla)
garage.vehicles.append(honda)
garage.start_all_engines()