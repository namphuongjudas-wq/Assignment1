def course_codes():
    clss = input("Enter your course_code: ")
    if clss == clss[:2].upper() + clss[2:]:
        return "True"
    else:
        return "False"


print(course_codes())

