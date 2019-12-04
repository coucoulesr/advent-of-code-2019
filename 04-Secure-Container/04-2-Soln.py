def digitsDontDecrease(num):
    """Takes an integer and returns a boolean reflecting if the digits of the integer never decrease."""
    numstr = str(num)
    for i in range(len(numstr)):
        if i == len(numstr) - 1:
            break
        if int(numstr[i]) > int(numstr[i+1]):
            return False
    return True


def hasRepeatingDigit(num):
    """Takes an integer and returns a boolean reflecting if there exists a digit that repeats exactly once therein."""
    numstr = str(num)
    for i in range(len(numstr)):
        if i == len(numstr) - 1:
            break
        if int(numstr[i]) == int(numstr[i+1]):
            if i == 0:                  # if at the start of the number, don't check the digit before (out of bounds).
                if (numstr[i] == numstr[i+1] and numstr[i] != numstr[i+2]):
                    return True
            if i == len(numstr) - 2:    # if at the last two digits, don't check the digit after (out of bounds).
                if (numstr[i] == numstr[i+1] and numstr[i] != numstr[i-1]):
                    return True
            if (0 < i and i < len(numstr) - 2):
                if numstr[i-1] != numstr[i]:
                    differentNumBefore = True
                else:
                    differentNumBefore = False
                if numstr[i+2] != numstr[i]:
                    differentNumAfter = True
                else:
                    differentNumAfter = False   
                if (differentNumBefore and differentNumAfter):
                    return True         
    return False


def passwordBruteForce(start, stop):
    """Given start and stop integers bounding an input range, return a list of all integers in the range
    (inclusive of endpoints) whose digits don't decrease and contain a digit that repeats once."""
    outArray = []
    for guess in range(start, stop + 1):
        if (digitsDontDecrease(guess) and hasRepeatingDigit(guess)):
            outArray.append(guess)
    return outArray


def main():
    with open('04-input') as file:
        (start, stop) = map(int, file.read().split('-'))

    print(len(passwordBruteForce(start, stop)))


if __name__ == "__main__":
    main()
