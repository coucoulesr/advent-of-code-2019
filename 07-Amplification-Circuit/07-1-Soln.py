class intCodeRunner():
    def __init__(self, instr_array, input = []):
        self.setInstructionArray(instr_array)   # Sets self.instructionArray (list of ints)
        self.setInput(input)                    # Sets self.input (list of ints)
        self.inputIndex = 0
        self.output = []

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
        }
        HALT = 99

        index = 0
        while True:
            op_code = self.instructionArray[index]
            op_code = ("00000" + str(op_code))[-5:]
            param_modes = [int(char) for char in op_code[0:3]][::-1]
            instruction = int(op_code[3:])

            if instruction == HALT:
                return self.instructionArray
            if instruction in instructionDict:
                index = instructionDict[instruction](index, param_modes)
            else:
                raise RuntimeError(
                    "Undefined instruction encountered. Please check instruction array.")

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
        self.instructionArray[pointers[2]] = self.instructionArray[pointers[0]] + \
            self.instructionArray[pointers[1]]
        index += 4
        return index

    def _multiply(self, index, param_modes):
        pointers = []
        for (idx, mode) in enumerate(param_modes, 1):
            if mode == 0:
                pointers.append(self.instructionArray[index + idx])
            elif mode == 1:
                pointers.append(index + idx)
        self.instructionArray[pointers[2]] = self.instructionArray[pointers[0]] * \
            self.instructionArray[pointers[1]]
        index += 4
        return index

    def _input(self, index, param_modes):
        pointer = self.instructionArray[index + 1]
        self.instructionArray[pointer] = self.input[self.inputIndex]
        self.inputIndex += 1
        index += 2
        return index

    def _output(self, index, param_modes):
        if param_modes[0] == 0:
            pointer = self.instructionArray[index + 1]
        else:
            pointer = index + 1
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
            params.append(self.instructionArray[pointers[idx - 1]])
        store = 1 if params[0] == params[1] else 0
        self.instructionArray[pointers[2]] = store
        index += 4
        return index

class permutationGenerator():
    def __init__(self, in_array):
        self.output = []
        self.length = len(in_array)
        for i in range(self.length):
            memArray = list(in_array)
            ith_el = [memArray.pop(i)]
            self.getPermutations(ith_el, memArray)
    
    def getOutput(self):
        return self.output

    def getPermutations(self, pop_array, remainder_array):
        if len(pop_array) == self.length:
            self.output.append(pop_array)
            return None
        else:
            for i in range(len(remainder_array)):
                memRemArray = list(remainder_array)
                memPopArray = list(pop_array)
                memPopArray.append(memRemArray.pop(i))
                self.getPermutations(memPopArray, memRemArray)


def main():
    with open('./07-Input') as file:
        instruction_array = list(map(int, file.read().split(',')))

    max_output = 0
    out_phases = None
    for permutation in permutationGenerator([i for i in range(5)]).getOutput():
        amplifiers = []
        for i in range(5):
            amplifiers.append(intCodeRunner(instruction_array, permutation[i]))
        amplifier_output = 0
        for amplifier in amplifiers:
            amplifier.addInput(amplifier_output)
            amplifier.run()
            amplifier_output = amplifier.output[0]
        if amplifier_output > max_output:
            max_output = amplifier_output
            out_phases = permutation
    print(out_phases, max_output)

if __name__ == "__main__":
    main()
