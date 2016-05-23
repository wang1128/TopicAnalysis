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
import gensim
from gensim import corpora, models

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
    for idx in range(len(splitArtList) - 1):#分词系统, 要统计词
        seg_list = list(jieba.cut(articleList[idx][3])) # idx 3 is the content
        wordList = wordList + seg_list
    return wordList

def removeStopWord(seg_list):
    print len(seg_list)
    setOfword = set(seg_list)
    wList = list(setOfword)
    for word in wList:
        count = seg_list.count(word)
        if count> 2500 or count < 3: #还有另一种方法， 就是就是去除前面第一百个 和 后面的少数的 这个后面要改
            print word, count
            setOfword.remove(word)
    cleanWordList = list(setOfword)
    print cleanWordList
    return cleanWordList

def calLDA(numOfTopic, cleanWordList):
    dictionary = corpora.Dictionary(cleanWordList)
    corpus = [dictionary.doc2bow(text) for text in cleanWordList]
    print numOfTopic
    print len(corpus)
    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=numOfTopic, id2word = dictionary, passes=20)
    row = len(corpus)
    col = numOfTopic
    ldaFeatureSet = np.zeros((row,col))
    print(ldamodel.print_topics(num_topics=numOfTopic, num_words=10))

    for i in range(len(corpus)):
        for element in ldamodel[corpus[i]]:
            colNum =  int(element[0]) - 1
            colVaule = element[1]
            ldaFeatureSet[i][colNum] = colVaule
    for i in range(len(corpus)):
        print ldamodel[corpus[i]]
    return ldaFeatureSet


if __name__ == '__main__':
    articleList = loadfiles()
    seg_list = calWordList(articleList)  # total word in the word list
    cleanWordList = removeStopWord(seg_list)
    npWordList = np.array(cleanWordList,dtype=object)
    np.save('npWordList',npWordList)
    ldaFeatureSet150 = calLDA(150,cleanWordList)
    np.save('ldaFeatureSet150', ldaFeatureSet150)





    #for item in seg_list:
    #    if item != u'\uff1a':
     #       print item

    #print "Default Mode:", " ".join(seg_list)




