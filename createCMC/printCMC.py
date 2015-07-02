#coding:utf-8
__author__ = 'Zhmxu'
# Created by Zhmxu on 2015/6/29.
import matplotlib.pyplot as plt
import numpy as np
def readData(file):
    with open(file) as fd:
        lines_ = [_.strip() for _ in fd.readlines()]
    data = []
    for line_ in lines_:
        strs = line_.split(' ')
        linedata = [int(strs[0][:-1]), int(strs[1]), int(strs[5])]
        data.append(linedata)

    return np.array(data)
    # return data


if __name__ == '__main__':

    showNum = 15

    #plt.figure(figsize=(16,9))

    filename1 = "datal.txt"
    dataL = readData(filename1)
    lx = dataL[:showNum,0]
    ly = [float(d)/632*100 for d in dataL[:showNum,2]]
    plt.plot(lx, ly, 'bo')
    plt.plot(lx, ly, 'b-')



    filename2 = "datah.txt"
    dataH = readData(filename2)
    hx = dataH[:showNum,0]
    hy = [float(d)/632*100 for d in dataH[:showNum,2]]
    plt.plot(hx, hy, 'ro')
    plt.plot(hx, hy, 'r-')



    dataMean0 = readData("small.txt")
    mx0 = dataMean0[:showNum,0]
    my0 = [float(d)/632*100 for d in dataMean0[:showNum,2]]
    plt.plot(mx0, my0, 'go')
    plt.plot(mx0, my0, 'g-.')

    dataMean1 = readData("large.txt")
    mx1 = dataMean1[:showNum,0]
    my1 = [float(d)/632*100 for d in dataMean1[:showNum,2]]
    plt.plot(mx1, my1, 'mo')
    plt.plot(mx1, my1, 'm-.')


    dataMean = readData("mean.txt")
    mx = dataMean[:showNum,0]
    my = [float(d)/632*100 for d in dataMean[:showNum,2]]
    plt.plot(mx, my, 'ko')
    plt.plot(mx, my, 'k-')


    # 右下角说明
    dot_x = [10.5]  #点的位置，X轴
    # dot_y = [10]
    line_x = [10,11]     #线的位置，

    plt.plot(dot_x, [10], 'bo', line_x, [10,10], 'b-')
    plt.text(12, 10, 'LBP')

    plt.plot(dot_x, [15], 'ro', line_x, [15,15], 'r-')
    plt.text(12, 15, 'HSV')

    plt.plot(dot_x, [20], 'ko', line_x, [20,20], 'k-')
    plt.text(12, 20, 'LBP+HSV(mean)')

    plt.plot(dot_x, [25], 'go', line_x, [25,25], 'g-')
    plt.text(12, 25, 'LBP+HSV(small)')

    plt.plot(dot_x, [30], 'mo', line_x, [30,30], 'm-')
    plt.text(12, 30, 'LBP+HSV(large)')

    # 坐标
    plt.axis([0,showNum,0,100]) #坐标范围
    plt.xlabel('Rank')
    plt.ylabel('Matching Rate(%)')

    # 刻度值
    ax=plt.gca()
    ax.set_yticks(np.arange(0,105,5))
    ax.set_xticks(np.arange(0,16,1))

    # 虚线
    for i in range(0,100,10):
        plt.plot([0,15], [i,i], 'k:')

    plt.title('CMC curves')
    plt.savefig('CMC curves')
    plt.show()