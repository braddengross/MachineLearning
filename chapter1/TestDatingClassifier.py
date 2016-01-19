import chapter1.dataUtility as du
import chapter1.kNearestNeighbors as kNN
import numpy as np

def datingClassTest():
    #amount of data to use for testing
    hoRatio = 0.10
    #convert file to matrix and labels
    datingDataMat, datingLabels = du.fileToMatrix("/Users/brad/PycharmProjects/machineLearning/data/datingTestSet.txt")
    #normalize the matrix
    normMat, ranges, minVals = du.autoNorm(datingDataMat)
    #count of observations
    m = normMat.shape[0]
    #count of observations for validation
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        #Loop through and test vectors 1 - amount of tests against model created with amount of tests - total
        classifierResult = kNN.classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if(classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))


#datingClassTest()


def classifyPerson():
    resultList = ["not at all", "in small doses", "in large doses"]
    percentTats = float(input("percentage of time spent playing video games? "))
    ffMiles = float(input("frequent flyer miles earned per year?" ))
    iceCream = float(input("liters of ice cream consumed per year? "))
    datingDataMat, datingLabels = du.fileToMatrix("/Users/brad/PycharmProjects/machineLearning/data/datingTestSet.txt")
    norMat, ranges, minVals = du.autoNorm(datingDataMat)
    inArr = np.asarray([ffMiles, percentTats, iceCream])
    classifierResult = kNN.classify0((inArr-minVals)/ranges, norMat, datingLabels, 3)
    print("You will probably like this person: ", resultList[classifierResult - 1])

classifyPerson()