import chapter3.trees as trees
import chapter3.plottingDecisionTrees as treePlot

myData, labels = trees.createDataSet()
print(myData)
print(trees.createTree(myData,labels))
treePlot.createPlot()
