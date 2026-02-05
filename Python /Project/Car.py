class Car:
    def __init__(self, name, fuelRate=100, velocity=0):
        self.name = name
        self._fuelRate = fuelRate
        self._velocity = velocity
    
    @property
    def fuelRate(self):
        return self._fuelRate
    
    @fuelRate.setter
    def fuelRate(self, value):
        self._fuelRate = max(0, min(100, value))
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self, value):
        self._velocity = max(0, min(200, value))
    
    def run(self, velocity, distance):
        self.velocity = velocity
        # Fuel decreases 10% every 10km
        fuel_needed = (distance // 10) * 10
        
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            # Calculate how far we can go
            possible_distance = (self.fuelRate // 10) * 10
            remain = distance - possible_distance
            self.fuelRate = 0
            self.stop(remain)
    
    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"Stopped! Remaining distance: {remain_distance} km")
        else:
            print("Arrived at destination!")