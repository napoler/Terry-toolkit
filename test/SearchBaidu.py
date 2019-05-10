#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import Terry_toolkit as tkit
baidu=tkit.SearchBaidu()
li= baidu.get('柯基犬')
print(li)
