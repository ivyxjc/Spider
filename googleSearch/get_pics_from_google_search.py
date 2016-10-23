import requests
import re

"""
爬bing图片搜索中的结果，
正则  imgurl=图片源网址
"""
url='https://cn.bing.com/images/search?pq=%u8d5b%u8f66%u58c1%u7eb8&sc=8-4&sp=-1&sk=&q=%e8%b5%9b%e8%bd%a6%e5%a3%81%e7%ba%b8&qft=+filterui:imagesize-custom_1600_900&FORM=R5IR4'

headers = {
    'Host':'cn.bing.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate, br',
    'DNT':'1',
    'Connection': 'keep-alive',
}

params={'pq':'赛车壁纸',
        'sc':'8-4',
        'sp':'-1',
        'sk':'',
        'q':'赛车壁纸',
        'qft':'+filterui:imagesize-custom_1600_900',
        'FORM':'R5IR4'}

res=requests.get(url,headers=headers,params=params)
print(res.status_code)
print(res.text)
p=re.compile('imgurl:&quot;(http://.+?)&quot')
search_res=re.findall(p,res.text)
for i in search_res:
    print(i)


