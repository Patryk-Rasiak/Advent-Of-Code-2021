
with open("advent/6/6b.txt") as f:
    data = f.read()

    inputs = list(map(int, data.split(",")))

    fish_day = [0] * 9

    for fish in inputs:
        fish_day[fish] += 1

    for i in range(256):
        fish_day.append(fish_day[0])
        fish_day = fish_day[1:]
        fish_day[6] += fish_day[-1]
    print(sum(fish_day))
