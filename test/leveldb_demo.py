
#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import Terry_toolkit as tkit
"""
LDB()
数据库测试

"""
#加载函数
tdb=tkit.LDB()
key="32323"
value= {"eee":111}


#添加一条 支持字符串和词典
tdb.put(key,value)
#获取一条
data=tdb.get(key)


data=tdb.str_dict(data)
print(data)

#删除
data=tdb.delete(key)
print(data)


# 存储多条
data=[('key','dddd')]
tdb.put_data(data)


print(tdb.get('key'))

#切换表前缀
tdb.load("dsd2132")
tdb.get_all()
