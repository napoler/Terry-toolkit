
#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import Terry_toolkit as tkit



cx=tkit.CxExtractor()
url="http://www.sohu.com/a/227667958_604442"
items= cx.url_text(url=url)
items
