import urllib.request
import urllib.parse
import json
import time
while(True):

    content=input("请输入需要翻译的内容(输入q退出程序):")
    if(content=='q'):
        break
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data={}
    data['type']='AUTO'
    data['i']=content
    data['doctype']='json'
    data['xmlVersion']=1.8
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['action']='FY_BY_CLICKBUTTON'
    data['typoResult']='true'

    data=urllib.parse.urlencode(data).encode('utf-8')
    header={}
    #添加header的第一种方法
    header['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'

    request=urllib.request.Request(url,data,header)

    #添加header的第二种方法
    # request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')

    response=urllib.request.urlopen(request)
    # print(response.geturl()) #获取网址print(response.info())  #获取信息
    # print(response.getcode()) # http状态码

    html=response.read().decode('utf-8')
    # print(html)

    target=json.loads(html)
    # print(target)
    # print('\n')
    print(target['translateResult'][0][0]['tgt'])
    # with open("cat_500_600.jpg",'wb') as f:
    #     f.write(cat_html)
