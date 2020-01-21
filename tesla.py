from vehicle import Vehicle

# Electric car
class Tesla(Vehicle):
    def __init__(self):

        """
        This a Tesla.
        """
        self.battery_kwh = 0

    def drive(self):
        print("I'm an electric super car Zoooooooooooom!")