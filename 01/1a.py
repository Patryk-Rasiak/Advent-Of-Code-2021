with open("advent/01/1a.txt") as f:
    data = f.readlines()

prev = int(data[0])
count = 0
for line in data[1:]:
    if int(line) > prev:
        count += 1
    prev = int(line)

print(count)
