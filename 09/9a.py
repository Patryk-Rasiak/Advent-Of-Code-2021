
with open("advent/09/9a.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    data = [[int(x) for x in line] for line in data]

risk_levels = 0
for row in range(len(data)):
    for col in range(len(data[row])):

        # Upper left corner
        if row == 0 and col == 0:
            if data[row][col] < data[row][col + 1] and data[row][col] < data[row + 1][col]:
                risk_levels += data[row][col] + 1

        # Upper right corner
        elif row == 0 and col == (len(data[row]) - 1):
            if data[row][col] < data[row][col - 1] and data[row][col] < data[row + 1][col]:
                risk_levels += data[row][col] + 1

        # Upper border
        elif row == 0:
            if data[row][col] < data[row][col + 1] and data[row][col] < data[row][col - 1] and data[row][col] < data[row + 1][col]:
                risk_levels += data[row][col] + 1

        # Lower left corner
        elif col == 0 and row == (len(data) - 1):
            if data[row][col] < data[row][col + 1] and data[row][col] < data[row - 1][col]:
                risk_levels += data[row][col] + 1

        # Left border
        elif col == 0:
            if data[row][col] < data[row][col + 1] and data[row][col] < data[row + 1][col] and data[row][col] < data[row - 1][col]:
                risk_levels += data[row][col] + 1

        # Lower right corner
        elif row == (len(data) - 1) and col == (len(data[row]) - 1):
            if data[row][col] < data[row][col - 1] and data[row][col] < data[row - 1][col]:
                risk_levels += data[row][col] + 1

        # Lower border
        elif row == (len(data) - 1):
            if data[row][col] < data[row][col + 1] and data[row][col] < data[row][col - 1] and data[row][col] < data[row - 1][col]:
                risk_levels += data[row][col] + 1

        # Right border
        elif col == (len(data[row]) - 1):
            if data[row][col] < data[row][col - 1] and data[row][col] < data[row + 1][col] and data[row][col] < data[row - 1][col]:
                risk_levels += data[row][col] + 1

        # Center
        elif data[row][col] < data[row][col + 1] and data[row][col] < data[row][col - 1] and data[row][col] < data[row + 1][col] and data[row][col] < data[row - 1][col]:
            risk_levels += data[row][col] + 1

print(risk_levels)
