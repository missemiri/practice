#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:42:22 2020

@author: emirimorita
"""

from gensim.models import word2vec
import logging
import sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

text_all = open('text_all.txt')
sentences = word2vec.LineSentence(text_all)
model = word2vec.Word2Vec(sentences,
                          sg=1,
                          size=100,
                          min_count=1,
                          window=10,
                          hs=1,
                          negative=0)

#keywordに似ている言葉を抽出 
sim_do = model.wv.most_similar(positive=["python"], topn=30)
## UNRESOLVED ERROR -> KeyError: "word 'python' not in vocabulary"


# リスト化されているので、見やすいように整形
print(*[" ".join([v, str("{:.5f}".format(s))]) for v, s in sim_do], sep="\n")


# import numpy as np
# t = Tokenizer() ## UNRESOLVED ERROR --> NameError: name 'Tokenizer' is not defined
# s = open("text0.txt")

# output_data=[]
# x = np.empty((0,4), float)
# for token in t.tokenize(s):
#   if token.part_of_speech.split(',')[0]=="名詞" or token.part_of_speech.split(',')[0]=="形容詞":
#     print(token.surface)
#     similarity1 = model.wv.similarity(w1=token.surface, w2="嬉しい")
#     #print("喜び：{0}".format(similarity1))
#     similarity2 = model.wv.similarity(w1=token.surface, w2="楽しい")
#     #print("悲しみ：{0}".format(similarity2))
#     similarity3 = model.wv.similarity(w1=token.surface, w2="悲しい")
#     #print("不安：{0}".format(similarity3))
#     similarity4 = model.wv.similarity(w1=token.surface, w2="興奮")
#     #print("興味：{0}".format(similarity4))
#     x = np.append(x, np.array([[similarity1, similarity2, similarity3, similarity4]]), axis=0)

# print("-"*30)
# print(np.mean(x, axis=0))
# print("嬉：{0}".format(np.mean(x, axis=0)[0]))
# print("楽：{0}".format(np.mean(x, axis=0)[1]))
# print("悲：{0}".format(np.mean(x, axis=0)[2]))
# print("興：{0}".format(np.mean(x, axis=0)[3]))