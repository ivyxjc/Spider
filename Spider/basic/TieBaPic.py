import urllib.request
import re
import random
import os
import socket


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
    html=None
    try:
        req=urllib.request.Request(url)
        response=urllib.request.urlopen(req,None,1)
        html=response.read()
    except socket.timeout:
        print("socket.timeout:"+url)
    except urllib.request.URLError:
        print("urllib.request.URLError:"+url)
    except UnicodeEncodeError:
        print("UnicodeEncodeError:"+url)
    return html


def get_imgs_urls(page_url):
    html=None;
    count=0;
    while(html==None and count<5):
        html=url_open(page_url)
        count+=1

    if(html!=None):
        html=html.decode('utf-8')
        p=re.compile(r'<img class="BDE_Image" src="(http://imgsrc\.baidu\.com/forum[^"]+.jpg)')
        # p=re.compile(r'http://imgsrc\.baidu\.com/forum[^"]+.jpg')
        img_address=p.findall(html)

        for i in img_address:
            print(i)
        return img_address
    return None

def save_imgs(img_address):
    for i in img_address:
        filename=i.split('/')[-1]
        count=0
        img=None
        while(img==None and count<3):
            img=url_open(i)
            count+=1
        if(img!=None):
            with open(filename,'wb') as f:
                f.write(img)
        else:
            print("img is None,it cannot be saved")


def get_page_url(url,pageStart,pageEnd):
    page_urls=[]
    for i in range(pageStart,pageEnd):
        page_urls.append(url+"?pn="+str(i))

    # for i in page_urls:
    #     print(i)
    return page_urls


def TieBaPic(url,pageStart,pageEnd,folder):

    if(os.path.exists(folder)):
        os.chdir(folder)
    else:
        os.mkdir(folder)
        os.chdir(folder)

    page_urls=get_page_url(url,pageStart,pageEnd)
    for i in page_urls:
        print("=====================")
        print(i)
        img_address=get_imgs_urls(i)
        save_imgs(img_address)












if __name__=='__main__':
    TieBaPic("http://tieba.baidu.com/p/4362233961",1,50,"E:\program\spiderPic\\tieba\\tiebaPic2")
    socket.setdefaulttimeout(2)

