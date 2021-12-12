def check_basin(row, col):
    global data, counter

    x = data[row][col]
    counter += 1
    data[row][col] = 9

    if data[row - 1][col] < 9 and data[row - 1][col] > x:
        check_basin(row - 1, col)
    if data[row + 1][col] < 9 and data[row + 1][col] > x:
        check_basin(row + 1, col)
    if data[row][col + 1] < 9 and data[row][col + 1] > x:
        check_basin(row, col + 1)
    if data[row][col - 1] < 9 and data[row][col - 1] > x:
        check_basin(row, col - 1)


with open("advent/09/9b.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    data = [[int(x) for x in line] for line in data]

basins = []
for nums in data:
    nums.insert(0, 9)
    nums.append(9)
data.insert(0, [9] * len(data[0]))
data.append([9]*len(data[0]))

low_points = []

for row in range(1, len(data)-1):
    for col in range(1, len(data[0])-1):
        if data[row][col] < data[row][col - 1] and data[row][col] < data[row][col + 1] and data[row][col] < data[row - 1][col] and data[row][col] < data[row + 1][col]:
            low_points.append((row, col))

counter = 0
for row, col in low_points:
    check_basin(row, col)
    basins.append(counter)
    counter = 0

basins.sort()
print(basins[-1] * basins[-2] * basins[-3])
