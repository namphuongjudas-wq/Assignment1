name = input("your name:")
print("xin chào, " + name)
print("----------")
r= float(input("ban kinh= "))
Ct= 2 * 3.14 * r
print("chu vi đường tròn là "+ str(Ct))
print("-----------")
cd= float(input("chieu dai= "))
cr= float(input("chieu rong= "))
Chcn= 2*cd + 2*cr
S= cd * cr
print(" chu vi hình chữ nhật là " + str(Chcn))
print(" diện tích hình chữ nhật là " + str(S))
print("------------")
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
print("----------------------------")

talents = float(input("Enter talents:\n"))
pounds = float(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))
talents_to_gram= talents*20*32*13.3
pound_to_gram=pounds*32*13.3
lots_to_gram= lots*13.3
sum= talents_to_gram + pound_to_gram + lots_to_gram
gram= sum%1000
kg= sum//1000
gram=round(gram,2)

print("the weight in modern units: " + str(kg) +" kilograms and " + str(gram) +" grams")
print("------------------------------")

import random

# 3-digit code
d1 = random.randint(0, 9)
d2 = random.randint(0, 9)
d3 = random.randint(0, 9)
print("3-digit code:", d1, d2, d3)

# 4-digit code
n1 = random.randint(1, 6)
n2 = random.randint(1, 6)
n3 = random.randint(1, 6)
n4 = random.randint(1, 6)
print("4-digit code:", n1, n2, n3, n4)