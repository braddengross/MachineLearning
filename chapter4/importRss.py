import chapter4.bayes as bayes

#ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
#ny['entries']
#print(len(ny['entries']))

def calculateMostFrequentValues(wordlist, fullText):
    import operator
    freqDict = {}
    for word in wordlist:
        freqDict[word] = fullText.count(word)
    #print(operator.itemgetter(1)(freqDict.items()))
    sortedFreq = sorted(freqDict.items(), key=operator.itemgetter(1), reverse = True)
    #Return top 30
    return sortedFreq[:30]

def localWords(feed0, feed1):
    import feedparser
    import numpy as np
    docList=[]
    classList=[]
    fullText=[]
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(minLen):
        wordList = bayes.textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = bayes.textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = bayes.createVocabList(docList)
    top30Words = calculateMostFrequentValues(vocabList, fullText)
    for pairW in top30Words:
        if pairW[0] in vocabList: vocabList.remove(pairW[0])
    trainingset = list(range(2*minLen))
    testSet = []
    for i in range(20):
        randIndex = int(np.random.uniform(0, len(trainingset)))
        testSet.append(trainingset[randIndex])
        del(trainingset[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingset:
        trainMat.append(bayes.bagOfWordsToVetor(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0v, p1v, pSpam = bayes.trainNB(np.asarray(trainMat), np.asarray(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = bayes.bagOfWordsToVetor(vocabList, docList[docIndex])
        if bayes.classifyNB(np.asarray(wordVector), p0v, p1v, pSpam) != classList[docIndex]:
            errorCount +=1
    print('the error rate is: ', float(errorCount)/len(testSet))
    return vocabList, p0v, p1v








