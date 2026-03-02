def phone_number_def():

    while True:
        phone_number = input("Type your phone number here: ")
        
        if phone_number.startswith("0") or phone_number.startswith("+84"):
            anonymous = "#" * (len(phone_number)-3) + phone_number[7:]
            return anonymous

        
        else:
            print("try again")

print(f"Your phone number is anonymized: {phone_number_def()}")


