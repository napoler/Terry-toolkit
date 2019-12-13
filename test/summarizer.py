# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from __future__ import unicode_literals
import sys
sys.path.append("../")

import Terry_toolkit as tkit
# #-*- encoding:utf-8 -*-
# from __future__ import print_function
# #https://github.com/letiantian/TextRank4ZH
# import sys
# try:
#     reload(sys)
#     sys.setdefaultencoding('utf-8')
# except:
#     pass

# import codecs
# from textrank4zh import TextRank4Keyword, TextRank4Sentence

# # text = codecs.open('../test/doc/01.txt', 'r', 'utf-8').read()
text ="""

关键短语提取
参照关键词提取提取出若干关键词。若原文本中存在若干个关键词相邻的情况，那么这些关键词可以构成一个关键词组。

例如，在一篇介绍支持向量机的文章中，可以找到关键词支持、向量、机，通过关键词组提取，可以得到支持向量机。

摘要生成
将每个句子看成图中的一个节点，若两个句子之间有相似性，认为对应的两个节点之间有一个无向有权边，权值是相似度。

通过pagerank算法计算得到的重要性最高的若干句子可以当作摘要。

"""
# tr4w = TextRank4Keyword()

# tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

# print( '关键词：' )
# for item in tr4w.get_keywords(20, word_min_len=1):
#     print(item.word, item.weight)

# print()
# print( '关键短语：' )
# for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
#     print(phrase)

# tr4s = TextRank4Sentence()
# tr4s.analyze(text=text, lower=True, source = 'all_filters')

# print()
# print( '摘要：' )
# for item in tr4s.get_key_sentences(num=10):
#     print(item.index, item.weight, item.sentence)  # index是语句在文本中位置，weight是权重







ttext=tkit.Text()
extractor = tkit.TripleExtractor()




from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "chinese"
SENTENCES_COUNT = 5


if __name__ == "__main__":
    # url = "https://en.wikipedia.org/wiki/Automatic_summarization"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    # print(parser.document)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
    # for sentence in summarizer(text, SENTENCES_COUNT):
        print(sentence)
        svos = extractor.triples_main(str(sentence))
        print(svos)