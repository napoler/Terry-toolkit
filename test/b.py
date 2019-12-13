#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
from harvesttext import HarvestText

import Terry_toolkit as tkit
t= tkit.Text()




text="""
威尔士柯基犬为1107年由法兰德斯工人携带过来的犬种，根据其近似狐狸的头部，有人认为它们与尖嘴犬祖先关系密切。13210323233
耳中等大小，直立，耳尖呈圆形，棕褐色眼睛中等大小，呈卵圆形。眼睛中等大小，不突出，眼圈为暗黑色，眼角清晰。嘴鼻部优美且紧凑，缺毛，为先天性特征。胸部宽度适中，向下逐渐变细，在前肢之间放松。后驱的肌肉发达且结实，但宽度略小于肩部。体躯比卡狄犬略小 [3]  。
被毛长度适中，绒毛层短而厚，外层被毛较长而粗糙，能抵御各种环境条件。全身毛长度不等，颈圈、胸部和肩部稍厚而长，躯干被毛平伏。前肢腹面、下腹部与后躯腹面毛比较长。被毛最好是直的。该犬容易褪毛。毛色有淡黄色短毛，金色短毛，红色短毛，黄褐色和白色短毛 [4]  。
"""

from harvesttext.resources import get_qh_sent_dict,get_baidu_stopwords,get_qh_typed_words
text=t.clear(text)
print(text)
t.load_ht('ht_model')
# # t.add_words(["暹罗猫"])
print("*"*20)
typed_words = {"n":["被毛",'猫咪']}
# entity_mention_dict = {'猫咪':['小猫','喵星人','宠物猫'],'郜林':['郜林','郜飞机'],'前锋':['前锋'],'上海上港':['上港'],'广州恒大':['恒大'],'单刀球':['单刀']}
# entity_type_dict = {'猫咪':'人名','郜林':'球员','前锋':'位置','上海上港':'球队','广州恒大':'球队','单刀球':'术语'}
# t.ht.add_entities(entity_mention_dict,entity_type_dict)
t.ht.add_typed_words(typed_words)

typed_words, stopwords = get_qh_typed_words(), get_baidu_stopwords()


terry_words=tkit.Resource().terry_words()
t.ht.add_typed_words(terry_words)

# for span, entity in t.ht.entity_linking(text):
# 	print(span, entity)
for item in t.ht.triple_extraction(sent=text, standard_name=False, stopwords=None, expand = "all"):
  print("三元组",item)
print("*"*20)
print("实体",t.ht.named_entity_recognition(text))
print("*"*20)
# for arc in t.ht.dependency_parse(text):
#     print(arc)
print(t.ht.posseg(text))
# entity_type_dict={}
# entity_id=0
# word_list=[]
# for word,tag0 in t.ht.posseg(text):
#     t=1

#     if tag0.startswith("nr"):
#         entity_type_dict[word] = {"id":str(entity_id),'tag':"人名"}
#         entity_id+=1
#         word_list.append(str(entity_id))
#     elif tag0.startswith("ns"):
#         # entity_type_dict[word] = "地名"
#         entity_type_dict[word] = {"id":str(entity_id),'tag':"地名"}
#         entity_id+=1
#         word_list.append(str(entity_id))
#     elif tag0.startswith("nt"):
#         # entity_type_dict[word] = "机构名"
#         entity_type_dict[word] = {"id":str(entity_id),'tag':"机构名"}
#         entity_id+=1
#         word_list.append(str(entity_id))
#     elif tag0.startswith("nz"):
#         # entity_type_dict[word] = "其他专名"
#         entity_type_dict[word] = {"id":str(entity_id),'tag':"其他专名"}      
#         entity_id+=1 
#         word_list.append(str(entity_id)) 
#     elif tag0.startswith("动物"):
#         # entity_type_dict[word] = "动物"
#         entity_type_dict[word] = {"id":str(entity_id),'tag':"动物"} 
#         entity_id+=1 
#         word_list.append(str(entity_id)) 
#     # elif tag0.startswith("n"):
#     #     entity_type_dict[word] = "名词"
#     else:
#         # print(word)
#         t=0
#         word_list.append(word)
#     # if tag0.startswith("r"):
#     #     entity_type_dict[word] = "指代词"


#     # elif tag0.startswith("ns"):
#     #     entity_type_dict[word] = "地名"


# print(word_list)
# # n={}
# # for i,key in enumerate( entity_type_dict.keys()):
# #     print( i,key)
# #     entity_type_dict
# print(entity_type_dict)

# print("".join(word_list))













entity_type_dict={}
entity_id=0
word_list=[]
for word,tag0 in t.ht.posseg(text):
    t=1

    if tag0.startswith("nr"):
        entity_type_dict[word] = {"id":str(entity_id),'tag':"人名"}
        entity_id+=1
        word_list.append("{"+word+"}")
    elif tag0.startswith("ns"):
        # entity_type_dict[word] = "地名"
        entity_type_dict[word] = {"id":str(entity_id),'tag':"地名"}
        entity_id+=1
        word_list.append("{"+word+"}")
    elif tag0.startswith("nt"):
        # entity_type_dict[word] = "机构名"
        entity_type_dict[word] = {"id":str(entity_id),'tag':"机构名"}
        entity_id+=1
        word_list.append("{"+word+"}")
    elif tag0.startswith("nz"):
        # entity_type_dict[word] = "其他专名"
        entity_type_dict[word] = {"id":str(entity_id),'tag':"其他专名"}      
        entity_id+=1 
        word_list.append("{"+word+"}")
    elif tag0.startswith("动物"):
        # entity_type_dict[word] = "动物"
        entity_type_dict[word] = {"id":str(entity_id),'tag':"动物"} 
        entity_id+=1 
        word_list.append("{"+word+"}")
    # elif tag0.startswith("n"):
    #     entity_type_dict[word] = "名词"
    elif tag0.startswith("m"):
        # entity_type_dict[word] = "其他专名"
        entity_type_dict[word] = {"id":str(entity_id),'tag':"时间"}      
        entity_id+=1 
        word_list.append("{"+word+"}")
    else:
        # print(word)
        t=0
        word_list.append(word)
    # if tag0.startswith("r"):
    #     entity_type_dict[word] = "指代词"


    # elif tag0.startswith("ns"):
    #     entity_type_dict[word] = "地名"


# print(word_list)
# n={}
# for i,key in enumerate( entity_type_dict.keys()):
#     print( i,key)
#     entity_type_dict
print(entity_type_dict)

print("".join(word_list))
