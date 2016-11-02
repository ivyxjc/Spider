import urllib.request
import random

url="http://www.ip.cn/"


iplist=[
    '117.135.251.131:82',
    '117.135.250.131:8080',
    '117.135.250.131:80',
    '117.135.250.133:81',
    '117.135.250.132:80',
    '117.135.251.134:80',
    '117.135.251.134:82'
]
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener=urllib.request.build_opener(proxy_support)
header={}
# header['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')]


urllib.request.install_opener(opener)


request=urllib.request.Request(url,None,header)

response=urllib.request.urlopen(request)

html=response.read().decode('utf-8')

print(html)
