city_list = []

for i in range (5):
    i = input("Enter the city here: ")
    print(i)
    city_list.append(i)

print("These cities entered are: ")
for city in city_list:
    print(city)