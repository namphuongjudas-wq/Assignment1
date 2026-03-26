import random
car_list = []
class car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * hours)
for i in range(1, 11):
        brand_new_car = car(f"ABC-{i}", random.randint(150, 200))
        car_list.append(brand_new_car)
finish = False
while not finish:
    for race_car in car_list:
       race_car.accelerate(random.randint(-10, 15))
       race_car.drive(1)
       if race_car.travelled_distance >= 10000:
            finish = True 
for c in car_list:
    print(f"{c.registration_number} | {c.maximum_speed} | {c.current_speed} | {c.travelled_distance} km")