
with open("advent/07/7a.txt") as f:
    data = f.read()
    inputs = list(map(int, data.split(",")))

inputs.sort()
min_distance = float("inf")
min_x = 0

for x in inputs:

    distance = 0
    for y in inputs:
        distance += abs(x - y)

    if distance < min_distance:
        min_distance = distance
        min_x = x

print(min_distance)
