number = []
while True:
    num = input("Enter your numbers: ")
    if num == "":
        break

    numbers= float(num)
    number.append(numbers)

    print("Enter again")
if len(numbers) > 0:
    print("Largest number is ", max(numbers))
    print("Smallest number is ", min())
else:
    print("Enter again")

     