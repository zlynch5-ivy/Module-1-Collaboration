# Created by Zach Lynch
# Code below takes information related to a user's vehicle, and lists it neatly in separate rows.

print("CAR SPECIFICATIONS:")
v_type = input("What kind of vehicle is it? (Truck, Sedan, SUV, etc.)")
maker = input("What company created the car? (Toyota, Ford, Chevy, etc.)")
model = input("What is the model name of the vehicle?")
year = input("When was the car created?")
doors = input("How many doors does the car have?")
roof = input("What type of roof does the car have?")

class Vehicle:
    def __init__(self, v_type):
        self.v_type = v_type

class Automobile(Vehicle):
    #Information given at the beginning is separated into a class
    def __init__(self, v_type, year, maker, model, doors, roof):
        super().__init__(v_type)
        self.year = year
        self.maker = maker
        self.model = model
        self.doors = doors
        self.roof = roof

my_car = Automobile(v_type, year, maker, model, doors, roof)
print(f"\n ---Car Details---")
print(f"""
      Vehicle Type: {my_car.v_type}
      Year: {my_car.year}
      Make: {my_car.maker}
      Model: {my_car.model}
      Number of Doors: {my_car.doors}
      Type of Roof: {my_car.roof}
      Type of Vehicle: {my_car.v_type}
""")