#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import Terry_toolkit as tkit
url=tkit.Url()
myurl = 'https://baike.baidu.com/item/%E5%A8%81%E5%B0%94%E5%A3%AB%E6%9F%AF%E5%9F%BA%E7%8A%AC/84385?fromtitle=%E6%9F%AF%E5%9F%BA%E7%8A%AC&fromid=1198817&fr=aladdin'
# text = url.open_url_v1(url= myurl)
# print('网页文本为',text)



 
text = url.open_url(url= myurl)
print('网页文本为',text)