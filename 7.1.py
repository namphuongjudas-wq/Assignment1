class car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        

if __name__ == "__main__":
    my_car = car("ABC-123" , "142 km/h")
    print(f'registration number is: {my_car.registration_number}')
    print(f'Current speed: {my_car.current_speed}')
    print(f'Maximun speed: {my_car.maximum_speed}')
    print(f'Travelled distance: {my_car.travelled_distance}')

