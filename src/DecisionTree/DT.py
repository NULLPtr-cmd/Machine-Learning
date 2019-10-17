from math import log


class DecisionTree:

    def __init__(self):
        self.decisionTree = {}

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

    def calcIV(self, dataSet):
        ivAns = []
        num = len(dataSet)
        numOfType = len(dataSet[0]) - 1
        for i in range(numOfType):
            feat = [f[i] for f in dataSet]
            feat = set(feat)
            ans = 0
            for val in feat:
                res = self.splitByFeature(dataSet, i, val)
                ans -= len(res) / float(num) * log((len(res)/float(num)))
                pass
            ivAns.append(ans)
            pass
        return ivAns


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

    def chooseBestFeature(self, dataSet, algo):
        if algo == 'ID3':
            num = len(dataSet)
            numOfType = len(dataSet[0]) - 1
            bestGain = 0
            for i in range(numOfType):
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
        
        if algo == 'C4.5':
            IV = self.calcIV(dataSet)
            num = len(dataSet)
            numOfType = len(dataSet[0]) - 1
            bestGainRatio = 0
            for i in range(numOfType):
                features = [example[i] for example in dataSet]
                features = set(features)
                ans = 0
                for val in features:
                    res = splitByFeature(dataSet, i, val)
                    ans += len(res) / float(num) * self.calcEntropy(res)
                    pass
                gain = self.calcEntropy(dataSet) - ans
                gainRatio = gain / IV[i]
                if(gainRatio >= bestGainRatio):
                    bestGainRatio = gainRatio
                    bestFeatures = i
                    pass

            return bestFeatures


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

        bestFeatOrder = self.chooseBestFeature(dataSet, 'ID3')
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

    def C4point5(self, dataSet, features):
        classList = [lable[-1] for lable in dataSet]
        if len(dataSet[0]) == 1:
            return self.chooseLabel(classList)
        if classList.count(classList[0]) == len(classList):
            return classList[0]

        bestFeatOrder = self.chooseBestFeature(dataSet, 'C4.5')
        bestFeat = features[bestFeatOrder]

        bestFeatType = [Type[bestFeatOrder] for Type in dataSet]
        bestFeatType = set(bestFeatType)
        decisionTree = {bestFeat: {}}

        for val in bestFeatType:
            newDataSet = self.splitByFeature(dataSet, bestFeatOrder, val)
            newFeatures = features[:bestFeatOrder]
            newFeatures.extend(features[bestFeatOrder+1:])
            decisionTree[bestFeat][val] = self.C4point5(
                newDataSet, newFeatures)
            pass

        return decisionTree
    
    def creatTree(self, dataSet, features, algo):
        if algo == 'ID3':
            self.decisionTree = self.ID3(dataSet, features)
        
        if algo == 'C4.5':
            self.decisionTree = self.C4point5(dataSet, features)