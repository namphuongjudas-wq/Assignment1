
numbers_list = []
while True:
    number = input("Enter the integers: ")
    if number == "":
        break
    else: 
        numbers_list.append(int(number))

def sum_integers(number_L):
    result = sum(number_L)
    return result
    
print("------------------")
print(f"Sum of the numbers in the list is: {sum_integers(numbers_list)}")