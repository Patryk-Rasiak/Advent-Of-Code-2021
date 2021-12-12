with open("advent/01/1b.txt") as f:
    data = f.readlines()
    data = [int(x) for x in data]

count = 0
prevs = []

for i in range(len(data[:-2])):

    curr = [data[i+x] for x in range(3)]
    if sum(curr) > sum(prevs) and len(prevs) != 0:

        count += 1
    prevs = curr
    print(count)
