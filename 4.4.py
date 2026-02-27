phone_number_list = []

while True:
    phone_number = input("Type your phone number here: ")
    
    if phone_number.startswith("0") or phone_number.startswith("+84"):
        phone_number_list.append(phone_number)
        anonymous = "#" * (len(phone_number)-3) + phone_number[7:]
        print(f"Your phone number is anonymized:{anonymous}")
        break
    
    else:
        print("try again")

