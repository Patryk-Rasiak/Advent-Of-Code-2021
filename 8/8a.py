with open("advent/8/8a.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

    counter = 0
    for line in data:
        _, output = line.split(" | ")
        for digit in output.split():
            if len(digit) in [2, 3, 4, 7]:
                counter += 1
    print(counter)
