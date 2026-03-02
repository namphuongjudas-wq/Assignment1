def course_codes():
        clss = input("Enter your course_code: ")
        letter = clss[:3]
        num = clss[3:]
        if letter.upper() and num.isdigit() and len(clss) == 6:
            return "True"
            
        else:
            return "False"


print(course_codes())




