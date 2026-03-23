number_list =[]

while True: 
    
    numbers = input("Enter your numbers here( press 'Enter' to quit): ")
    if numbers == "":
        break
    else: 
        number_list.append(int(numbers))
        number_list.sort()

print(number_list[-5:])