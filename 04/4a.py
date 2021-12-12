def count_unmarked(board):
    count = 0
    for row in board:
        for key, value in row.items():
            if value == False:
                count += int(key)
    return count


def check_win_horizontally(row):

    for value in row.values():
        if value == False:
            return False
    return True


def check_win_vertically(board):

    for i in range(5):
        true_count = 0
        for j in range(5):
            if list(board[j].values())[i] == True:
                true_count += 1
        if true_count == 5:
            return True
    return False


def check_win(board, row):
    return check_win_horizontally(row) or check_win_vertically(board)


with open("advent/04/4a.txt") as f:
    data = f.read().split("\n\n")

inp = data[0].split(",")
boards = data[1:]

# 2D list of dictionaries for every board
marks = []

# Initializing a list of marks for every line in every board
for board in boards:
    marks.append([])
    for line in board.split("\n"):
        marks[-1].append({})
        for num in line.split():
            marks[-1][-1][num] = False


def play():
    for num in inp:
        for board in list(marks):
            for row in board:

                if num in row.keys():
                    row[num] = True
                    if check_win(board, row):
                        unmarked = count_unmarked(board)
                        return unmarked * int(num)


result = play()
print(result)
