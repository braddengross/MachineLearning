import numpy as np
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
            ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
            ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
            ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
            ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
            ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]

    classificationVector = [0,1,0,1,0,1]
    return postingList, classificationVector

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWordsToVector(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print("the word: %s is not in my vocabulary!" % word)
    return returnVec

def trainNB(trainingMatrix, trainingCatgories):
    numberOfTrainingDocs = len(trainingMatrix)
    numberOfWords = len(trainingMatrix[0])
    pAbusive = sum(trainingCatgories) / float(numberOfTrainingDocs)
    p0Numerator = np.zeros(numberOfWords)
    p1Numerator = np.zeros(numberOfWords)
    p0Denominator = 0.0
    p1Denominator = 0.0
    for i in range(numberOfTrainingDocs):
        if trainingCatgories[i] == 1:
            p1Numerator += trainingMatrix[i]
            p1Denominator += sum(trainingMatrix[i])
        else:
            p0Numerator += trainingMatrix[i]
            p0Denominator += sum(trainingMatrix[i])
    p1Vect = p1Numerator / p1Denominator
    p0Vect = p0Numerator / p0Denominator
    return p0Vect, p1Vect, pAbusive

