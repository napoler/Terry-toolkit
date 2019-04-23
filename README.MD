#jieba path
结巴分词目录快速处理

## 安装
```
pip install -U jieba_path
```


## 使用
批量处理文件


```

from jieba_path import jieba_path
jpath = jieba_path.Jpath()
#处理目录下的txt所有文件
jpath.jieba_path('./data/', 'txt')
#单个文件处理
jpath.jieba_file('./data/001.txt')

#处理完的文件在原目录只是在文件结尾添加.jiaba可以方便使用下面的函数获取文件

#获取目录下的txt文件列表
jpath.file_List('./data/', 'txt')
#获取目录下的jieba文件列表
jpath.file_List('./data/', 'jiaba')

#将所有处理好文档合并成一个文档
jpath.file_to_one('./data/', type='jieba', endType='end')

#分句
jpath.cut_p( file)
cut_p.end
```
open_file()



pip install -r requirements.txt

