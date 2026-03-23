number = int(input("Enter an interger here: "))
prime = True
for i in range (2,number-1):
    if number % int(i) == 0:
        prime = False
        break
    else:
        pass
if prime == False or number <= 1:
    print("Not Prime Number")
else:
    print("Prime Number")