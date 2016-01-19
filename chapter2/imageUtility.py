import numpy as np

def imageToVector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect

testVector = imageToVector('../data/digits/testDigits/0_13.txt')
print(testVector[0, 0:31])
print(testVector[0, 32:63])

