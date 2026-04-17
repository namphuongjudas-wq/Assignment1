def average_score(filename):
    total = 0
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                name, score = line.split(',')
                total += int(score.strip())
                count += 1
    return total / count if count > 0 else 0

if __name__ == "__main__":
    print("Average score:", average_score("scores.txt"))