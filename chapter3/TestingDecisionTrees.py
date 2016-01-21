import chapter3.trees as trees

myData, labels = trees.createDataSet()

print(trees.chooseBestFeatureToSplit(myData))
print(myData)