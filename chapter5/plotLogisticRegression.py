import chapter5.logisticRegression as lr
import numpy as np

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMatrix, labelMatrix = lr.loadDataSet()
    dataArray = np.asarray(dataMatrix)
    n = np.shape(dataArray)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMatrix[1]) == 1:
            xcord1.append(dataArray[i, 1])
            ycord1.append(dataArray[i, 2])
        else:
            xcord2.append(dataArray[1, i])
            ycord2.append(dataArray[2, i])
    fig = plt.figure()


