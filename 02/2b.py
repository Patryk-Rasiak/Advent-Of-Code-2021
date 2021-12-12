
with open("advent/02/2b.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

horizontal = 0
depth = 0
aim = 0
for line in data:
    direction, value = line.split(" ")
    value = int(value)
    match direction:
        case "forward":
            horizontal += value
            depth += aim * value
        case "up":
            aim -= value
        case "down":
            aim += value
        case _:
            pass
print(depth * horizontal)
