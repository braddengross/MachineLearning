import chapter3.trees as trees

myData, labels = trees.createDataSet()
print(myData)
print(trees.calcShannonEnt(myData))

#myData[0][-1] = 'maybe'
#print(myData)
#print(trees.calcShannonEnt(myData))


print(trees.splitDataSet(myData, 0, 0))