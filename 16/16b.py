import math

hex_to_bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
              "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

data = "".join([hex_to_bin[x]
               for x in open("advent/16/16b.txt").read().replace("\n", "")])


def solve(data):
    res = solve_rec(data)
    print(res[0][0])


def solve_rec(data):
    # Type ID
    t = int(data[3:6], 2)

    # Counter of length of the current packet
    counter = 6
    new_data = data[6:]
    result = []

    if t == 4:
        run = True
        new_res = ""
        while run:
            if new_data[0] == "0":
                run = False
            new_res += new_data[1:5]
            new_data = new_data[5:]
            counter += 5
        result.append(int(new_res, 2))
    else:
        I = new_data[0]
        counter += 1
        new_data = new_data[1:]

        if I == "0":
            # Current length
            curr_l = 0
            # Check the length of subpackets and call them
            max_l = int(new_data[:15], 2)
            new_data = new_data[15:]
            counter += 15

            while curr_l < max_l:
                r, c = solve_rec(new_data)
                new_data = new_data[c:]
                curr_l += c
                result += r
                counter += c

        else:
            # For I = 1 check the number of subpackets and call them
            num_sub = int(new_data[:11], 2)
            new_data = new_data[11:]
            counter += 11

            for _ in range(num_sub):
                r, c = solve_rec(new_data)
                new_data = new_data[c:]
                result += r
                counter += c

    # Update the result based on the type ID
    match t:
        case 0:
            result = [sum(result)]
        case 1:
            result = [math.prod(result)]
        case 2:
            result = [min(result)]
        case 3:
            result = [max(result)]
        case 5:
            if result[0] > result[1]:
                result = [1]
            else:
                result = [0]
        case 6:
            if result[0] < result[1]:
                result = [1]
            else:
                result = [0]
        case 7:
            if result[0] == result[1]:
                result = [1]
            else:
                result = [0]
        case _:
            pass

    return result, counter


solve(data)
