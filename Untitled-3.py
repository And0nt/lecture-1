class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 50
        self.mood = 50
        self.health = 100

    def eat(self):

class Student(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.money = 1000
        self.knowledge = 50
        self.fatigue = 0
        self.courses = []

    def study(self):
        self.knowledge += 10
        self.fatigue += 5

    def work(self):
        self.money += 50
        self.fatigue += 10

    def rest(self):
        self.fatigue -= 10

    def live_a_day(self):

student = Student("Іван", 20)

for day in range(365):
    student.live_a_day()