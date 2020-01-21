class Vehicle:
    def __init__(self):
        self.main_color = ""
        self.maximum_occupancy = ""

    def drive(self):
        print("Vroooom!")

    def turn(self, direction):
      self.direction = direction
      print (f"watch out were turning {self.direction}!")

    def stop(self):
      print ("STOPPING!!!!")