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

def main():
    with open("02-input", 'r') as file:
        input_array = [int(i) for i in file.read().split(',')]
    input_array[1] = 12
    input_array[2] = 2
    
    intCodeRunner(input_array)
    print(input_array)

if __name__ == "__main__":
    main()