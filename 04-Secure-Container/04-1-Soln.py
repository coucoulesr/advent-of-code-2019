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
    """Takes an integer and returns a boolean reflecting if there exists a digit that repeats therein."""
    numstr = str(num)
    for i in range(len(numstr)):
        if i == len(numstr) - 1:
            break
        if int(numstr[i]) == int(numstr[i+1]):
            return True
    return False

def passwordBruteForce(start, stop):
    """Given start and stop integers bounding an input range, return a list of all integers in the range
    (inclusive of endpoints) whose digits don't decrease and contain a repeating digit."""
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
