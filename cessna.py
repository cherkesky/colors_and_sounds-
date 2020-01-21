from vehicle import Vehicle

class Cessna(Vehicle):
  def __init__ (self):
    self.fuel_capacity = 0
  def drive(self):
        print("I'm in my Cessna!!!")

  def turn(self, direction):
    self.direction = direction
    print (f"This Cessna is turning {self.direction} watch out!")

  def stop(self):
    self.direction = direction
    print (f"This Cessna is STOPPING duck!")