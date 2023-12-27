#!/usr/bin/python3
import numpy as np
import operator
import sys
from os import listdir

training_folder = sys.argv[1]
test_folder = sys.argv[2]


def convert(filename):
    vector = np.zeros((1, 1024))
    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
        return vector
               
def createDataSet(file):
    labels = []
    trainingDigits = listdir(file)
    m = len(trainingDigits)
    matrix = np.zeros((m, 1024))
    for i in range(m):
        f = trainingDigits[i]
        q = int(f.split('_')[0])
        labels.append(q)
        matrix[i, :] = convert(file + '/' + f)
    return matrix, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]        

testDigits = listdir(test_folder)
matrix, labels = createDataSet(training_folder)

for k in range(1, 21):
    cnt = 0
    error = 0
   
    for i in range(len(testDigits)):
        answer = int(testDigits[i].split('_')[0])
        testData = convert(test_folder + '/' + testDigits[i])
        result = classify0(testData, matrix, labels, k)
        if answer != result:
            error += 1
        cnt += 1
   
    print(int(error/cnt * 100))
