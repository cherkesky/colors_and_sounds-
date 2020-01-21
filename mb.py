from vehicle import Vehicle

# Gas powered truck
class MB(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0
    
    def drive(self):
        print("Slick cool riding. Yehheee!")

    def turn(self, direction):
      self.direction = direction
      print (f"This MB is turning {self.direction} watch out!")

    def stop(self):
      self.direction = direction
      print (f"This MB is STOPPING watch out!")