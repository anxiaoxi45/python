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

    showNum = 500

    #plt.figure(figsize=(16,9))

    filename1 = "h_new.txt"
    dataL = readData(filename1)
    x = dataL[:showNum,0]
    y = [float(d)/632*100 for d in dataL[:showNum,2]]
    plt.plot(x, y, 'bo')
    plt.plot(x, y, 'b-')





    # 右下角说明
    plt.plot([showNum*0.87], [10], 'bo', [showNum*0.85,showNum*0.89], [10,10], 'b-')
    plt.text(showNum*0.9, 10, 'HSV')


    # 坐标
    plt.axis([0,showNum,0,100]) #坐标范围
    plt.xlabel('Rank')
    plt.ylabel('Matching Rate(%)')

    # 刻度值
    ax=plt.gca()
    ax.set_yticks(np.arange(0,105,5))
    ax.set_xticks(np.arange(0,showNum+1,50))

    # 虚线
    for i in range(0,100,10):
        plt.plot([0,15], [i,i], 'k:')

    plt.title('CMC curves')
    plt.savefig('CMC curves')
    plt.show()