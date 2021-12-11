

with open("advent/10/10a.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

    closings = {"]": "[", "}": "{", ">": "<", ")": "("}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    corrupted_closings = []

    for k in range(len(data)):
        i = 0
        while i < len(data[k]):
            if data[k][i] in closings.keys():

                if data[k][i-1] == closings[data[k][i]]:
                    data[k] = data[k][:i-1] + data[k][i+1:]
                    i = 0
                else:
                    corrupted_closings.append(data[k][i])
                    break
            else:
                i += 1

    sum = 0
    for closing in corrupted_closings:
        sum += points[closing]

    print(sum)
