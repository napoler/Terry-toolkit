#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import Terry_toolkit as tkit
url=tkit.Url()
myurl = 'https://blog.csdn.net/hxldxx99/article/details/48932393'
# text = url.open_url_v1(url= myurl)
# print('网页文本为',text)

import requests

 
# text = url.open_url(url= myurl)
# print('网页文本为',text)

 
# html=requests.get(myurl)
# print (html.encoding)
# print (html.text.encode(html.encoding))


headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
resp = requests.get(myurl,headers=headers) #请求


# resp=requests.get(myurl)
print (resp.encoding)
resp.encoding = resp.apparent_encoding
print (resp.encoding)
txt = resp.text #获取响应的html内容
    
print (txt)