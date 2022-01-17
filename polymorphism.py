class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print("Details:",self.name,self.color,self.price)

    def max_speed(self):
        print("Vehicle's Maximun speed is 480 km/hr")

    def change_gear(self):
        print("Vehicle's can change upto 6 gears")

class Car(Vehicle):
    def max_speed(self):
        print("Car's maximim speed is 890 km/hr")

    def change_gear(self):
        print("Car can change upto 7 gears")

Car = Car("tesla ","black",9649664)
Car.show()
Car.max_speed()
Car.change_gear()

print("\n")
Vehicle = Vehicle("royal Enfild","olive green", 760954)
Vehicle.show()
Vehicle.max_speed()
Vehicle.change_gear()
