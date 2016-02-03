def loadDataSet():
    dataMatrix = []
    labelMatrix = []
    fr = open('../data/testSet.txt')
    for line in fr.readlines():
        lineArray = line.strip().split()
        dataMatrix.append(1.0, float(lineArray[0]), float(lineArray[1]))
        labelMatrix.append(int(lineArray[2]))
    return dataMatrix, labelMatrix

