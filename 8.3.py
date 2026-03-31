class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Thang máy đang ở tầng: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Thang máy đang ở tầng: {self.current_floor}")

    def go_to_floor(self, target_floor):
        # Kiểm tra tầng hợp lệ
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Tầng không hợp lệ!")
            return
            
        print(f"==> Yêu cầu di chuyển đến tầng {target_floor}")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()



class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        # Tạo danh sách các thang máy
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        # Kiểm tra xem số thứ tự thang máy có tồn tại không (index từ 0)
        if 0 <= elevator_number < len(self.elevators):
            print(f"\n[Tòa nhà] Đang vận hành thang máy số {elevator_number}:")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Thang máy không tồn tại!")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        # Tạo danh sách các thang máy
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        # Kiểm tra xem số thứ tự thang máy có tồn tại không (index từ 0)
        if 0 <= elevator_number < len(self.elevators):
            print(f"\n[Tòa nhà] Đang vận hành thang máy số {elevator_number}:")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Thang máy không tồn tại!")

    def fire_alarm(self):
        print("\n" + "="*40)
        print("CẢNH BÁO CHÁY! Đưa tất cả thang máy về tầng trệt.")
        print("="*40)
        for i, elevator in enumerate(self.elevators):
            print(f"\n[Hệ thống an toàn] Di chuyển thang máy số {i}:")
            elevator.go_to_floor(self.bottom_floor)

if __name__ == "__main__":
    print("--- TEST BÀI 1 ---")
    h = Elevator(1, 10)
    h.go_to_floor(5) 
    h.go_to_floor(1)
    my_building = Building(1, 10, 3) 
    my_building.run_elevator(0, 7) 
    my_building.run_elevator(2, 4) 
    my_building.fire_alarm()