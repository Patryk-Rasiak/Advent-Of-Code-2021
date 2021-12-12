# Sorting so that strings with length 5 will be at the end
def specific_sort(x):
    if len(x) == 5:
        return 10
    else:
        return len(x)


def contains(str1, str2):
    for char in str2:
        if char not in str1:
            return False
    return True


with open("advent/08/8b.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

sum = 0

for line in data:
    inputs, outputs = line.split("| ")
    digits = (inputs + outputs).split()
    digits.sort(key=specific_sort)
    numbers = {}
    result = ""

    for digit in digits:

        match len(digit):
            case 2:
                numbers["1"] = digit
            case 3:
                numbers["7"] = digit
            case 4:
                numbers["4"] = digit
            case 5:
                if contains(digit, numbers["1"]):
                    numbers["3"] = digit
                elif contains(numbers["6"], digit):
                    numbers["5"] = digit
                else:
                    numbers["2"] = digit
            case 6:
                if contains(digit, numbers["4"]):
                    numbers["9"] = digit
                elif contains(digit, numbers["1"]):
                    numbers["0"] = digit
                else:
                    numbers["6"] = digit
            case 7:
                numbers["8"] = digit

    # Getting output for each entry
    for output in outputs.split():
        for key, value in numbers.items():
            if set(output) == set(value):
                result += key
    sum += int(result)

print(sum)
