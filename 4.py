while True:
    try:
        a=int(input("nhập số nguyên thứ nhất:"))
        b=int(input("nhập số nguyên thứ hai:"))
        c=int(input("nhập số nguyên thứ ba:"))
        break
    except ValueError:
        print(" Bạn đã nhập sai vui lòng nhập lại đúng số nguyên")
T= a+b+c
M= a*b*c
Aver= (a+b+c)/3
print("Tổng= " + str(T))
print("Tích= " + str(M))
print("Trung bình cộng= " + str(Aver))