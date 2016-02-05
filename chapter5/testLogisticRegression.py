import chapter5.logisticRegression as lr

dataArray, labelMatrix = lr.loadDataSet()
weights = lr.gradientAscent(dataArray, labelMatrix)
print(weights)
