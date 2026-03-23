numbers_list = []
while True:
    number = input("Enter the integers: ")
    if number == "":
        break
    else: 
        numbers_list.append(int(number))



def uneven_number(uneven):
    result = []
    for i in uneven:
        if i % 2 == 0:
            result.append(i)
        else:
            continue
    return result

print(numbers_list)
print(uneven_number(numbers_list))