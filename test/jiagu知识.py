#encoding=utf-8
from __future__ import unicode_literals
import sys
import jiagu
sys.path.append("../")
import Terry_toolkit as tkit
t= tkit.Text()
data= tkit.Json("/mnt/data/dev/github/gpt2Write/gpt2Write/data/data.json").auto_load()
data_save= tkit.Json("/mnt/data/dev/github/标注数据/Bert-BiLSTM-CRF-pytorch/data/data.json")

for item in data:
    # print(item)
    seqs=[]
    seqs.append(item["title"])
    seqs=seqs+t.sentence_segmentation_v1(item["content"])
    for seq in seqs:
        try:
            knowledge = jiagu.knowledge(seq)
            # print(knowledge)
            if len(knowledge)>0:
                it={"text":seq,"knowledge":knowledge}
                data_save.save([it])
        except:
            pass
        


# text = '''
# 威尔士柯基犬为1107年由法兰德斯工人携带过来的犬种，根据其近似狐狸的头部，有人认为本犬与尖嘴犬祖先关系密切。但也有人认为是随着威尔士与瑞典贸易传至威尔士的瑞典短脚长身犬和土著犬交配，产生了柯基犬。威尔士柯基犬名字来自威而斯语“corrci”娇小之犬的意思。本犬有潘布鲁克犬与卡迪肯犬两种变种犬。
# 潘布鲁克犬比卡迪肯犬名气大，本犬虽然体型娇小，却一直深受高阶层人士喜爱。
# 从12世纪的查理一世到现在的女王伊丽莎白二世，威尔士柯基犬一直是英国王室的宠物 [2]  。
# '''				


# text = '姚明（Yao Ming），1980年9月12日出生于上海市徐汇区，祖籍江苏省苏州市吴江区震泽镇，前中国职业篮球运动员，司职中锋，现任中职联公司董事长兼总经理。'

# 

# knowledge = jiagu.knowledge(text)
# print(knowledge)

# ner = jiagu.ner(text) # 命名实体识别
# print(ner)
# w=[]
# words=[]
# for i,item in enumerate(ner):
#     if item.startswith("B-"):
#         words.append("".join(w))
#         w=[]
#         w.append(text[i])
#     elif item.startswith("I-"):
#         w.append(text[i])
# print(words)
