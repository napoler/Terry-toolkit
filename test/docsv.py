
#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
# from harvesttext import HarvestText

import Terry_toolkit as tkit
t= tkit.Text()
# t.load_ht('ht_model')
# terry_words=tkit.Resource().terry_words()
# t.ht.add_typed_words(terry_words)
tjson=tkit.Json(file_path="kws.json")
n={}

with open('/mnt/data/dev/tdata/baike_triples.txt', 'r', encoding = 'utf-8') as f:
    for i,line in enumerate(f):
        # do_something(line)
        # print(line.split("\t")[1])
        # n.append(line.split("\t")[1])
        n[line.split("\t")[1]]=0
        # if i>0:
        #    print(len(n)/i)

        print(len(n))

        # print(type(line))

# with open('/mnt/data/dev/tdata/7Lore_triple.csv', 'r', encoding = 'utf-8') as f:
#     for line in f:
#         # do_something(line)
#         print(line.split(", "))

#         # print(type(line))