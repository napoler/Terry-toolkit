# -*- coding: utf-8 -*-
# 对文件进行预处理
import re
from textrank4zh import TextRank4Keyword, TextRank4Sentence

class Text:
    """
    文本处理函数



    """
    def __init__(self):
        pass
    # 遍历目录文件夹
    def sentence_segmentation(self, string):
        """
        句子分割函数

        包括 (。|！|\!|\.|？|\?)

        >>> sentence_segmentation("这里似乎内.容不给")


        """
        #sentences = re.split('(。|！|\!|\.|？|\?|\：|\:|\?)',string)
        #分句函数

        sentences = re.split('(。|！|\!|\.|？|\?)',string)         # 保留分割符

        new_sents = []
        for i in range(int(len(sentences)/2)):
            sent = sentences[2*i] + sentences[2*i+1]
            new_sents.append(sent)

        return new_sents

    # 清理多余的换行空格等
    def clear(self, string):
        """清理多余空格

        清理多余的换行空格等

        >>> clear('这里似乎内\t容不给')
        >>> [{'index': 0, 'sentence': '法院经审理查明，被告人陈淑惠在担任银川市兴庆区委副书记、区长，灵武市委副书记、代市长、市长期间，利用职务上的便利，在工程款拨付、项目审批等方面为他人谋取利益，先后非法收受他人财物折合人民币546万余元、英镑2万元、美元3万元', 'weight': 0.12558810530050332}, {'index': 1, 'sentence': '法院认为，被告人陈淑惠身为国家工作人员，利用职务之便，为他人谋取利益，非法收受他人财物数额特别巨大，其行为已构成受贿罪', 'weight': 0.11183996893770527}, {'index': 10, 'sentence': '2009年1月至2009年11月，李建军任职了10个月的灵武市长就升任市委书记，接任灵武市长的正是陈淑惠，此后两人党政班子搭档了两年时间', 'weight': 0.10833734824662838}]

        """

        # return string.strip()
        # for line in string.readlines():
        # string = re.sub('[\n]+', '\n', string)
        string = string.replace('\n', '').replace(
            '\n\n', '\n').replace('\r\n', '\n').replace('   ', '\n')
        # string = string.replace('\n\n', ' ').replace('\n', '')
        string = re.sub(' +', ' ', string)
        return string
    def summary(self, text,num=10):
        """获取文本的摘要

        >>> summary( text,num=10)
        >>> [{'word': '淑惠', 'weight': 0.03249010309710726}, {'word': '法院', 'weight': 0.02192152416206948}, {'word': '灵武', 'weight': 0.021869542539628625}, {'word': '李建军', 'weight': 0.019213098969148662}, {'word': '人财物', 'weight': 0.01856601133033217}, {'word': '市长', 'weight': 0.017907055156049748}, {'word': '市委书记', 'weight': 0.017755388969961372}, {'word': '被告人', 'weight': 0.016851090405232656}, {'word': '受贿罪', 'weight': 0.016218911983344443}, {'word': '行贿人', 'weight': 0.015739567821084217}]

        
        """
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source = 'all_filters')
        print(tr4s.get_key_sentences(num=3))

        # return data
    def get_keywords(self, text,num=10):
        """获取文本的关键词

        >>> get_keywords( text,num=10)
        
        """
        tr4w = TextRank4Keyword()

        tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
        return tr4w.get_keywords(num, word_min_len=2)
        # return data
    def get_keyphrases(self, text,num=10):
        """获取文本的关键短语

        >>> get_keyphrases( text,num=10)
        >>> ['灵武市长', '陈淑惠', '被告人陈', '被告人陈淑惠']

        
        """
        tr4w = TextRank4Keyword()
        # print( '关键短语：' )
        tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

        return tr4w.get_keyphrases(keywords_num=num, min_occur_num= 2)

        # return data