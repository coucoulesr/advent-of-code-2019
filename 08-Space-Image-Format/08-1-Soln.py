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
    
    print(numOnes * numTwos)


if __name__ == "__main__":
    main()
