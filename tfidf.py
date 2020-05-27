#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:26:05 2020

@author: emirimorita
"""
########Wakati-gaki#######
import MeCab

def _split_to_words(text, to_stem=False):
    """
    入力: 'すべて自分のほうへ'
    出力: tuple(['すべて', '自分', 'の', 'ほう', 'へ'])
    """
    tagger = MeCab.Tagger('mecabrc') 
    mecab_result = tagger.parse(text)
    info_of_words = mecab_result.split('\n')
    words = []
    for info in info_of_words:
        # macabで分けると、文の最後に’’が、その手前に'EOS'が来る
        if info == 'EOS' or info == '':
            break
            # info => 'な\t助詞,終助詞,*,*,*,*,な,ナ,ナ'
        info_elems = info.split(',')
        # 6番目に、無活用系の単語が入る。もし6番目が'*'だったら0番目を入れる
        if info_elems[6] == '*':
            # info_elems[0] => 'ヴァンロッサム\t名詞'
            words.append(info_elems[0][:-3])
            continue
        if to_stem:
            # 語幹に変換
            words.append(info_elems[6])
            continue
        # 語をそのまま
        words.append(info_elems[0][:-3])
    return words

def stems(text):
    stems = _split_to_words(text=text, to_stem=True)
    return stems

###########vectorizer############
import os
from sklearn.feature_extraction.text import TfidfVectorizer


def is_bigger_than_min_tfidf(term, terms, tfidfs):
    '''
    [term for term in terms if is_bigger_than_min_tfidf(term, terms, tfidfs)]で使う
    list化した、語たちのtfidfの値のなかから、順番に当てる関数。
    tfidfの値がMIN_TFIDFよりも大きければTrueを返す
    '''
    if tfidfs[terms.index(term)] > 0.01:
        return True
    return False

############calculations############
    
vectorizer = TfidfVectorizer(analyzer=stems, min_df=1, max_df=50)
corpus = text_list[7:]
x = vectorizer.fit_transform(corpus)

# tfidfの高い語
terms = vectorizer.get_feature_names()
tfidfs = x.toarray()[i]
frequent = [term for term in terms if is_bigger_than_min_tfidf(term, terms, tfidfs)]

# export list of frequent words to csv
import numpy as np
np.savetxt("frequent_words.csv", frequent, delimiter=",", fmt='%s')



    
