import math

def moduleFuelReq(mass):
    output = math.floor(mass/3) - 2
    return output if output > 0 else 0


def main():
    fuel_required = 0
    next_fuel = 0
    with open("01-input") as file:
        for line in file:
            next_fuel = moduleFuelReq(int(line))
            while next_fuel > 0:
                fuel_required += next_fuel
                next_fuel = moduleFuelReq(next_fuel)

    print(fuel_required)


if __name__ == "__main__":
    main()
