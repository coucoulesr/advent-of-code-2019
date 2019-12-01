import math

def moduleFuelReq(mass):
    return math.floor(mass/3) - 2

def main():
    sum = 0
    with open("01-input") as file:
        for line in file:
            sum += moduleFuelReq(int(line))
    print(sum)

if __name__ == "__main__":
    main()