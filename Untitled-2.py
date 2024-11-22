class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def honk(self):
        print("Beep beep!")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size

    def rev_engine(self):
        print("Vroom vroom!")

car1 = Car("Toyota", "Camry", 2023, 4)
motorcycle1 = Motorcycle("Honda", "CBR1000RR", 2022, 1000)

print(car1.get_info())
car1.honk()
print(motorcycle1.get_info())
motorcycle1.rev_engine()