#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import Terry_toolkit as tkit
baidu = tkit.CrawlerBaidu()
# li = baidu.get('柯基犬')
# print(li)


li = baidu.get_full('柯基犬')
print(li)


