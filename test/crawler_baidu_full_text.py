#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import Terry_toolkit as tkit


"""
直接获取全文本搜索结果


"""
baidu = tkit.CrawlerBaidu()
li = baidu.get('柯基犬')
print(li)


cx = tkit.CxExtractor()
for item in li:

    print(item['title'])
    print(item['url'])

    # test_html = cx.readHtml("E:\\Documents\\123.html")
    # test_html = cx.getHtml(item['url'])
    test_html = baidu.open_url(item['url'])
    content = cx.filter_tags(test_html)
    s = cx.getText(content)
    print(s)
