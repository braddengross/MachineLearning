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

def bagOfWordsToVetor(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def trainNB(trainingMatrix, trainingCatgories):
    numberOfTrainingDocs = len(trainingMatrix)
    numberOfWords = len(trainingMatrix[0])
    pAbusive = sum(trainingCatgories) / float(numberOfTrainingDocs)
    p0Numerator = np.ones(numberOfWords)
    p1Numerator = np.ones(numberOfWords)
    p0Denominator = 2.0
    p1Denominator = 2.0
    for i in range(numberOfTrainingDocs):
        if trainingCatgories[i] == 1:
            p1Numerator += trainingMatrix[i]
            p1Denominator += sum(trainingMatrix[i])
        else:
            p0Numerator += trainingMatrix[i]
            p0Denominator += sum(trainingMatrix[i])
    p1Vect = np.log(p1Numerator / p1Denominator)
    p0Vect = np.log(p0Numerator / p0Denominator)
    return p0Vect, p1Vect, pAbusive

def classifyNB(vectorToClassify, p0Vector, p1Vector, pClass1):
    p1 = sum(vectorToClassify * p1Vector) + np.log(pClass1)
    p0 = sum(vectorToClassify * p0Vector) + np.log(1-pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
    docList=[]
    classList=[]
    fullText=[]
    for i in range(1,26):
        wordList = textParse(open('../data/email/spam/%d.txt' % i, encoding='utf-8', errors='ignore').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('../data/email/ham/%d.txt' % i, encoding='utf-8', errors='ignore').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):
        randIndex = int(np.random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWordsToVector(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0v, p1v, pSpam = trainNB(np.array(trainMat), np.array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWordsToVector(vocabList, docList[docIndex])
        if classifyNB(np.array(wordVector), p0v, p1v, pSpam) != classList[docIndex]:
            errorCount += 1
    print("The error rate is: ", float(errorCount)/len(testSet))


