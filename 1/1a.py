import sys


with open("advent/1/1.txt") as f:
    data = f.readlines()


prev = int(data[0])
counter = 0
for line in data[1:]:
    if int(line) > prev:
        counter += 1
    prev = int(line)

print(counter)
