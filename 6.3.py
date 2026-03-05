name_list = set()
while True:
    name = input("Typr your name here: ")
    
    if name == "":
        break
    if name in name_list:
        print("Existing name")
    else:
        print("New name")
        name_list.add(name)
     
    
print("\nList of name:")
for i in name_list:
    print(i)

