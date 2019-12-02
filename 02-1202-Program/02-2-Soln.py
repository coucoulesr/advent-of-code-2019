def intCodeRunner(in_array):
    index = 0
    while True:
        op = in_array[index]
        if op == 99:
            return in_array
        elif op == 1 or op == 2:
            p1 = in_array[index + 1]
            p2 = in_array[index + 2]
            p_out = in_array[index + 3]
            if op == 1:
                in_array[p_out] = in_array[p1] + in_array[p2]
            if op == 2:
                in_array[p_out] = in_array[p1] * in_array[p2]
        else:
            return "error"
        index += 4

def bruteForce(answer, in_array):
    for i in range(len(in_array)):
        for j in range(len(in_array)):
            try_list = list(in_array)
            try_list[1] = i
            try_list[2] = j
            intCodeRunner(try_list)
            if try_list[0] == answer:
                return (i, j)
    return (0, 0)

def main():
    with open("02-input", 'r') as file:
        input_array = [int(i) for i in file.read().split(',')]

    (noun, verb) = bruteForce(19690720, input_array)
    print(100 * noun + verb)

if __name__ == "__main__":
    main()