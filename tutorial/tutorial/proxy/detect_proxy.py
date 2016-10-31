import requests
from tutorial.proxy.getProxy_local import getProxy_local


def detect_proxy():
    filename="proxy.json"
    proxies=getProxy_local(filename)

    for i in proxies:
        url=proxies[i]
        if(url==None):
            continue
        map = {"http": None}
        url="http://"+url
        print(url)
        map["http"]=url
        try:

            response=requests.get("http://www.baidu.com",proxies=map)
            print(response.status_code)
            if(response.status_code==200):
                pass
            else:
                pass
        except TimeoutError :
            pass

detect_proxy()