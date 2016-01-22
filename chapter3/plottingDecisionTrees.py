import matplotlib.pyplot as plt
import chapter3.trees as trees

decisionNode = dict(boxstyle="sawtooth", fc=".8")
leafNode = dict(boxstyle="round4", fc=".8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeText, centerPoint, parentPoint, nodeType):
    createPlot.ax1.annotate(nodeText, xy=parentPoint, xycoords='axes fraction',
        xytext=centerPoint, textcoords='axes fraction',
        va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (.8, .1), (.3, .8), leafNode)
    plt.show()

def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers':
                    {0: 'no', 1: 'yes'}}}},
                        {'no surfacing': {0: 'no', 1: {'flippers':
                            {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]

def plotMidText(centerPoint, parentPoint, textString):
    xMid = (parentPoint[0]-centerPoint[0]) / 2.0 + centerPoint[0]
    yMid = (parentPoint[1]-centerPoint[1]) / 2.0 + centerPoint[1]
    createPlot.ax1.text(xMid, yMid, textString, va="center", ha="center", rotation=5)

def plotTree(myTree, parentPoint, nodeText):
    numLeafs = trees.getNumberofLeafs(myTree)
    depth = trees.getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    centerPoint = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(centerPoint, parentPoint, nodeText)
    plotNode(firstStr, centerPoint, parentPoint, decisionNode)
    secondDict =  myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    if(plotTree.yOff == 0) :
        print("problem")
    for key in secondDict.keys():
        plt.show()
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key], centerPoint, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), centerPoint, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), centerPoint, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def createPlot(inTree):
    fig = plt.figure(1, facecolor="white")
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(trees.getNumberofLeafs(inTree))
    plotTree.totalD = float(trees.getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW;
    plotTree.yOff = 1.0;
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()



