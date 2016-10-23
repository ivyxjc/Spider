import urllib.request
import random
import socket
import os
import gzip

def url_open(url):
    iplist=[
        '49.77.22.1:8118',
        '58.134.102.3:12696',
        '120.26.213.55:9999',
        '120.198.231.23:8081',
        '120.198.231.23:81',
        '120.198.231.23:85',
        '120.198.231.23:83',
        '120.198.231.23:80',
        '120.198.231.23:8086',
        '120.198.231.24:83',
        '120.198.231.23:82',
        '120.198.231.24:86',
        '120.198.231.24:80',
        '120.198.231.24:8080',
        '120.198.231.23:8082',
        '120.198.231.23:86',
        '120.198.231.24:82',
        '120.198.231.24:8081',
        '120.198.231.24:8086',
        '120.198.231.23:8080',
        '120.198.231.21:85',
        '120.198.231.21:84',
        '120.198.231.24:84',
        '120.198.231.21:83',
        '120.198.231.21:80',
        '120.198.231.21:81',
        '120.198.231.21:8080',
        '120.198.231.24:8082',
        '120.198.231.21:82',
        '120.198.231.21:86',
        '120.198.231.21:8086',
        '120.198.231.21:8081',
        '120.198.231.21:8082',
        '120.198.231.23:84',
        '120.198.231.24',
        '117.135.251.131:82',
        '117.135.250.131:8080',
        '117.135.250.131:80',
        '117.135.250.133:81',
        '117.135.250.132:80',
        '117.135.251.134:80',
        '117.135.251.134:82']

    proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

    opener=urllib.request.build_opener(proxy_support)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')]


    urllib.request.install_opener(opener)

    req=urllib.request.Request(url)
    response=urllib.request.urlopen(req)
    html=response.read()


    return html


img_address=['http://imgsrc.baidu.com/forum/w%3D580/sign=7cb25293f003918fd7d13dc2613c264b/892397dda144ad34461782f4d7a20cf431ad851c.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=a64fd0bd9e25bc312b5d01906ede8de7/b56eddc451da81cbb26186be5566d01609243139.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=b46f3cb736adcbef01347e0e9cae2e0e/2bfa828ba61ea8d399d27177900a304e241f58d4.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=82bae0550e24ab18e016e13f05fbe69a/f124b899a9014c08beda2dd60d7b02087af4f4e4.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=e731a549374e251fe2f7e4f09786c9c2/e3edab64034f78f051339d807e310a55b3191c8c.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=c1a78b4a6c63f6241c5d390bb745eb32/a1389b504fc2d562b68dd09ee01190ef76c66c3f.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=056245ceae773912c4268569c8188675/ea1fbe096b63f62498013a708044ebf81a4ca361.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=bb1eae61750e0cf3a0f74ef33a47f23d/2101213fb80e7bec7fab0092282eb9389b506b4b.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=967075556a224f4a5799731b39f69044/5336acaf2edda3cc5852bb5306e93901213f920a.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=19829f5dafd3fd1f3609a232004e25ce/9a025aafa40f4bfb60e49227044f78f0f7361888.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=c3827e53be12c8fcb4f3f6c5cc0392b4/ee03738da977391202128912ff198618367ae289.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=3bdf288dd6c8a786be2a4a065708c9c7/60f0f736afc3793114950e5eecc4b74542a911c3.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=82a3e2f4082442a7ae0efdade142ad95/12d162d9f2d3572c0d2d44ab8d13632763d0c3fe.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=e9673c04aa4bd11304cdb73a6aaea488/b1ec8a13632762d0d6f17cc8a7ec08fa503dc6fe.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=4669ee5a97ef76c6d0d2fb23ad17fdf6/5f10b912c8fcc3ce6049f5489545d688d43f203b.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=801f4be4a30f4bfb8cd09e5c334f788f/898fa0ec08fa513d248a48a53a6d55fbb2fbd9ac.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=6738af558118367aad897fd51e728b68/14338744ebf81a4c86668eb5d02a6059252da672.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=1a330a51a68b87d65042ab1737082860/3d2dd42a2834349baa14d6e5ceea15ce36d3be44.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=066ba94909f41bd5da53e8fc61db81a0/93d4b31c8701a18bfca35c2d992f07082838fe0c.jpg',
'http://imgsrc.baidu.com/forum/w%3D580/sign=e9673c04aa4bd11304cdb73a6aaea488/b1ec8a13632762d0d6f17cc8a7ec08fa503dc6fe.jpg'
]

def save_imgs(img_address):
    for i in img_address:
        filename=i.split('/')[-1]
        with open(filename,'wb') as f:
            try:
                img=url_open(i)
                f.write(img)
            except urllib.error.URLError:
                print("error")
                continue
            except socket.timeout:
                print("timeout")
                continue

# socket.setdefaulttimeout(2)
# os.chdir("E:\program\spiderPic\\test")
# save_imgs(img_address)


print(os.path.exists("E:\program\spiderPic"+'\\'+'proxy.config'))
# while(True):
#     try:
#         html=url_open("http://www.bing.com/?mkt=zh-CN").decode('utf-8')
#     except urllib.error.URLError:
#         print("error")
#         continue
#     except socket.timeout:
#         print("timeout")
#         continue
#     except UnboundLocalError:
#         print("UnboundLocalError")
#         continue
#     print(html[0:1])
#     print('\n')


iplist=[
    '49.77.22.1:8118',
    '58.134.102.3:12696',
    '120.26.213.55:9999',
    '120.198.231.23:8081',
    '120.198.231.23:81',
    '120.198.231.23:85',
    '120.198.231.23:83',
    '120.198.231.23:80',
    '120.198.231.23:8086',
    '120.198.231.24:83',
    '120.198.231.23:82',
    '120.198.231.24:86',
    '120.198.231.24:80',
    '120.198.231.24:8080',
    '120.198.231.23:8082',
    '120.198.231.23:86',
    '120.198.231.24:82',
    '120.198.231.24:8081',
    '120.198.231.24:8086',
    '120.198.231.23:8080',
    '120.198.231.21:85',
    '120.198.231.21:84',
    '120.198.231.24:84',
    '120.198.231.21:83',
    '120.198.231.21:80',
    '120.198.231.21:81',
    '120.198.231.21:8080',
    '120.198.231.24:8082',
    '120.198.231.21:82',
    '120.198.231.21:86',
    '120.198.231.21:8086',
    '120.198.231.21:8081',
    '120.198.231.21:8082',
    '120.198.231.23:84',
    '120.198.231.24',
    '117.135.251.131:82',
    '117.135.250.131:8080',
    '117.135.250.131:80',
    '117.135.250.133:81',
    '117.135.250.132:80',
    '117.135.251.134:80',
    '117.135.251.134:82']

url="http://www.kuaidaili.com/free/inha/903/"

proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')]

urllib.request.install_opener(opener)
html=None
try:
    req=urllib.request.Request(url)
    response=urllib.request.urlopen(req,None,5)
    html=response.read()
    # print(response.info())
    print(req.get_header("Content-Encoding"))
    for i in response.getheaders():
        if i[0]=="Content-Encoding":
            if(i[-1]=="gzip"):
                html=gzip.decompress(html)


except socket.timeout as e:
    print(e)
    print("socket.timeout:"+url)
except urllib.request.URLError as e:
    print(e)
    print("urllib.request.URLError:"+url)
except UnicodeEncodeError as e:
    print(e)
    print("UnicodeEncodeError:"+url)

# html=gzip.decompress(html)
# print(html.decode('utf-8'))