#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import Terry_toolkit as tkit
"""
获取搜索结果

并且提取结果网页的正文



"""

# baidu = tkit.CrawlerBaidu()
# li = baidu.get('柯基犬')
# print(li)

# li = baidu.get_full('柯基犬')
# print(li)



# li = baidu.get('柯基犬')
# print(li)


from MagicBaidu import MagicBaidu
import pprint

mb = MagicBaidu()

# Get {'title','url','text'}
# for i in mb.search(query='python'):
# 	try:
# 		pprint.pprint(i)
# 	except:
# 		pass
li=[]
for i in mb.search(query='python'):
    
    # print(mb.get_real_url(i['url']))
    i['url']=mb.get_real_url(i['url'])
    # print(i)
    li.append(i)
print(li)

    # print(mb.get_real_url(url))
# for url in mb.search_url(query='柯基犬'):
#     print(url)
#     print(mb.get_real_url(url))
