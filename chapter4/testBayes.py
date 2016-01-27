import chapter4.bayes as bayes
from numpy import *
import re

#listOfPosts, listClasses = bayes.loadDataSet()
#myVocabList = bayes.createVocabList(listOfPosts)

trainMatrix=[]
#for post in listOfPosts:
#    trainMatrix.append(bayes.setOfWordsToVector(myVocabList, post))

#p0, p1, pAbusive = bayes.trainNB(trainMatrix, listClasses)
#print(pAbusive)
#print(p0)
#print(p1)

def testingNB():
    listOfPosts, listClasses = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(listOfPosts)
    trainMatrix = []
    for post in listOfPosts:
        trainMatrix.append(bayes.setOfWordsToVector(myVocabList, post))
    p0,p1, pAbusive = bayes.trainNB(array(trainMatrix), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(bayes.setOfWordsToVector(myVocabList, testEntry))
    print(testEntry, 'classified as: ', bayes.classifyNB(thisDoc, p0, p1, pAbusive))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(bayes.setOfWordsToVector(myVocabList, testEntry))
    print(testEntry, 'classified as: ', bayes.classifyNB(thisDoc, p0, p1, pAbusive))

def splitAndLowercaseTokens(listOfTokens):
    regex = re.compile("\\W*")
    listOfTokens = regex.split(listOfTokens)
    print([tok.lower() for tok in listOfTokens if len(tok) > 0])


#testingNB()
bayes.spamTest()
