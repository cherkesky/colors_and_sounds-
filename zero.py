from vehicle import Vehicle

class Zero(Vehicle):
  def __init__ (self):
    self.battery_kwh = 0
  def drive(self):
    print ("Coooool electric motorcycle Nwwwwwwwwweeeee")

  def turn(self, direction):
    self.direction = direction
    print (f"This Zero is turning {self.direction} watch out!")

  def stop(self):
    print (f"This Zero is STOPPING watch out!")