correct_username = "python"
correct_password = "rules"
attempts = 0

while attempts < 5:
    user = input("Username: ")
    pw = input("Password: ")
    
    if user == correct_username and pw == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        if attempts == 5:
            print("Access denied")