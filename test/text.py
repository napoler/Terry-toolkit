#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import Terry_toolkit as tkit
t= tkit.Text()

text="""


法院经审理查明，被告人陈淑惠在担任银川市兴庆区委副书记、区长，灵武市委副书记、代市长、市长期间，利用职务上的便利，在工程款拨付、项目审批等方面为他人谋取利益，先后非法收受他人财物折合人民币546万余元、英镑2万元、美元3万元。

法院认为，被告人陈淑惠身为国家工作人员，利用职务之便，为他人谋取利益，非法收受他人财物数额特别巨大，其行为已构成受贿罪。陈淑惠到案后，如实交代了监察机关尚未掌握的其他绝大部分受贿犯罪事实。在案发前，陈淑惠主动向部分行贿人退赃158万元，案发后积极退缴剩余全部赃款。在检察机关审查起诉及法院审理期间，陈淑惠认罪认罚，确有悔罪表现，应当从轻处罚。综上，法院以被告人陈淑惠犯受贿罪判处其有期徒刑10年，并处罚金人民币60万元，受贿违法所得财物依法予以没收，上缴国库。

据公开简历，陈淑惠出生于1963年5月，2009年11月至2012年5月，曾任灵武市市长。

2018年10月，陈淑惠被查。

“政事儿”注意到，陈淑惠曾经的搭档市委书记李建军于今年5月被宣布调查。

李建军也是陈淑惠的前任灵武市长。

2009年1月至2009年11月，李建军任职了10个月的灵武市长就升任市委书记，接任灵武市长的正是陈淑惠，此后两人党政班子搭档了两年时间。




"""

# li = t.summary(text=text)
# print(li)

# li = t.get_keyphrases(text=text)
# print(li)

# li = t.sentence_segmentation(text=text)
# print(li)


li = t.participle(text='李建军任职了10个月的灵武市长就升任市委书记，接任灵武市长的正是陈淑惠',dotype='words_all_filters')
print(li)