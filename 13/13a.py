# Function to count how many # symbols are in the board
def count(board):
    count = 0
    for line in board:
        for char in line:
            if char == "#":
                count += 1
    return count


def fold_up(board, y):

    # Split boards into top board and bottom board
    top_board = board[:y]
    bottom_board = board[y + 1:]

    # Rotate bottom board vertically
    bottom_board.reverse()

    # If top board is longer, cover bottom board on the end of the top board
    if len(top_board) >= len(bottom_board):
        j = len(top_board) - 1
        for i in range(len(bottom_board)-1, -1, -1):
            top_board[j] = ["#" if top_board[j][x] == "#" or bottom_board[i][x]
                            == "#" else "." for x in range(len(top_board[0]))]

            j -= 1

        return top_board

    else:
        j = len(bottom_board) - 1
        for i in range(len(top_board)-1, -1, -1):
            bottom_board[j] = ["#" if bottom_board[j][x] == "#" or top_board[i][x]
                               == "#" else "." for x in range(len(top_board[0]))]
            j -= 1

        return bottom_board


def fold_left(board, x):

    left_board = []
    right_board = []

    # Split board for left and right board
    for row in board:
        left_board.append(row[:x])
        right_board.append(row[x+1:])

    # Rotate the right board horizontally
    for i in range(len(right_board)):
        right_board[i].reverse()

    # If the left board is longer, then cover the right board on the end of the left board
    if len(left_board[0]) >= len(right_board[0]):
        for row in range(len(left_board)):
            left_board[row] = ["#" if left_board[row][len(left_board[0])-1-z] == "#" or right_board[row][len(
                right_board[0])-1-z] == "#" else "." for z in range(len(right_board[0]))]
        return left_board
    else:
        for row in range(len(left_board)):
            right_board[row] = ["#" if right_board[row][len(right_board[0])-1-z] == "#" or left_board[row][len(
                left_board[0])-1-z] == "#" else "." for z in range(len(left_board[0]))]


with open("advent/13/13a.txt") as f:
    data = f.read()

# Split the input into coordinates and instructions
coords, instructions = data.split("\n\n")


# Find maximum x and y coord to set the board size accordingly
max_x = 0
max_y = 0
for point in coords.split():
    x, y = point.split(",")
    x, y = int(x), int(y)

    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y

# Initialize the board
board = []
for i in range(max_y+1):
    board.append(["."] * (max_x+1))

for point in coords.split():
    x, y = point.split(",")
    x, y = int(x), int(y)
    board[y][x] = "#"

# Call the apprioriate function for each instruction
for line in instructions.split("\n"):
    line = line.split("=")

    if line[0][-1] == "y":
        board = fold_up(board, int(line[1]))
    else:
        board = fold_left(board, int(line[1]))

    break


print(count(board))
