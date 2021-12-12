def count_fuel(x):
    counter = 0
    for i in range(x + 1):
        counter += i
    return counter


with open("advent/07/7b.txt") as f:
    data = f.read()

inputs = list(map(int, data.split(",")))

inputs.sort()

min_distance = float("inf")
min_x = 0

for x in range(max(inputs)):

    distance = 0
    for y in inputs:
        distance += count_fuel(abs(x - y))

    if distance < min_distance:
        min_distance = distance
        min_x = x
    else:
        break

print(min_distance)
