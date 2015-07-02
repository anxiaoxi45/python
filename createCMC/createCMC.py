#coding:utf-8
__author__ = 'Zhmxu'
# Created by Zhmxu on 2015/6/27.

def readData(filenameA, filenameB):
    with open(filenameA) as fd:
        listA = [_.strip() for _ in fd.readlines()]
    with open(filenameB) as fd:
        listB = [_.strip() for _ in fd.readlines()]

    presonPair = []
    for i in range(len(listA)):
        idx = listA[i].find('_')
        if cmp(listA[i][:idx], listB[i][:idx]) == 0:
            presonPair.append([listA[i], listB[i]])

    return presonPair


def createCMCpair(data, savefilename):
    pathA = 'dataset1/viper_cama/c/'
    pathB = 'dataset1/viper_camb/c/'
    fout = open(savefilename, 'wt')
    for i in range(len(data)):
        print >>fout, pathA+data[i][0] + ' ' + pathB+data[i][1] + ' 1'
        print data[i][0]
        for j in range(len(data)):
            if j != i:
                print >>fout, pathA+data[i][0] + ' ' + pathB+data[j][1] + ' 0'

    fout.close()


if __name__ == '__main__':
    listFileNameA = r'E:\Data\siameseDATA\15.01.12\dataset1\viper_cama_c.txt'
    listFileNameB = r'E:\Data\siameseDATA\15.01.12\dataset1\viper_camb_c.txt'
    savefile = r'E:\Data\siameseDATA\15.01.12\dataset1\viper_CMC.txt'
    data = readData(listFileNameA, listFileNameB)
    createCMCpair(data, savefile)