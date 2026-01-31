def get_middle_char(text):
    length = len(text)
    middle = length // 2  

    if length % 2 == 0:
        return text[middle - 1 : middle + 1]
    else:
       
        return text[middle]


print(f"Middle of 'Python': {get_middle_char('Python')}")  
print(f"Middle of 'Rules': {get_middle_char('Rules')}")    