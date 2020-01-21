from vehicle import Vehicle

# Electric car
class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def drive(self):
        print("I'm an electric super car Zoooooooooooom!")

    def turn(self, direction):
      self.direction = direction
      print (f"This Tesla is turning {self.direction} watch out!")

    def stop(self):
      self.direction = direction
      print (f"This Tesla is STOPPING watch out!")