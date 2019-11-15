#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import Terry_toolkit as tkit
# t= tkit.Db()

tdb=tkit.Db()
# tdb.add(key="niubi",value={'gender': "male", 'age': 28, 'name': 'john'})
# tdb.add(key="niub2",value="wqwq")
# j=tdb.get(key="niub2")
# print(type(j))
# print(j)


tdb.col('ss')
print(dir(tdb.col.all()))

print(tdb.col.all())
