def color():

    color_code = input("Enter your color code here: ")

    if color_code.startswith("#") and len(color_code) == 7:
        return "Correct"

    else:
        return "Try again"

print(color())
    

