def count_lines(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            if line.strip(): 
                count += 1
    return count

if __name__ == "__main__":
    print("Non-blank line count:", count_lines("sample.txt"))