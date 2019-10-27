import numpy as np
import pandas as pd
import random
from math import log


class RandomForest:
    def __init__(self, dataSet, k, num):
        self.RF = []
        self.Data = np.mat(dataSet)
        self.num = k
        self.numOfTree = num

    def generateDataSet(self):
        DataSet = []
        for i in range(self.Data.shape[0]):
            a = random(0, self.Data.shape[0])
            DataSet.append(self.Data[a, :])
        return DataSet

    def calcEntropy(self, dataSet):
        num = len(dataSet)
        typeofData = {}
        for feavec in dataSet:
            lable = feavec[-1]
            if lable not in typeofData.keys:
                typeofData[lable] = 1
                pass
            else:
                typeofData[lable] += 1
                pass
            pass
        ent = 0
        for key in typeofData:
            ent -= (float(typeofData[key]/num) *
                    log(float(typeofData[key]/num, 2)))
            pass
        return ent

    def splitByFeature(self, dataSet, aixs, value):
        retSet = []
        retVec = []
        for feavec in dataSet:
            if feavec[aixs] == value:
                retVec = feavec[:aixs]
                retVec.extend(feavec[aixs+1:])
                retSet.append(retVec)
                pass
            pass
        return retSet

    def chooseLabel(self, classList):
        classCount = {}
        for lable in classList:
            if lable not in classCount.keys():
                classCount[lable] = 1
                pass
            else:
                classCount[lable] += 1
                pass
            pass

        sortedClass = sorted(
            classCount.items, key=lambda d: d[1], reverse=True)
        return sortedClass[0][0]

    def ID3(self, dataSet, features):
        classList = [lable[-1] for lable in dataSet]
        if len(dataSet[0]) == 1:
            return self.chooseLabel(classList)
        if classList.count(classList[0]) == len(classList):
            return classList[0]

        bestFeatOrder = self.chooseBestFeature(dataSet)
        bestFeat = features[bestFeatOrder]

        bestFeatType = [Type[bestFeatOrder] for Type in dataSet]
        bestFeatType = set(bestFeatType)
        decisionTree = {bestFeat: {}}

        for val in bestFeatType:
            newDataSet = self.splitByFeature(dataSet, bestFeatOrder, val)
            newFeatures = features[:bestFeatOrder]
            newFeatures.extend(features[bestFeatOrder+1:])
            decisionTree[bestFeat][val] = self.ID3(
                newDataSet, newFeatures)
            pass

        return decisionTree

    def chooseBestFeature(self, dataSet):
        num = len(dataSet)
        numOfType = min((len(dataSet[0]) - 1), self.num)
        randomFeature = random.sample(range(0, len(dataSet[0]-1)), numOfType)
        bestGain = 0
        for i in randomFeature:
            features = [example[i] for example in dataSet]
            features = set(features)
            ans = 0
            for val in features:
                res = splitByFeature(dataSet, i, val)
                ans += len(res) / float(num) * self.calcEntropy(res)
                pass
            gain = self.calcEntropy(dataSet) - ans
            if(gain >= bestGain):
                bestGain = gain
                bestFeatures = i
                pass

        return bestFeatures

    def trainDT(self):
