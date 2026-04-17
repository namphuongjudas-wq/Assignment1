def find_keyword_lines(filename, keyword):
    line_numbers = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f, start=1):
            if keyword in line:
                line_numbers.append(i)
    return line_numbers

if __name__ == "__main__":
    print("Lines with 'python':", find_keyword_lines("sample.txt", "python"))

    