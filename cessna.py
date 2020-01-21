from vehicle import Vehicle

class Cessna(Vehicle):
  def __init__ (self):
    self.fuel_capacity = 0
  def drive(self):
        print("I'm in my Cessna!!!")