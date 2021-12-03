def most_common_digit(data, index):
    counts = {"0": 0, "1": 0}

    for line in data:
        counts[line[index]] += 1

    if counts["0"] > counts["1"]:
        return "0"
    else:
        return "1"


def least_common_digit(data, index):
    counts = {"0": 0, "1": 0}

    for line in data:
        counts[line[index]] += 1

    if counts["0"] <= counts["1"]:
        return "0"
    else:
        return "1"


with open("advent/3/3b.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    most_common_data = data.copy()
    least_common_data = data.copy()
    i = 0
    while len(most_common_data) > 1:
        most_common = most_common_digit(most_common_data, i)
        most_common_data = list(
            filter(lambda x: x[i] == most_common, most_common_data))
        i += 1
    print(most_common_data[0])

    i = 0
    while len(least_common_data) > 1:
        most_common = least_common_digit(least_common_data, i)
        least_common_data = list(
            filter(lambda x: x[i] == most_common, least_common_data))
        i += 1

    print(least_common_data[0])

    print(int(most_common_data[0], 2) * int(least_common_data[0], 2))
