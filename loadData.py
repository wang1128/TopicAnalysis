# author: Penghao Wang
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
 * ${导入数据 并清洗数据 from 36kr}
 #
 * @version V1.0
 * @Author Penghao Wang
 * @Create ${2016.5.18} ${10:46}
 * @Copyright: Copyright 2016 zhizhu Technology
'''

import jieba
import numpy as np

def loadfiles():
    f = open('result_fetch.txt', 'r')
    articleList = []
    splitArtList = []  #每一篇文章分为 4个部分 index0 : url, index 1 : time, index 2: title, index 3 : content

    for line in f:
        articleList.append(line)
    for idx,article in enumerate(articleList):
        content = articleList[idx]
        splitContent = content.split('\t')
        splitArtList.append(splitContent)

    return splitArtList




if __name__ == '__main__':
    articleList = loadfiles()
    print articleList[0][2]
    seg_list = jieba.cut(articleList[0][2])
    print "Default Mode:", " ".join(seg_list)




