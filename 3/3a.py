def most_common_digit(data, index):
    counts = {"0": 0, "1": 0}

    for line in data:
        counts[line[index]] += 1

    return max(counts, key=counts.get)


def least_common_digit(data, index):
    counts = {"0": 0, "1": 0}

    for line in data:
        counts[line[index]] += 1

    return min(counts, key=counts.get)


with open("advent/3/3a.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

    gamma_rate = ""
    epsilon_rate = ""

    for i in range(len(data[0])):
        most_common = most_common_digit(data, i)
        least_common = least_common_digit(data, i)
        gamma_rate += most_common
        epsilon_rate += least_common

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))
