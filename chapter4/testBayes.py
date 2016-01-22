import chapter4.bayes as bayes

listOfPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOfPosts)
print(myVocabList)

print(bayes.setOfWordsToVector(myVocabList, listOfPosts[0]))
print(bayes.setOfWordsToVector(myVocabList, listOfPosts[3]))