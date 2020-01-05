#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
# from harvesttext import HarvestText

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







import time
import gc
from sys import getsizeof

text="""

 点击「箭头所指处」可快速关注微信号：巢湖教育（chaohujiaoyu）建设一支能力强、素质高、作风正的少先队辅导员队伍是加强少先队工作的基础工程，是推动未成年人思想道德建设的重要力量。据悉，我市2014年聘任的少先队总辅导员及各地聘任的少先队大队辅导员，至今聘期已满。为进一步贯彻落实相关文件及会议精神，加强少先队辅导员队伍建设，推进我市少先队事业的深入发展，团市委、市教体局、市人力资源与社会保障局、市少工委决定对全市的少先队总（大队）辅导员进行重新聘任。 辅导员配备与管理1设市总辅导员1名，城区总辅导员1名，各乡镇配备1名总辅导员。按照《中共合肥市委关于进一步加强少年儿童和少先队工作的意见》（合发〔2014〕25号）规定，县（市）区少先队总辅导员按不低于同级团委或教育行政部门中层副职的标准配备，乡镇少先队总辅导员一般由中心小学大队辅导员兼任。小学设置少先队大队辅导员岗位，按学校中层管理人员选拔配备和管理使用，享受同等待遇；中学设置少先队大队辅导员岗位，按学校团委副书记管理使用，享受同等待遇，是党员并且符合学校团干年龄要求的应担任学校团委副书记。2少先队辅导员三年一聘，期满后重新办理聘任手续。经团市委会同教育部门考核并聘任的总（大队）辅导员，无特殊情况不得随意撤换，学校对总（大队）辅导员进行调整时，需征求上级团委和教育部门意见，做到随缺随补。3少先队辅导员考核每学年进行一次，由团市委、市少工委会同市教体局考核，考核结果计入个人档案，并报送给所在学校党组织，考核不合格的予以解聘。4属于行政编制的少先队总辅导员，根据工作年限、实际表现及岗位设置情况，按照同级团委中层副职、中层正职、领导班子副职对应的职级，逐级晋升非领导职务。5属于专业技术岗位的少先队总辅导员，其从事少先队总辅导员工作的内容、工作量和成果应纳入专业技术职务评聘。 辅导员聘任基本条件1中共党员或共青团员，忠诚党的少年儿童事业，真心热爱少年儿童和少先队工作，品行端正，作风正派，具有奉献精神，竭诚为少年儿童健康成长服务。2具有较高的职业素质，了解和掌握少年儿童教育规律，有一定的理论研究水平，具有丰富的少先队工作实践经验、较强的组织协调能力、语言文字表达能力和指导基层少先队工作的能力。3聘任少先队总辅导员的，一般具有少先队工作或少年儿童教育工作3年以上工作经验。


 
"""
from pympler import tracker
tr = tracker.SummaryTracker()

print(text)

print("*"*20)
extractor = tkit.TripleExtractor()
svos = extractor.triples_main(text)
# print(svos)
for item in svos:
  
    # print(" ".join(item))
    print('三元组',item)
# # print("*"*20)
tr.print_diff()

print(dir())
del __cached__
gc.collect()

for key in dir():
  print(key,getsizeof(key))


print('extractor',getsizeof(extractor))
print('svos',getsizeof(svos))
print("110")
time.sleep(30)
extractor.__del__()
print("111")
time.sleep(30)
del extractor
gc.collect()
print("112")
time.sleep(30)
print("113")
time.sleep(30)








# from harvesttext.resources import get_qh_sent_dict,get_baidu_stopwords,get_qh_typed_words
# text=t.clear(text)
# print(text)
# t.load_ht('ht_model')
# # # t.add_words(["暹罗猫"])
# print("*"*20)
# typed_words = {"属性":["是个",'就是']}
# # entity_mention_dict = {'猫咪':['小猫','喵星人','宠物猫'],'郜林':['郜林','郜飞机'],'前锋':['前锋'],'上海上港':['上港'],'广州恒大':['恒大'],'单刀球':['单刀']}
# # entity_type_dict = {'猫咪':'人名','郜林':'球员','前锋':'位置','上海上港':'球队','广州恒大':'球队','单刀球':'术语'}
# # t.ht.add_entities(entity_mention_dict,entity_type_dict)


# typed_words, stopwords = get_qh_typed_words(), get_baidu_stopwords()


# terry_words=tkit.Resource().terry_words()
# t.ht.add_typed_words(terry_words)
# t.ht.add_typed_words(typed_words)
# for span, entity in t.ht.entity_linking(text):
# 	print(span, entity)
# for item in t.ht.triple_extraction(sent=text, standard_name=False, stopwords=None, expand = "all"):
#   print("三元组",item)
# print("*"*20)
# print("实体",t.ht.named_entity_recognition(text))
# print("*"*20)
# for arc in t.ht.dependency_parse(text):
#     print(arc)
# print(t.ht.posseg(text))


# print(t.named_entity_recognition(text))








# # print(t.ht.seg(text,return_sent=False))    # return_sent=False时，则返回词语列表
# # # # print(t.ht.named_entity_recognition(text))


# # # ht=t.ht

# # # ht.add_new_entity("颜骏凌", "颜骏凌", "球员")
# # # docs = ["武磊和颜骏凌是队友",
# # # 		"武磊和郜林都是国内顶尖前锋"]
# # # G = ht.build_entity_graph(docs)
# # # print(dict(G.edges.items()))
# # # G = ht.build_entity_graph(docs, used_types=["球员"])
# # # print(dict(G.edges.items()))