class intCodeRunner():
    def __init__(self, instr_array, input=[]):
        # Sets self.instructionArray (list of ints)
        self.setInstructionArray(instr_array)
        # Sets self.input (list of ints)
        self.setInput(input)
        self.inputIndex = 0
        self.output = []
        self.rel_base = 0

    def run(self):
        instructionDict = {
            1: self._add,
            2: self._multiply,
            3: self._input,
            4: self._output,
            5: lambda *params: self._jump_if(True, *params),
            6: lambda *params: self._jump_if(False, *params),
            7: self._less_than,
            8: self._equals,
            9: self._rel_base
        }
        HALT = 99

        index = 0
        while True:
            op_code = self.instructionArray[index]
            op_code = ("00000" + str(op_code))[-5:]
            param_modes = [int(char) for char in op_code[0:3]]
            param_modes.reverse()
            instruction = int(op_code[3:])

            if instruction == HALT:
                return self.instructionArray
            if instruction in instructionDict:
                index = instructionDict[instruction](index, param_modes)
            else:
                raise RuntimeError(
                    "Undefined instruction encountered. Please check instruction array.")

    def runAsync(self):
        instructionDict = {
            1: self._add,
            2: self._multiply,
            3: self._input,
            5: lambda *params: self._jump_if(True, *params),
            6: lambda *params: self._jump_if(False, *params),
            7: self._less_than,
            8: self._equals,
            9: self._rel_base
        }
        HALT = 99
        OUTPUT = 4

        index = 0
        output_index = 0
        while True:
            op_code = self.instructionArray[index]
            op_code = ("00000" + str(op_code))[-5:]
            param_modes = [int(char) for char in op_code[0:3]]
            param_modes.reverse()
            instruction = int(op_code[3:])

            if instruction == OUTPUT:
                index = self._output(index, param_modes)
                yield self.output[output_index]
                output_index += 1
            if instruction == HALT:
                return self.instructionArray
            if instruction in instructionDict:
                index = instructionDict[instruction](index, param_modes)

    def getOutput(self):
        return self.output

    def getInput(self):
        return self.input

    def getInstructionArray(self):
        return self.instructionArray

    def setInput(self, input):
        try:
            if isinstance(input, int):
                self.input = [input]
            else:
                self.input = list(map(int, list(input)))
        except:
            raise TypeError(
                "Invalid intCodeRunner input: setInput argument must be of type int or list of ints.")

    def addInput(self, input):
        try:
            self.input.append(int(input))
        except:
            raise TypeError(
                "Invalid intCodeRunner input: addInput argument must be of type int.")

    def setInstructionArray(self, in_array):
        try:
            self.instructionArray = list(map(int, in_array))
        except:
            raise TypeError(
                "Invalid intCodeRunner input: instruction array must be an iterable object containing integers.")

    def _add(self, index, param_modes):
        pointers = []
        for (idx, mode) in enumerate(param_modes, 1):
            if mode == 0:
                pointers.append(self.instructionArray[index + idx])
            elif mode == 1:
                pointers.append(index + idx)
            elif mode == 2:
                pointers.append(
                    self.instructionArray[index + idx] + self.rel_base)
        self.instructionArray[pointers[2]] = self.instructionArray[pointers[0]
                                                                   ] + self.instructionArray[pointers[1]]
        index += 4
        return index

    def _multiply(self, index, param_modes):
        pointers = []
        for (idx, mode) in enumerate(param_modes, 1):
            if mode == 0:
                pointers.append(self.instructionArray[index + idx])
            elif mode == 1:
                pointers.append(index + idx)
            elif mode == 2:
                pointers.append(
                    self.instructionArray[index + idx] + self.rel_base)
        self.instructionArray[pointers[2]] = self.instructionArray[pointers[0]
                                                                   ] * self.instructionArray[pointers[1]]
        index += 4
        return index

    def _input(self, index, param_modes):
        if param_modes[0] == 0:
            pointer = self.instructionArray[index + 1]
        else:  # param_modes[0] == 2
            pointer = self.instructionArray[index + 1] + self.rel_base
        self.instructionArray[pointer] = self.input[self.inputIndex]
        self.inputIndex += 1
        index += 2
        return index

    def _output(self, index, param_modes):
        if param_modes[0] == 0:
            pointer = self.instructionArray[index + 1]
        elif param_modes[0] == 1:
            pointer = index + 1
        else:  # param_modes[0] == 2
            pointer = self.instructionArray[index + 1] + self.rel_base
        self.output.append(self.instructionArray[pointer])
        # print(self.instructionArray[pointer])
        index += 2
        return index

    def _jump_if(self, in_bool, index, param_modes):
        pointers, params = ([], [])
        for i in range(2):
            if param_modes[i] == 0:
                pointers.append(self.instructionArray[index + i + 1])
            elif param_modes[i] == 1:
                pointers.append(index + i + 1)
            elif param_modes[i] == 2:
                pointers.append(
                    self.instructionArray[index + i + 1] + self.rel_base)
            params.append(self.instructionArray[pointers[i]])
        if ((in_bool == True and params[0] != 0) or (in_bool == False and params[0] == 0)):
            index = params[1]
        else:
            index += 3
        return index

    def _less_than(self, index, param_modes):
        pointers, params = ([], [])
        for (idx, mode) in enumerate(param_modes, 1):
            if mode == 0:
                pointers.append(self.instructionArray[index + idx])
            elif mode == 1:
                pointers.append(index + idx)
            elif mode == 2:
                pointers.append(
                    self.instructionArray[index + idx] + self.rel_base)
            params.append(self.instructionArray[pointers[idx - 1]])
        store = 1 if params[0] < params[1] else 0
        self.instructionArray[pointers[2]] = store
        index += 4
        return index

    def _equals(self, index, param_modes):
        pointers, params = ([], [])
        for (idx, mode) in enumerate(param_modes, 1):
            if mode == 0:
                pointers.append(self.instructionArray[index + idx])
            elif mode == 1:
                pointers.append(index + idx)
            elif mode == 2:
                pointers.append(
                    self.instructionArray[index + idx] + self.rel_base)
            params.append(self.instructionArray[pointers[idx - 1]])
        store = 1 if params[0] == params[1] else 0
        self.instructionArray[pointers[2]] = store
        index += 4
        return index

    def _rel_base(self, index, param_modes):
        if param_modes[0] == 1:
            pointer = index + 1
        elif param_modes[0] == 0:
            pointer = self.instructionArray[index + 1]
        else:  # param_modes[0] == 2:
            pointer = self.instructionArray[index + 1] + self.rel_base
        self.rel_base += self.instructionArray[pointer]
        index += 2
        return index


def main():
    with open('11-Input') as file:
        input_array = list(map(int, file.read().split(',')))
    for i in range(len(input_array * 1000)):
        input_array.append(0)

    robot_code = intCodeRunner(input_array, 0)
    robot = robot_code.runAsync()

    colorDict = {(0,0): 0}
    location = [0,0]
    direction = 0       # 0, 1, 2, 3: N, E, S, W

    while True:
        try:
            new_color = next(robot)
            colorDict[tuple(location)] = new_color
            direction = (4 + (direction - 1 + (next(robot) * 2))) % 4
            if direction % 2 == 0:
                location[1] += -1 + direction
            if direction % 2 != 0:
                location[0] += -1 if direction == 3 else 1
            if not (tuple(location) in colorDict):
                colorDict[tuple(location)] = 0
            robot_code.addInput(colorDict[tuple(location)])
        except StopIteration:
            break

    print(len(colorDict) - 1) # -1: it doesn't paint the last panel


if __name__ == "__main__":
    main()
