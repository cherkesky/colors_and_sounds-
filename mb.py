from vehicle import Vehicle

# Gas powered truck
class MB(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0
    
    def drive(self):
        print("Slick cool riding. Yehheee!")