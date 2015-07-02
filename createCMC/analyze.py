#coding:utf-8
__author__ = 'Zhmxu'
# Created by Zhmxu on 2015/6/27.

import re

def readTestData(filename):
    with open(filename) as fd:
        lines = [_.strip() for _ in fd.readlines()]

    pattern1 = re.compile(r'<1>(\d+)\.(\d+)/')
    pattern2 = re.compile(r'<0>(\d+)\.(\d+)/')

    result = []

    for line_ in lines:
        match1 = pattern1.search(line_)
        str_ = match1.group()
        posLoss = float(str_[3:-1])
        match2 = pattern2.findall(line_)
        negLoss = [float(t[0]+'.'+t[1]) for t in match2]
        negLoss = sorted(negLoss)

        result.append([posLoss, negLoss])

    return result

def saveResult(data, filename):
    fout = open(filename, 'wt')
    numSamples = len(data)
    for i in range(numSamples):
        neg = data[i][1]
        negstr = ""
        for j in range(len(neg)):
            negstr = negstr + str(neg[j]) + " "
        print >> fout, "pos:" + str(data[i][0]) + " neg:" + negstr


    smallThen = [0]*632
    print >> fout, "\n\n\n\n\n\n\n\n some wrong:\n"
    for i in range(numSamples):
        posLoss = data[i][0]
        negLoss = data[i][1]
        num = 0

        if (negLoss[0] < posLoss):  #some wrong
            negstr = ""
            for j in range(len(negLoss)):
                if (negLoss[j] < posLoss):
                    negstr = negstr + str(negLoss[j]) + " "
                else:
                    num = j
                    break
            smallThen[num] = smallThen[num] + 1
            print >> fout, "pos:" + str(data[i][0]) + " neg:" + negstr
        else:
            smallThen[0] = smallThen[0] + 1


    # total = 0
    # for i in range(len(smallThen)):
    #     total = total + smallThen[i]
    print >> fout, "\n\n\n rank:   (total num:" + str(numSamples) + ")\n"
    accumulated = 0
    for i in range(len(smallThen)):
        if ((i > 50) & (smallThen[i] == 0)):
            continue
        accumulated = accumulated + smallThen[i]
        print >> fout, str(i+1) + ": " + str(smallThen[i]) + \
                       "  " + str(100*float(smallThen[i])/numSamples) +"%" + \
            "  " + str(accumulated) + "  " + str(100*float(accumulated)/numSamples) +"%"

    fout.close()


def meanData(filename1, filename2, savename):
    data1 = readTestData(filename1)
    data2 = readTestData(filename2)

    numSamples = len(data1)
    meandata = []
    for i in range(numSamples):
        posLoss = (data1[i][0] + data2[i][0])/2
        negLoss = [(x+y)/2 for (x,y) in zip(data1[i][1], data2[i][1])]
        meandata.append([posLoss, negLoss])

    fout = open(savename, 'wt')
    for i in range(numSamples):
        neg = meandata[i][1]
        negstr = ""
        for j in range(len(neg)):
            negstr = negstr + str(neg[j]) + " "
        print >> fout, "pos:" + str(meandata[i][0]) + " neg:" + negstr
    fout.close()

    return meandata

def Norm(data):
    numSamples = len(data)

    for i in range(numSamples):
        sum_ = data[i][0]
        sum_ = sum_ + sum(data[i][1])

        data[i][0] = data[i][0]/sum_
        for j in range(len(data[i][1])):
            data[i][1][j] = data[i][1][j] / sum_
    return data

def meanDataNorm(filename1, filename2, savename):
    data1 = readTestData(filename1)
    data2 = readTestData(filename2)

    data1 = Norm(data1)
    data2 = Norm(data2)

    numSamples = len(data1)
    meandata = []
    for i in range(numSamples):
        posLoss = (data1[i][0] + data2[i][0])/2
        negLoss = [(x+y)/2 for (x,y) in zip(data1[i][1], data2[i][1])]
        meandata.append([posLoss, negLoss])

    fout = open(savename, 'wt')
    for i in range(numSamples):
        neg = meandata[i][1]
        negstr = ""
        for j in range(len(neg)):
            negstr = negstr + str(neg[j]) + " "
        print >> fout, "pos:" + str(meandata[i][0]) + " neg:" + negstr
    fout.close()

    return meandata



# 取两者较小值
def smallData(filename1, filename2, savename):
    data1 = readTestData(filename1)
    data2 = readTestData(filename2)

    data1 = Norm(data1)
    data2 = Norm(data2)

    numSamples = len(data1)
    meandata = []
    for i in range(numSamples):
        posLoss = data1[i][0] if (data1[i][0] > data2[i][0]) else data2[i][0]
        negLoss = [x if (x>y) else y for (x,y) in zip(data1[i][1], data2[i][1])]
        meandata.append([posLoss, negLoss])

    fout = open(savename, 'wt')
    for i in range(numSamples):
        neg = meandata[i][1]
        negstr = ""
        for j in range(len(neg)):
            negstr = negstr + str(neg[j]) + " "
        print >> fout, "pos:" + str(meandata[i][0]) + " neg:" + negstr
    fout.close()

    return meandata

def getMean():
    filename1 = r'D:\Linux\caffe-master-5.13\caffe-master-5.13\examples\h\h_small_test_loss_CMC.txt'
    filename2 = r'D:\Linux\caffe-master-6.24\examples\l0\l3_small_test_loss_CMC.txt'
    savename = 'meandata.txt'

    # mean = meanDataNorm(filename1, filename2, savename)
    small = smallData(filename1, filename2, 'largedata.txt')
    saveResult(small, 'largeresult.txt')

if __name__ == '__main__':
    getMean()
    # filename = r'D:\Linux\caffe-master-6.24\examples\h\loss_h_test_CMC.txt'
    # data = readTestData(filename)
    # savefilename = r'D:\Linux\caffe-master-6.24\examples\h\resultAnalysis.txt'
    # saveResult(data, savefilename)

