numbers_list = []
while True:
    nums = input("enter numbers: ")
    if nums == "":
        break
    if nums.isdigit():
        numbers_list.append(nums)
        numbers_list.sort(reverse=True)
print(numbers_list)
print(numbers_list[:5])