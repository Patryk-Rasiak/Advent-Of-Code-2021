

with open("advent/10/10b.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

    closings = {"]": "[", "}": "{", ">": "<", ")": "("}
    completions = {"[": "]", "{": "}", "(": ")", "<": ">"}
    values = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []

    for k in range(len(data)):
        corrupted = False
        i = 0
        while i < len(data[k]):
            if data[k][i] in closings.keys():

                if data[k][i-1] == closings[data[k][i]]:
                    data[k] = data[k][:i-1] + data[k][i+1:]
                    i = 0

                else:
                    corrupted = True
                    break

            else:
                i += 1

        # incomplete line
        if(len(data[k]) > 0) and not corrupted:

            score = 0
            data[k] = list(data[k])
            data[k].reverse()
            for opening in data[k]:
                score *= 5
                score += values[completions[opening]]
            scores.append(score)
    scores.sort()
    print(scores[len(scores)/2])
