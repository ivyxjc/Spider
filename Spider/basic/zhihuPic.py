import urllib.request
import os
import random
import time



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


#获取图片地址，返回图片地址的list
def get_imgs(url):
    html=url_open(url).decode('utf-8')

    img_address=[]
    a=html.find('data-original')
    while(a!=-1):
        b=html.find('.jpg',a,a+300)
        if(b!=-1):
            # print(html[a+15:b+4])
            img_address.append(html[a+15:b+4])
        else:
            b=a+9
        a=html.find('data-original=',b)


    for i in img_address:
        print(i)

    return img_address


#存储到本地
def save_imgs(img_address):

    for i in img_address:
        # print(i)
        filename=i.split('/')[-1]
        with open(filename,'wb') as f:

            img=url_open(i)
            f.write(img)


def zhihuPic(url,folder="zhihu"):
    if(os.path.exists(folder)):
        os.chdir(folder)
    else:
        os.mkdir(folder)
        os.chdir(folder)
    img_address=get_imgs(url)
    save_imgs(img_address)





if __name__=='__main__':
    zhihuPic("https://www.zhihu.com/question/22070147","E:\program\spiderPic")
