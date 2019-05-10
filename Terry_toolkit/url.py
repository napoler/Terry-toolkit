import requests
import urllib.request

class Url:
    """Url相关的操作库



    """

    def open_url(self, url):
        """
        安全有效的打开url

        >>> open_url(url)
        
        # req = request.build_opener(url)
        # req.add_header(
        #     'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0')
        # response = urllib.request.urlopen(req)
        # r = requests.get(url)
        # r.status_code
        # r.encoding = 'utf-8'
        # r.text
        # html = response.read().decode('utf8')  # gbk格式的
        # opener = urllib.request.build_opener()
        # opener.addheaders = [('User-agent',  # 添加模拟浏览器访问的header信息
        #                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
        # html = opener.open(url).read().decode()
        # html = requests.get(url, timeout=10).content.decode('utf-8')


        """
        req = urllib.request.Request(url)
        req.add_header(
            'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0')
        response = urllib.request.urlopen(req)
        try:
            html = response.read().decode('utf-8')
        except:
            html = response.read().decode('gb2312')

        return html
    def open_url_v1(self, url):
        # r = requests.get(url)
        r = requests.get(url, allow_redirects=True)
        print(r.url)
        print('r.status_code',r.status_code)
        print(' r.history', r.history)
        return r.text
        pass
    