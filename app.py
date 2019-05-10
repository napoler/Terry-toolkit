from cacheout import Cache
cache = Cache()

from flask import Flask, render_template, request, json, Response, jsonify
import Terry_toolkit as tkit
# t= tkit.Text()
app = Flask(__name__)

@app.route("/")
def home():
    items=[
    {'path':'/json/search_baidu','data':{
        'keyword':'关键词','start':0
    }}
    ]
    # return items
    return render_template("index.html",**locals())

@app.route("/json/search_baidu")

def json_search_baidu():
    """json_search_baidu
    获取百度搜索结果

    """
    keyword = request.args.get('keyword')
    start = request.args.get('start')

    key = keyword+str(start)
    if cache.get(key) is None:
        print('创建新缓存')
        baidu=tkit.SearchBaidu()
        items= baidu.get(keyword=keyword,start=0)
        cache.set(key ,items)
    else:
        print('获取缓存')
        items = cache.get(key)

    return jsonify(items)


@app.route("/json/url_content")
def json_url_content():
    """json_url_content
    获取网页内容

    """
    url = request.args.get('url')
    start = request.args.get('start')

    key = url+str(start)
    if cache.get(key) is None:
        print('创建新缓存')
        cx=tkit.CxExtractor()
        
        items= cx.url_text(url=url)
        items= tkit.Text().text_processing(items)
        
        cache.set(key ,items)
    else:
        print('获取缓存')
        items = cache.get(key)
    print(items)
    return jsonify(items)



if __name__ == "__main__":
    # app.run()
    app.run(
        host='0.0.0.0',
        port=5000)
# 跑host

# python3 -m flask run --host=0.0.0.0