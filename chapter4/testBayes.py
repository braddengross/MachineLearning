import chapter4.bayes as bayes

listOfPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOfPosts)

trainMatrix=[]
for post in listOfPosts:
    trainMatrix.append(bayes.setOfWordsToVector(myVocabList, post))

p0, p1, pAbusive = bayes.trainNB(trainMatrix, listClasses)
print(pAbusive)
print(p0)
print(p1)

