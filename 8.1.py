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


if __name__ == "__main__":
    print("--- TEST BÀI 1 ---")
    h = Elevator(1, 10)
    h.go_to_floor(5) 
    h.go_to_floor(1)



   
