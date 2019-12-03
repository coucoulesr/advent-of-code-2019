class WireGrid():
    def __init__(self, directionArray=[]):
        """Takes an array of directions and populates a dictionary with keys corresponding to (y, x) positions 
        the wire visits and values corresponding to the number of steps the wire takes to get there.
        """
        self.wirePosDict = {}
        pointer = [0, 0]
        steps = 0
        for direction in directionArray:
            instruction = direction[0].lower()
            length = int(direction[1:])
            # reads whether the instruction alters y (1st index) or x (2nd index) position.
            magnitude = 1 if instruction == "r" or instruction == "d" else -1
            # reads whether the instruction moves in positive (right/down) or negative (left/up) direction for given axis.
            direction = 1 if instruction == "l" or instruction == "r" else 0
            for i in range(length):
                steps += 1
                pointer[direction] += magnitude
                if not (tuple(pointer) in self.wirePosDict):
                    self.wirePosDict[tuple(pointer)] = steps

    def findCollisions(self, otherGrid):
        """Returns array of (y, x) positions both this wire and input other wire visit"""
        collisions = []
        for pos in self.wirePosDict:
            if pos in otherGrid.wirePosDict:
                collisions.append(pos)
        return collisions

    def shortestCollisionDistance(self, otherGrid):
        """Returns distance to collision with shortest distance from origin, 
        measured in Manhattan Distance (ie delta_x + delta_y)"""
        collisions = self.findCollisions(otherGrid)
        shortestCollisionDistance = 100**100
        for collision in collisions:
            collisionDistance = abs(collision[0]) + abs(collision[1])
            if collisionDistance < shortestCollisionDistance:
                shortestCollisionDistance = collisionDistance
        return shortestCollisionDistance

    def shortestCollisionSteps(self, otherGrid):
        """Returns total steps required for collision with fewest steps 
        taken by both wires (ie first collision seen by each wire)"""
        collisions = self.findCollisions(otherGrid)
        shortestCollisionSteps = 100**100
        for collision in collisions:
            thisWireSteps = self.wirePosDict[collision]
            otherWireSteps = otherGrid.wirePosDict[collision]
            totalSteps = thisWireSteps + otherWireSteps
            if totalSteps < shortestCollisionSteps:
                shortestCollisionSteps = totalSteps
        return shortestCollisionSteps


def main():
    # Test Case 1: Should return 610.
    # grid1 = WireGrid(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'])
    # grid2 = WireGrid(['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])

    # Test Case 2: Should return 410.
    # grid1 = WireGrid(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'])
    # grid2 = WireGrid(['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])

    with open("03-input") as file:
        dirArray1 = [i.strip() for i in file.readline().split(',')]
        dirArray2 = [i.strip() for i in file.readline().split(',')]

    grid1 = WireGrid(dirArray1)
    grid2 = WireGrid(dirArray2)

    print(grid1.shortestCollisionSteps(grid2))


if __name__ == "__main__":
    main()
