
#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
from harvesttext import HarvestText

import Terry_toolkit as tkit
t= tkit.Text()
t.load_ht('ht_model')
terry_words=tkit.Resource().terry_words()
t.ht.add_typed_words(terry_words)


para = """
流浪猫跑进家里，想把它送出去，朋友看了却说太傻

街角有只猫
发布时间：18-06-2919:16

现在，很多人都有宠物，对于他们的宠物来说，大多数人把它们当成自己的孩子来养，很宠爱，而且大多数人都有各种各样的宠物，而且更多的人不会放慢它们。由于它的出现，它现在已经成为一种受欢迎的宠物，深受人们的喜爱。

现在，大多数养宠物的人都是城市里的人。他们不需要他们做任何事情。他们害怕他们有点受伤，尤其是猫。他们经常把他们关在家里，害怕他们跑掉。毕竟，很难确定城市的方向。猫仍然对外面的世界感到好奇，很难一回来就回来。

一个网友的家里跑的是一只猫，它很可能是别人的猫跑出来的，找不到回家的路，应该像它的家一样，跑进去，还不走。

刚打开门，那只流浪猫溜进了门，试图把它送走。

在这一天，这位网友在家里完成了他的工作。在家加班已经两天了。要完成它并不容易。它准备出去吃一顿美餐，然后回家好好睡一觉。这两天都在外面吃饭。
"""
#返回关于新词质量的一系列信息，允许手工改进筛选(pd.DataFrame型)
new_words_info = t.ht.word_discover(para)
#new_words_info = ht.word_discover(para, threshold_seeds=["武磊"])  
print(new_words_info)
new_words = new_words_info.index.tolist()
print(new_words)

print(t.ht.seg(para,return_sent=False))    # return_sent=False时，则返回词语列表

t.named_entity_recognition(para)