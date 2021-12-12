
with open("advent/6/6a.txt") as f:
    data = f.read()

    inputs = list(map(int, data.split(",")))
    days = 80

    for day in range(days):

        for i in range(len(inputs)):

            if inputs[i] == 0:
                inputs.append(8)
                inputs[i] = 6
            else:
                inputs[i] -= 1

    print(len(inputs))
