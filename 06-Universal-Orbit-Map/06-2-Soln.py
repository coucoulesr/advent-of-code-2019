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

    def getAllParents(self):
        """Returns an array of all Planet objects that Planet instance is a descendant of.
        
        Array is in ascending order."""
        parents = []
        parent = self.parent
        while parent != None:
            parents.append(parent)
            temp = parent
            parent = temp.parent
        return parents

    def getAllDescendants(self):
        """Returns an array of all Planet objects that descend from Planet instance.
        
        Array is populated in a depth-first manner"""
        children = []
        for child in self.children:
            children.append(child)
            for descendant in child.getAllDescendants():
                children.append(descendant)
        return children

    def totalDescendants(self):
        """Returns the total number of descendants of Planet instance."""
        return len(self.getAllDescendants())

    def totalParents(self):
        """Returns the total number of Planets this Planet instance is a descendant of."""
        return len(self.getAllParents())

    def __repr__(self):
        return str(self.value)


def main():
    planetDict = {}     # Using a dictionary was NOT overkill for this problem.
    with open('./06-Input') as file:
        for line in file:
            parent, child = line.strip().split(')')
            for planet in (parent, child):
                if not planet in planetDict:
                    planetDict[planet] = Planet(planet)
            planetDict[parent].addChild(planetDict[child])
            planetDict[child].setParent(planetDict[parent])
    myParents = planetDict['YOU'].getAllParents()
    santasParents = planetDict['SAN'].getAllParents()
    # The parent arrays are in ascending order of distance from the subject
    # Therefore the first object present in both arrays is the nearest common parent
    # The sum of the indices of the nearest common parent is the number of jumps required
    orbitalTransfers = 0
    for planet in myParents:
        if planet in santasParents:
            orbitalTransfers = myParents.index(planet) + santasParents.index(planet)
            break
    print(orbitalTransfers)


if __name__ == "__main__":
    main()
