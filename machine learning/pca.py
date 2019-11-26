# encoding:utf=8

from numpy import *

def pca(dataMat, topNfeat=99999999):
    meanVals = mean(dataMat, axis=0)
    print(meanVals)
    meanRemoved = dataMat - meanVals
    print(meanRemoved)
    covMat = cov(meanRemoved, rowvar=0)#计算协方差
    print(covMat)
    eigVals, eigVects = linalg.eig(mat(covMat)) #计算出特征值和特征向量
    print(eigVals, eigVects)
    eigValInd = argsort(eigVals) #从小到大排序，返回的是index
    eigValInd = eigValInd[:-(topNfeat+1):-1] #对eigVals逆序排序得到topN个
    redEigVects = eigVects[:, eigValInd]
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat

if __name__ == "__main__":
    matrix = mat([[1,2,3,4],[2,2,3,4],[3,2,3,4]])
    lowDDataMat, reconMat = pca(matrix, 1)
    print(lowDDataMat)
    print(reconMat)