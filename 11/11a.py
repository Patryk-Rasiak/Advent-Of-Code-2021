from itertools import product, permutations

with open("advent/11/11a.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

    data = [[int(x) for x in line] for line in data]
    flashes = 0

    for i in range(len(data)):
        data[i].insert(0, float("-inf"))
        data[i].append(float("-inf"))
    data.insert(0, [float("-inf")] * len(data[1]))
    data.append([float("-inf")] * len(data[1]))

    for step in range(100):
        for row in range(len(data)):
            for col in range(len(data[0])):
                data[row][col] += 1

        run = True
        while run:
            run = False

            for row in range(len(data)):
                for col in range(len(data[0])):
                    if data[row][col] > 9:
                        flashes += 1
                        perm = product([-1, 0, 1], repeat=2)
                        for i, j in perm:
                            if not (i == 0 and j == 0) and data[row+i][col+j] != 0:
                                data[row+i][col+j] += 1

                        data[row][col] = 0
                        run = True

    print(flashes)
