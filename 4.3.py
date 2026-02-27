def number():
    text = input("Type your text here: ")
    words = text.split()
    nums = []
    for word in words:
        clean = word.strip(".,!?")

        if clean.isdigit():
            nums.append(int(clean))
    
    resul = sum(nums)
    print(f"tổng số trong văn bản trên là:{resul}")
    return resul

number()