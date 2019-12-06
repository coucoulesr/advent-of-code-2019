class intCodeRunner():
    def __init__(self, in_array, input):
        self.setInstructionArray(in_array)
        self.setInput(input)

    def run(self):
        ADD = 1
        MULTIPLY = 2
        INPUT = 3
        OUTPUT = 4
        JUMP_IF_TRUE = 5
        JUMP_IF_FALSE = 6
        LESS_THAN = 7
        EQUALS = 8
        HALT = 99

        index = 0
        while True:
            op_code = self.array[index]
            op_code = ("00000" + str(op_code))[-5:]
            param_modes = [int(char) for char in op_code[0:3]][::-1]
            instruction = int(op_code[3:])
            if instruction == HALT:
                return self.array
            elif instruction == ADD:
                index = self._add(index, param_modes)
            elif instruction == MULTIPLY:
                index = self._multiply(index, param_modes)
            elif instruction == INPUT:
                index = self._input(index)
            elif instruction == OUTPUT:
                index = self._output(index, param_modes)
            elif instruction == JUMP_IF_TRUE:
                index = self._jump_if(True, index, param_modes)
            elif instruction == JUMP_IF_FALSE:
                index = self._jump_if(False, index, param_modes)
            elif instruction == LESS_THAN:
                index = self._less_than(index, param_modes)
            elif instruction == EQUALS:
                index = self._equals(index, param_modes)
            else:
                raise RuntimeError("Undefined instruction encountered. Please check instruction array.")
 
    def getInput(self):
        return self.input

    def getInstructionArray(self):
        return self.array

    def setInput(self, input):
        try:
            self.input = int(input)
        except:
            raise TypeError("Invalid intCodeRunner input: input must be of type int.")

    def setInstructionArray(self, in_array):
        try:
            self.array = list(map(int, in_array))
        except:
            raise TypeError("Invalid intCodeRunner input: instruction array must be an iterable object containing integers.")

    def _add(self, index, param_modes):
        pointers = []
        for (idx, mode) in enumerate(param_modes, 1):
            if mode == 0:
                pointers.append(self.array[index + idx])
            elif mode == 1:
                pointers.append(index + idx)
        self.array[pointers[2]] = self.array[pointers[0]] + self.array[pointers[1]]
        index += 4
        return index
    
    def _multiply(self, index, param_modes):
        pointers = []
        for (idx, mode) in enumerate(param_modes, 1):
            if mode == 0:
                pointers.append(self.array[index + idx])
            elif mode == 1:
                pointers.append(index + idx)
        self.array[pointers[2]] = self.array[pointers[0]] * self.array[pointers[1]]
        index += 4
        return index
    
    def _input(self, index):
        pointer = self.array[index + 1]
        self.array[pointer] = self.input
        index += 2
        return index
    
    def _output(self, index, param_modes):
        if param_modes[0] == 0:
            pointer = self.array[index + 1]
        else:
            pointer = index + 1
        print(self.array[pointer])
        index += 2
        return index

    def _jump_if(self, in_bool, index, param_modes):
        pointers, params = ([], [])
        for i in range(2):
            if param_modes[i] == 0:
                pointers.append(self.array[index + i + 1])
            elif param_modes[i] == 1:
                pointers.append(index + i + 1)
            params.append(self.array[pointers[i]])
        if ((in_bool == True and params[0] != 0) or (in_bool == False and params[0] == 0)):
            index = params[1]
        else:
            index += 3
        return index

    def _less_than(self, index, param_modes):
        pointers, params = ([], [])
        for (idx, mode) in enumerate(param_modes, 1):
            if mode == 0:
                pointers.append(self.array[index + idx])
            elif mode == 1:
                pointers.append(index + idx)
            params.append(self.array[pointers[idx - 1]])
        store = 1 if params[0] < params[1] else 0
        self.array[pointers[2]] = store
        index += 4
        return index

    def _equals(self, index, param_modes):
        pointers, params = ([], [])
        for (idx, mode) in enumerate(param_modes, 1):
            if mode == 0:
                pointers.append(self.array[index + idx])
            elif mode == 1:
                pointers.append(index + idx)
            params.append(self.array[pointers[idx - 1]])
        store = 1 if params[0] == params[1] else 0
        self.array[pointers[2]] = store
        index += 4
        return index

def main():
    with open('./05-Input') as file:
        input_array = list(map(int, file.read().split(',')))

    test = intCodeRunner(input_array, 5)
    test.run()


if __name__ == "__main__":
    main()
