#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import Terry_toolkit as tkit


# data=tkit.Json(file_path="/mnt/data/dev/tdata/知识提取/chinese/test.json").auto_load()

# for it in data:
#     print(it)

import json

# json.load()函数的使用，将读取json信息
file = open('/mnt/data/dev/tdata/知识提取/chinese/train.json','r',encoding='utf-8')
info = json.load(file)
# print(info)
relation={}
relation_full={}
n=0
for it in info:
    if it['relation']!="NA":
        
        print(it['head']['word'])
        print(it['relation'].split('/')[-1])
        relation[it['relation'].split('/')[-1]]=0
        relation_full[it['relation']]=0
        print(it['tail']['word'])
        # print(it)
        n=n+1
        print("*"*40)
print(relation)
print(relation_full)
print(n)
print(len(relation))