def intCodeRunner(in_array, input):
    index = 0
    while True:
        op_code = in_array[index]
        op_code = ("00000" + str(op_code))[-5:]
        instr = int(op_code[3:])
        param_modes = [int(char) for char in op_code[0:3]][::-1]
        if instr == 99:
            return in_array
        elif instr == 1 or instr == 2:
            params = []
            for (idx, mode) in enumerate(param_modes, 1):    
                if mode == 0:
                    params.append(in_array[index + idx])
                elif mode == 1:
                    params.append(index + idx)
            if instr == 1:
                in_array[params[2]] = in_array[params[0]] + in_array[params[1]]
            if instr == 2:
                in_array[params[2]] = in_array[params[0]] * in_array[params[1]]
            index += 4
        elif instr == 3:
            in_array[in_array[index + 1]] = input
            index += 2
        elif instr == 4:
            if param_modes[0] == 0:
                pointer = in_array[index + 1]
            else:
                pointer = index + 1
            print(in_array[pointer])
            index += 2
        else:
            return "error"
        


def main():
    with open('./05-Input') as file:
        input_array = list(map(int, file.read().split(',')))
    
    intCodeRunner(input_array, 1)


if __name__ == "__main__":
    main()
