def print_board(board):

    for line in board:
        for char in line:
            print(char, end='')
        print()


with open("advent/5/5a.txt") as f:
    data = f.readlines()

    data = [x.strip() for x in data]
    board = [[] for _ in range(1000)]
    for line in board:
        for _ in range(1000):
            line.append('.')

    for line in data:
        a1, a2 = line.split(" -> ")
        x1, y1 = a1.split(",")
        x2, y2 = a2.split(",")

        x1_temp, y1_temp, x2_temp, y2_temp = int(x1), int(y1), int(x2), int(y2)

        x1 = max(x1_temp, x2_temp)
        x2 = min(x1_temp, x2_temp)
        y1 = max(y1_temp, y2_temp)
        y2 = min(y1_temp, y2_temp)

        # Vertical line
        if x1 == x2:
            while y1 >= y2:
                if board[y2][x1] == '.':
                    board[y2][x1] = 1
                else:
                    board[y2][x1] += 1
                y2 += 1

        # Horizontal line
        elif y1 == y2:
            while x1 >= x2:
                if board[y1][x2] == '.':
                    board[y1][x2] = 1
                else:
                    board[y1][x2] += 1
                x2 += 1

print_board(board)

counter = 0

for line in board:
    for char in line:
        if type(char) != str and char > 1:
            counter += 1

print(counter)
