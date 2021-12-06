def print_board(board):
    for line in board:
        for char in line:
            if char == 0:
                print('.', end='')
            else:
                print(char, end='')
        print()


with open("advent/5/5b.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

    # Initializing the board
    board = [[] for _ in range(1000)]
    for line in board:
        for _ in range(1000):
            line.append(0)

    for line in data:
        a1, a2 = line.split(" -> ")
        x1, y1 = a1.split(",")
        x2, y2 = a2.split(",")

        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        # Vertical line
        if x1 == x2:

            for z in range(min(y1, y2), max(y1, y2)+1):
                board[z][x1] += 1

        # Horizontal line
        elif y1 == y2:

            for z in range(min(x1, x2), max(x1, x2)+1):
                board[y1][z] += 1

        # Diagonal line
        else:
            if x1 < x2 and y1 < y2:
                while x1 <= x2:
                    board[y1][x1] += 1
                    x1 += 1
                    y1 += 1

            elif x1 > x2 and y1 > y2:
                while x1 >= x2:
                    board[y2][x2] += 1
                    x2 += 1
                    y2 += 1

            elif x1 < x2 and y1 > y2:
                while x1 <= x2:
                    board[y1][x1] += 1
                    x1 += 1
                    y1 -= 1

            elif x1 > x2 and y1 < y2:
                while x1 >= x2:
                    board[y1][x1] += 1
                    x1 -= 1
                    y1 += 1


# Counting overlaps
counter = 0
for line in board:
    for char in line:
        if char > 1:
            counter += 1

print(counter)
