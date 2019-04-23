# -*- coding: utf-8 -*-
# 对文件进行预处理



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

        包括 (。|！|\!|\.|？|\?|\：|\:|\?)

        >>> sentence_segmentation("这里似乎内.容不给")


        """
        sentences = re.split('(。|！|\!|\.|？|\?|\：|\:|\?)',string)
        return sentences

    # 清理多余的换行空格等
    def clear(self, string):
        """清理多余空格

        清理多余的换行空格等

        >>> clear('这里似乎内\t容不给')

        """

        # return string.strip()
        # for line in string.readlines():
        # string = re.sub('[\n]+', '\n', string)
        string = string.replace('\n', '').replace(
            '\n\n', '\n').replace('\r\n', '\n').replace('   ', '\n')
        # string = string.replace('\n\n', ' ').replace('\n', '')
        string = re.sub(' +', ' ', string)
        return string