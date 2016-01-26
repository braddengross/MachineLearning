import numpy as np

def fileToMatrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    #Example of tuple unpacking
    returnMat = np.zeros((numberOfLines, 3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        #Fill in the return matrix line by line for all columns in the matrix but not the class
        returnMat[index, :] = listFromLine[0:3]
        #Add the class from the input
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    #Shape gives you rows followed by columns
    m = normDataSet.shape[0]
    #Subtract the minimum values from each value
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    #Divide each ralue by the range
    normDataSet = normDataSet/np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


