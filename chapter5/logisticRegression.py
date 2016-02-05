from numpy import *

def loadDataSet():
    dataMatrix = []
    labelMatrix = []
    fr = open('../data/testSet.txt')
    for line in fr.readlines():
        lineArray = line.strip().split()
        dataMatrix.append([1.0, float(lineArray[0]), float(lineArray[1])])
        labelMatrix.append(int(lineArray[2]))
    return dataMatrix, labelMatrix

def sigmoid(inX):
    return 1.0 / (1+exp(-inX))

def gradientAscent(dataMatrix, classLabels):
    dataMatrix = matrix(dataMatrix)
    labelMatrix = matrix(classLabels).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)
        error = labelMatrix - h
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights

