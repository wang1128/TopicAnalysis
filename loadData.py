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

def calWordList(splitArtList):
    wordList = []
    for idx in range(len(splitArtList) - 1):
        seg_list = list(jieba.cut(articleList[idx][3])) # idx 3 is the content
        wordList = wordList + seg_list
    return wordList

if __name__ == '__main__':
    articleList = loadfiles()
    #print articleList[0][2]
    #seg_list = list(jieba.cut(articleList[0][3])) #分词系统, 要统计词
    #print seg_list
    #print len(articleList)
    seg_list = calWordList(articleList)  # total word in the word list
    print len(seg_list)
    setOfword = set(seg_list)
    wList = list(setOfword)
    for word in wList:
        if seg_list.count(word)> 3000:
            print word

    #for item in seg_list:
    #    if item != u'\uff1a':
     #       print item

    #print "Default Mode:", " ".join(seg_list)




