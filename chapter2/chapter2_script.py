import chapter2.kNearestNeighbors as kNN
import chapter2.dataUtility as du
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

group, labels = kNN.createDataset()

print(group)
print(labels)

print(kNN.classify0([0, 0], group, labels, 3))

print(os.path.split(__file__))

datingDataMat, datingLabels = du.fileToMatrix("/Users/brad/PycharmProjects/machineLearning/data/datingTestSet.txt")

print(datingDataMat)
print(datingLabels[0:20])


fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*np.asarray(datingLabels), 15.0*np.asarray(datingLabels))
plt.show()

normMat, ranges, minVals = du.autoNorm(datingDataMat)
print(normMat)
print(ranges)
print(minVals)



