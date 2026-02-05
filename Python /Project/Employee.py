class Employee(Person):
    def __init__(self, name, money, id, email, salary, distanceToWork, car=None):
        super().__init__(name, money)
        self.id = id
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        self.car = car
    
    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"
    
    def drive(self, distance):
        if self.car:
            self.car.run(self.car.velocity or 60, distance)
    
    def refuel(self, gasAmount=100):
        if self.car:
            self.car.fuelRate += gasAmount
    
    