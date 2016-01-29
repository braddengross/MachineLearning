

#ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
#ny['entries']
#print(len(ny['entries']))

def calculateMostFrequentValues(wordlist, fullText):
    import operator
    freqDict = {}
    for word in wordlist:
        freqDict[word] = fullText.count(word)
    print(operator.itemgetter(1)(freqDict.items()))
    sortedFreq = sorted(freqDict.items(), key=operator.itemgetter(1), reverse = True)
    #Return top 30
    return sortedFreq[:30]

def localWords(feed0, feed1):
    import feedparser
    import bayes
    docList=[]
    classList=[]
    fullText=[]
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['suma'])


