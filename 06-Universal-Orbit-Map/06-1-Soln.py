class Planet():
    """Planet object that holds value (name), parent, and children as class variables

    I didn't actually need any of the methods that deal with children but I coded them first
    so I kept them anyways."""

    def __init__(self, val, parent=None, *args):
        """Planet constructor: takes name, optional parent, optional children"""
        self.value = val
        self.setParent(parent)
        self.children = []
        for child in args:
            self.addChild(child)

    def setParent(self, parent):
        """Adds parent to Planet instance. Parent must be object of type Planet."""
        if isinstance(parent, Planet) or parent == None:
            self.parent = parent
        else:
            raise TypeError('Parent of Planet object must be of Planet type.')

    def addChild(self, child):
        """Adds child to Planet instance. Child must be object of type Planet."""
        if isinstance(child, Planet):
            self.children.append(child)
        else:
            raise TypeError('Child of Planet object must be of Planet type.')

    def totalDescendants(self):
        """Returns the total number of descendants of Planet instance."""
        total = 0
        for child in self.children:
            total += 1
            total += child.totalDescendants()
        return total
    
    def totalParents(self):
        """Returns the total number of Planets this Planet instance is a descendant of."""
        total = 0
        parent = self.parent
        while parent != None:
            temp = parent
            parent = temp.parent
            total += 1
        return total

    def __repr__(self):
        return str(self.value)


def main():
    planetDict = {}     # Using a dictionary was overkill for this problem.
    with open('./06-Input') as file:
        for line in file:
            parent, child = line.strip().split(')')
            for planet in (parent, child):
                if not planet in planetDict:
                    planetDict[planet] = Planet(planet)
            planetDict[parent].addChild(planetDict[child])
            planetDict[child].setParent(planetDict[parent])
    # Each Planet is in direct orbit of its parent and 
    #   in indirect orbit of each of its parent's parents.
    totalOrbits = 0
    for planet in planetDict.values():
        totalOrbits += planet.totalParents()
    print(totalOrbits)

if __name__ == "__main__":
    main()
