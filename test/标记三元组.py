#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import Terry_toolkit as tkit
t= tkit.Text()

from multiprocessing import Process
import time
import random
import multiprocessing as mp
import math


content2="""

10月13日下午16时，北京市空气重污染应急指挥部办公室发布空气重污染蓝色预警。北京市及华北地区受不利气象条件影响，污染物积累明显，空气质量达到重度污染水平。京津如笼黑纱！（以下图片为新浪及网络） 图为北京城市上空如同笼罩着一层黑纱。秋冬季节北风、西北风偏多，不知道此次雾霾会不会飘到青岛来，但是，有备无患，倘若青岛雾霾，孩子老人该怎么办？各位妈妈们先要做到心里有数！ 青岛雾霾，孩子老人该怎么办？搜索 01准备好口罩。关于口罩的选择一定要选择过滤效果好的，不能只看花色只看样式，医用口罩是比较好的选择。02多喝水。水对身体基本上是没啥坏处的，尤其是白开水，一定要让孩子多喝水，起床之后先喝杯水，放学回到家也要多喝水！03减少户外运动。孩子是闲不住的，但是这种天气下也尽量少带孩子出去，在户外会吸收太多的雾霾空气，对身体反而是一种伤害，老人也不要出去了，尤其是心脏病还有肺病患者不！04食补。可以多吃一些清肺的食物，因为雾霾是通过呼吸道进入肺部的，木耳，梨都是不错的选择，另外多吃点增强抵抗力的食物，虾皮，菠菜，海鲜等。05去空气好的地方旅游。（这个方法可以忽略不计！）这个方法一般很少有人会采用，不过也可以作为一种方法哦，世界这么大总有空气好的地方，带着孩子老人来躺旅游，避开雾霾天气，呼吸新鲜空气。另外这种天气行车也要注意1、大雾天气，空气能见度低，行车要慢一点，以免发生意外！2、车辆行驶在雾霾天气里，一定要关好车窗和天窗，不要用开车窗的方式来通风，不然高浓度的悬浮污染物，或可吸入颗粒物，很容易涌入车内，这就跟人直接在雾霾里呼吸是一样的了。3、关闭车窗时，就要会用空调来调节净化车内空气，比如将空调设成内循环，为防止冬天一味使用热空调，造成挡风玻璃和车窗玻璃的内侧起雾，可以将冷暖空调同时开，起动A/C装置，将温度设定在24-25度，这样就能够达到一个较好的效果。



"""



def split_sents(content):
    limit=3
    t= tkit.Text()
    sents=t.sentence_segmentation_v1(content)
    for i in range(math.ceil(len(sents)/limit)):

        one=sents[i*limit:(i+1)*limit]
        yield "。".join(one)

# def auto_triples(content):
#     # tdict=[]
#     try:
#         mp.set_start_method('spawn')
#     except:
#         pass
#     for one in split_sents(content):
#         print(one)
#         # print("###"*20)

#         q = mp.Queue()
#         p = Process(target=get_triples,args=(content,q))
#         p.start()   #让这个进程开始执行test函数里面的代码
#         # tdict.append(q.get())
#         print("xiu13")
#         time.sleep(100)
#         yield q.get()
#         p.join()

#     # return tdict

def auto_triples(content):

    for one in split_sents(content):
        d=get_triples(content)

        print("xiu13")
        time.sleep(100)
        yield d


    # return tdict


def get_triples(content):
    # print(content)
    limit=3
    extractor = tkit.TripleExtractor()
    tdict={}
    svos = extractor.triples_main(content)
    for sentence,items,ner in svos:
        # print(",".join(item))
        for item in items:
         
            if len(item)==4 and item[3]=="主谓宾":
                # print(item)
            # if len(item)==4:
                if tdict.get(item[0])==None:
                    tdict[item[0]]={item[1]:[(item[2],sentence)]}
                elif tdict[item[0]].get(item[2])==None:
                    tdict[item[0]][item[1]]=[(item[2],sentence)]
                else:
                    tdict[item[0]][item[1]].append((item[2],isentence))
    # print(tdict)
    # print(" print(tdict)",tdict)
    # print(tdict.keys())
    del extractor
    # q.put(tdict)
    return tdict
            

def run():
    # while True:
    db=tkit.LDB()
    tt= tkit.Text()
    tfile=tkit.File()
    tjson=tkit.Json(file_path="data.json")
    for item in tfile.file_List("/home/terry/pan/github/bert/data/text/news2016zh/"):
        print(item)
        db.load("files")
        
        try:
            db.get(item)
            print("跳过")
            continue
        except:
            pass
        # print(tfile.open_file(item))
        # item="/home/terry/pan/github/bert/data/text/news2016zh/1559850465.8304443/1559850473.5257394/article_f3b5cd293dbec4c4778f3037e99dad38.txt"
        content = tfile.open_file(item)
        # tdict=get_triples(content)
        print(len(content))
        # continue
        # try:
        #     mp.set_start_method('spawn')
        # except:
        #     pass
        # q = mp.Queue()
        # p = Process(target=auto_triples,args=(content,q))
        # p.start()   #让这个进程开始执行test函数里面的代码
        # tdicts=q.get()
        # p.join()     #等进程p结束之后，才会继续向下走
        # # break
        # auto_triples(content)
        # break

        for tdict in auto_triples(content):
            for a in tdict.keys():
                # print(t)
                for b in tdict[a].keys():
                    for c,original in tdict[a][b]:
                        print("#"*30)
                        print(original)
                        print("-"*30)
                        print([a,b,c])
                        print("-"*30)
                        print("选择((1:不是,2:是))")
                        value = input('输入选择:')
                        try:
                            value=int(value)-1
                        except:
                            print("不是(默认)")
                            value==0                    

                        if value==0:
                            print("不是")
        
                        elif  value ==1:
                            print("是")

                        else:
                            print("不是(默认)")
                            value==0
                        print([a,b,c])
                        text=original
                        one={'label':value,'sentence':text,"triple":[a,b,c]}
                        db.load("maker_kg")
                        db.put(tt.md5(text),one)
        db.load("files")
        db.put(item,item)
                    # tjson.save([one])




    # def replace_one(text):
    #     xdict={0:"赵",1:"孙",2:"李",
    #     3:"吴",
    #     4:"郑",
    #     5:"王",
    #     6:"陈",}
    #     text=text.replace("小王",xdict[0])
    #     return text



if __name__=="__main__":
    # print("main")
    run()
    # a=auto_triples(content2)
    # print(a)
    # print("xiu10")
    # time.sleep(100)
    # print("xiu11")
    # time.sleep(100)
    # print("xiu13")
    # time.sleep(100)
