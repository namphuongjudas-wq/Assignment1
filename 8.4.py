import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def change_speed(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            speed_change = random.randint(-15, 15)
            car.change_speed(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'-'*70}")
        print(f"{'Biển số'} | {'Tốc độ tối đa'} | {'Tốc độ hiện tại'} | {'Quãng đường (km)'}")
        print(f"{'-'*70}")
        for car in self.car_list:
            print(f"{car.registration_number} | {car.max_speed} | {car.current_speed} | {car.travelled_distance}")
        print(f"{'-'*70}")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True
        return False



if __name__ == "__main__":

    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200) 
        cars.append(Car(f"ABC-{i}", max_speed))
    derby = Race("Grand Demolition Derby", 8000, cars)
    hours_passed = 0
    while not derby.race_finished():
        derby.hour_passes()
        hours_passed += 1
        if hours_passed % 10 == 0:
            print(f"\n[TRẠNG THÁI SAU {hours_passed} GIỜ] - Cuộc đua {derby.name}")
            derby.print_status()
    print("\n" + "="*40)
    print(f"CUỘC ĐUA KẾT THÚC SAU {hours_passed} GIỜ!")
    print("="*40)
    derby.print_status()