#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import Terry_toolkit as tkit
t= tkit.Text()

text="""
柯基犬是个十足的小狗子
"""

# li = t.summary(text=text)
# print(li)

# li = t.get_keyphrases(text=text)
# print(li)

# li = t.sentence_segmentation(text=text)
# print(li)


# li = t.participle(text=text,dotype='words_all_filters')
# print(li)

ie=tkit.TripleIE(model_path='/mnt/data/dev/model/ltp/ltp_data_v3.4.0')


s=ie.get(text)
# print(s)
# 
for item in s:
    if item==None:
        pass 
    else:
       print(item[0],item[1],item[2])


# extractor = tkit.TripleExtractor()
# svos = extractor.triples_main(text)
# # print(svos)

# for item in svos:
#     print("".join(item))