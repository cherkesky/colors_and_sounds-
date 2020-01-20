# Practice: Custom Colors and Sounds

# Define 5 of your favorite vehicles
car1 = {"make": Porsche, "color": "Black", top_speed=140 }
car2 = {"make": Jaguar, "color": "Gray", top_speed=100 }
car3 = {"make": Audi, "color": "Red", top_speed=110}
car4 = {"make": BMW, "color": "White", top_speed=120}
car5 = {"make": Subaru, "color": "Blue", top_speed=200}

# Move all common properties in your vehicles to a new Vehicle class.
# Create an instance of each vehicle.
# Define a different value for each vehicle's properties.
# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# Make your vehicle instances perform all three behaviors.