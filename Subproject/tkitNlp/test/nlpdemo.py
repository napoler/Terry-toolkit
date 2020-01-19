# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from __future__ import unicode_literals
import sys
sys.path.append("../")

import tkitNlp 
from harvesttext import HarvestText


# nlp=tkitNlp

from harvesttext import loadHT,saveHT
ht = HarvestText()
# new_words = ["漫威漫画","666"]
# ht.add_new_words(new_words)   # 作为广义上的"新词"登录
saveHT(ht,"/tmp/ht_model1")
ht0 = loadHT("/tmp/ht_model1")



para = """威尔士柯基犬为1107年由法兰德斯工人携带过来的犬种，根据其近似狐狸的头部，有人认为本犬与尖嘴犬祖先关系密切。
"""




# para = "上港的武磊武球王是中国最好的前锋。"
# entity_mention_dict = {'武磊': ['武磊', '武球王'], "上海上港":["上港"]}
# entity_type_dict = {'武磊': '球员', "上海上港":"球队"}
# ht0.add_entities(entity_mention_dict, entity_type_dict)

ht0.add_new_entity("漫威漫画", mention0="漫威漫画", type0="nrf")  # 作为特定类型登录
ht0.add_new_entity("法兰德斯", mention0="法兰德斯", type0="nrf")  # 作为特定类型登录
ht0.add_new_entity("为", mention0="为", type0="v")  # 作为特定类型登录
ht0.add_new_entity("认为", mention0="认为", type0="v")  # 作为特定类型登录
for arc in ht0.dependency_parse(para):
    print(arc)

print(ht.triple_extraction(para))
print(ht0.triple_extraction(para))


print(ht0.triple_extraction(sent=para,expand = "exclude_entity"))

#[['\n\n梅乡站', '是', '一个位于千叶县野田市'], ['一个', '位于', '千叶县野田市'], ['铁路车站', '属于', '东武铁道野田线'], ['车站编号', '是', 'TD 18。\n\n\n']]
# [['处决者', '漫', '画角色'], ['本名', '是', '一名超级反派']]


