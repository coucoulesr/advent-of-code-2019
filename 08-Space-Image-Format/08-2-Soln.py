def imageBuilder(inputStr, w, h):
    """Given a transmission string, image width, and image height, returns an array representing a Space Image Format image.
    
    Each element of the array is an array representing a layer. 
    Each layer array is an array of rows with the value of the pixel at the corresponding index of the row.
    Thus an element on a given layer with given x,y coordinates (0-indexed, measured from top-left) is accessed as such:
        imageArray[layer][y][x]
    """
    x, y, image, layer, line = 0, 0, [], [], []
    for px in inputStr:
        if x < w:
            line.append(int(px))
            x += 1
        elif x == w:
            layer.append(line)
            line = []
            line.append(int(px))
            x = 1
            y += 1
            if y == h:
                image.append(layer)
                y, layer = 0, []
    layer.append(line)
    image.append(layer)
    return image


def imageParser(image):
    """Given a Space Image Format array, returns an array that represents the rendered image.
    
    
    The value of each position in the returned rectangular array correspondes to a color as follows:
        1: black, 0: white, -1: no color (transparent)
    """
    w = len(image[0][0])
    h = len(image[0])
    render = []
    for y in range(h):
        line = []
        for x in range(w):
            line.append(-1)
        render.append(line)
    for layer in image:
        for (y, row) in enumerate(layer):
            for (x, item) in enumerate(row):
                if item in (0, 1) and render[y][x] == -1:
                    render[y][x] = item
    return render


def main():
    with open('08-Input') as file:
        input = str(file.read()).strip()

    image = imageBuilder(input, 25, 6)
    fewestZeros = 2**32
    numOnes = 0
    numTwos = 0
    for layer in image:
        layerDict = {}
        for row in layer:
            for item in row:
                if not item in layerDict:
                    layerDict[item] = 1
                else:
                    layerDict[item] += 1
        if layerDict[0] < fewestZeros:
            fewestZeros = layerDict[0]
            numOnes = layerDict[1]
            numTwos = layerDict[2]
    print('Part 1:', numOnes * numTwos)

    render = imageParser(image)
    print('\nPart 2:')
    for row in render:
        for item in row:
            if item == -1:
                print(u'\u2591', end='')
            elif item == 0:
                print(u'\u2592', end='')
            elif item == 1:
                print(u'\u2593', end='')
        print('')


if __name__ == "__main__":
    main()
