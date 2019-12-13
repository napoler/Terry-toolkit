#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
from harvesttext import HarvestText

import Terry_toolkit as tkit
t= tkit.Text()

text="""
奥巴马也喜欢流浪猫。
小猫很不错的。
宠物猫生活很滋润。


"""
# li = t.summary(text=text)
# print(li)

# li = t.get_keyphrases(text=text)
# print(li)

# li = t.sentence_segmentation(text=text)
# print(li)


# # li = t.participle(text=text,dotype='words_all_filters')
# # print(li)
# text = t.clear(text) #提取单个句子 分句
# print(text)
# ie=tkit.TripleIE(model_path='/mnt/data/dev/model/ltp/ltp_data_v3.4.0')

# # print("*"*20)
# s=ie.get(text)
# # print(s)
# # 
# for item in s:
#     if item==None:
#         pass 
#     else:
#       if len(item)>3:
#         print([item[0],item[1],item[2],"["+item[3]+"]"])
#       else:
#         print(item[0],item[1],item[2])

# # s=ie.get_test(text)
# # print(s)









text="""

在巴黎、纽约和芝加哥等地，随着非洲移民的到来，也带动了野生动物肉品市场的空前活跃。
 
"""

print(text)

print("*"*20)
# extractor = tkit.TripleExtractor()
# svos = extractor.triples_main(text)
# # print(svos)
# for item in svos:
  
#     # print(" ".join(item))
#     print('三元组',item)
# # # print("*"*20)










from harvesttext.resources import get_qh_sent_dict,get_baidu_stopwords,get_qh_typed_words
text=t.clear(text)
print(text)
t.load_ht('ht_model')
# # t.add_words(["暹罗猫"])
print("*"*20)
typed_words = {"属性":["是个",'就是']}
# entity_mention_dict = {'猫咪':['小猫','喵星人','宠物猫'],'郜林':['郜林','郜飞机'],'前锋':['前锋'],'上海上港':['上港'],'广州恒大':['恒大'],'单刀球':['单刀']}
# entity_type_dict = {'猫咪':'人名','郜林':'球员','前锋':'位置','上海上港':'球队','广州恒大':'球队','单刀球':'术语'}
# t.ht.add_entities(entity_mention_dict,entity_type_dict)


typed_words, stopwords = get_qh_typed_words(), get_baidu_stopwords()


terry_words=tkit.Resource().terry_words()
t.ht.add_typed_words(terry_words)
t.ht.add_typed_words(typed_words)
for span, entity in t.ht.entity_linking(text):
	print(span, entity)
for item in t.ht.triple_extraction(sent=text, standard_name=False, stopwords=None, expand = "all"):
  print("三元组",item)
print("*"*20)
print("实体",t.ht.named_entity_recognition(text))
print("*"*20)
for arc in t.ht.dependency_parse(text):
    print(arc)
print(t.ht.posseg(text))


print(t.named_entity_recognition(text))








# print(t.ht.seg(text,return_sent=False))    # return_sent=False时，则返回词语列表
# # # print(t.ht.named_entity_recognition(text))


# # ht=t.ht

# # ht.add_new_entity("颜骏凌", "颜骏凌", "球员")
# # docs = ["武磊和颜骏凌是队友",
# # 		"武磊和郜林都是国内顶尖前锋"]
# # G = ht.build_entity_graph(docs)
# # print(dict(G.edges.items()))
# # G = ht.build_entity_graph(docs, used_types=["球员"])
# # print(dict(G.edges.items()))