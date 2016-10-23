import urllib.request
import random
import socket
import re
import os
import gzip
import sys

kuaidaili_com_url="http://www.kuaidaili.com/free/inha/"
kuaidaili_com_proxylist=[]

def url_open(url):
    # iplist=[
    #     '15.150.96.184:9000',
    #     '1.60.156.123:9000',
    #     '183.23.216.147:8090',
    #     '115.223.234.177:9000',
    #     '106.7.153.82:9000',
    #     '59.55.58.203:9000',
    #     '60.219.23.108:9000',
    #     '115.218.125.97:9000',
    #     '115.223.192.86:9000  ',
    #     '111.72.83.127:9000',
    #     '49.68.28.96:9000',
    #     '115.223.229.206:9000',
    #     '180.104.173.127:9000',
    #     '59.62.35.168:9000',
    #     '123.154.240.252:9000',]

    iplist=[
        '183.22.139.28:9000',
        '112.126.72.101:8080',
        '163.125.144.199:9999',
        '223.95.84.179:3128']




    proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

    opener=urllib.request.build_opener(proxy_support)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')]

    urllib.request.install_opener(opener)
    html=None
    try:
        req=urllib.request.Request(url)
        response=urllib.request.urlopen(req,None,2)
        html=response.read()
    except socket.timeout as e:
        print(e)
        print("socket.timeout:"+url)
    except urllib.request.URLError as e:
        print(e)
        print("urllib.request.URLError:"+url)
    except UnicodeEncodeError as e:
        print(e)
        print("UnicodeEncodeError:"+url)

    return html

#获取url对应的html源码（没有decode），可通用
#默认url_open()三次，如果三次内都打开失败，返回None
#返回html source
def get_one_page_html(page_url,try_times=3):
    html=None
    count=0
    while(html==None and count<try_times):
        html=url_open(page_url)
        count+=1
    if(html!=None):
        return html
    else:
        return None

#
def get_one_page_proxy(html):
    proxy_list=[]
    if(html==None):
        return None
    else:
        try:
            html=html.decode('utf-8')
            res=re.findall("<td>([\d|.]+)</td>",html)
            for i in range(0,len(res),2):
                proxy_list.append(res[i]+":"+res[i+1])
            return proxy_list
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
    return None

def save_proxy(proxy_list,file_name):
    f=open(file_name,'a')
    if(proxy_list!=None):
        for i in proxy_list:
            print(i)
            f.write(i+'\n')



#获取所有的页面的url
def get_pages_url(url,pageStart,pageEnd):
    page_urls=[]
    for i in range(pageStart,pageEnd+1):
        page_urls.append(url+str(i)+'/')
    return page_urls

def get_proxy(url,file_name):
    pages_url=get_pages_url(url,2,12)
    for i in pages_url:
        print(i)
        html=get_one_page_html(i)
        proxy_list=get_one_page_proxy(html)
        save_proxy(proxy_list,file_name)


if __name__=='__main__':
    get_proxy(kuaidaili_com_url,"E:\program\spiderPic\proxy.txt")
