import chapter3.trees as trees
import chapter3.plottingDecisionTrees as treePlot

print(treePlot.retrieveTree(1))

#myTree = treePlot.retrieveTree(0)
#myTree['no surfacing'][3] = 'maybe'
#treePlot.createPlot(myTree)

myData, labels = trees.createDataSet()
myTree = treePlot.retrieveTree(0)
print(trees.classify(myTree, labels, [1,0]))
print(trees.classify(myTree, labels, [1,1]))

