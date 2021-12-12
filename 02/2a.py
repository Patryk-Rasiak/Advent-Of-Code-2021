
with open("advent/02/2a.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

horizontal = 0
depth = 0
for line in data:
    direction, value = line.split(" ")
    value = int(value)
    match direction:
        case "forward":
            horizontal += value
        case "up":
            depth -= value
        case "down":
            depth += value
        case _:
            pass
print(depth * horizontal)
