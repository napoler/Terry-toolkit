# # _*_coding:utf-8_*_
# # Simple usage
# from stanfordcorenlp import StanfordCoreNLP
# # Other human languages support, e.g. Chinese
# sentence = '朱元璋说我喜欢吃肉'
# print('kaishi')
# # with StanfordCoreNLP(r'/mnt/data/dev/model/stanford-chinese-corenlp', lang='zh') as nlp:
# #     print(nlp.word_tokenize(sentence))
# #     print(nlp.pos_tag(sentence))
# #     print(nlp.ner(sentence))
# #     print(nlp.parse(sentence))
# #     print(nlp.dependency_parse(sentence))


# # nlp = StanfordCoreNLP(r'/mnt/data/dev/model/stanford-corenlp-full-2018-02-27', lang='zh')

# # print(nlp.word_tokenize(sentence))
# # nlp.close()
# nlp = StanfordCoreNLP('http://localhost', port=9000, lang='zh')
# print(nlp.word_tokenize(sentence))
# print(nlp.pos_tag(sentence))
# print(nlp.ner(sentence))
# print(nlp.parse(sentence))
# print(nlp.dependency_parse(sentence))

# # with StanfordCoreNLP(r'/mnt/data/dev/model/stanford-corenlp-full-2018-02-27', lang='zh') as nlp:
# #     print(nlp.word_tokenize(sentence))
# #     print(nlp.pos_tag(sentence))
# #     print(nlp.ner(sentence))
# #     print(nlp.parse(sentence))
# #     print(nlp.dependency_parse(sentence))


# coding=utf-8
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000

import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/mnt/data/dev/model/stanford-corenlp-full-2018-02-27', quiet=False, lang='zh')
props = {'annotators': 'coref', 'pipelineLanguage': 'zh'}

text ="""

流浪猫的生活艰难，尤其是在这样高楼林立的社会，流浪猫的生活更加不容易了。比如说在一些恶劣的天气时，它们就无处可躲，只能深深的受着，能不能挺过去还不一定呢。好在，也有一些好心人会尽自己所能帮助流浪猫，在流浪猫遇到困难的时候伸出援助之手。
"""

print(nlp.annotate(text, properties=props))
result = json.loads(nlp.annotate(text, properties=props))

num, mentions = result['corefs'].items()[0]
for mention in mentions:
    print(mention)