with open("advent/1/1b.txt") as f:
    data = f.readlines()
    data = [int(x) for x in data]
    counter = 0
    prevs = []

    for i in range(len(data[:-2])):

        curr = [data[i+x] for x in range(3)]
        if sum(curr) > sum(prevs) and len(prevs) != 0:

            counter += 1
        prevs = curr
    print(counter)
