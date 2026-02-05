class Person:
    def __init__(self, name, money, mood="neutral", healthRate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self._healthRate = healthRate  # Use property
    
    @property
    def healthRate(self):
        return self._healthRate
    
    @healthRate.setter
    def healthRate(self, value):
        if 0 <= value <= 100:
            self._healthRate = value
        else:
            self._healthRate = max(0, min(100, value))
    
    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"
    
    def eat(self, meals):
        if meals >= 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
    
    def buy(self, items):
        self.money -= items * 10