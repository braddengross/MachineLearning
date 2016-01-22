import chapter3.trees as trees
import chapter3.plottingDecisionTrees as treePlot

fr = open("../data/lenses.txt")
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels=['age', 'prescript', 'astigmatic', 'tearrate']
lensesTree = trees.createTree(lenses, lensesLabels)

print(lensesTree)

treePlot.createPlot(lensesTree)