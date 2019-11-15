# -*- coding: utf-8 -*-
# __init__.py
#from .a import A
#from .b import B
"""
# Terry_toolkit
===

各种工具合集
文档地址
http://terry-toolkit.terrychan.org/zh/master/

# 安装
> pip3 install Terry_toolkit

"""
#多文件导入以后只用导入 import Terry-toolkit 就可以使用所有类
#>>> import mymodule
#>>> a = mymodule.A()
#>>> a.spam()


from .file import *
from .text import *
# from .text import Text
from .dict_get import *
from .crawler_baidu import *
from .CxExtractor import *
from .turl import *
from .SearchBaidu import *
# from .TextRank4ZH import TextRank4ZH
from .list import *
from .tjson import *
from.csv import *
from.db import *

# https://www.helplib.com/GitHub/article_112235
# https://unqlite-python.readthedocs.io/en/latest/quickstart.html#key-value-features
from unqlite import *
"""
#cacheout缓存模块
# from cacheout import Cache# 如果选择LFUCache 就导入即可
# https://pypi.org/project/cacheout/
"""
from cacheout import *
# cache = LFUCache()
from .sentence_parser import *
from .triple_extraction import *
