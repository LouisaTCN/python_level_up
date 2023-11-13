class Vehicle():
    def __init__(self, steering_type, colour, make, model):
        self.steering = steering_type
        self.colour = colour
        self.make = make
        self.model = model

    def move(self):
        print(f"The{self.model}{self.make} is moving")

    def start(self):
        print(f"You have started the {self.model}{self.make}")

    def stop(self):
        print(f"You have stopped the {self.model}{self.make}")




class Car(Vehicle):
    def __init__(self, steering_type, colour, make, model, registration_number, horsepower):
        self.registration_number = registration_number
        self.hosepower = horsepower

    Vehicle.__init__(self, steering_type, colour, make, model)

    def handbrake_turn(self):
         print(f"The {self.model}{self.make} is drifting with handbrake turn")
###**** line 25 needs correcting!******

