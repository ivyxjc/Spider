import requests
from lxml import etree
import re
import copy

class Spider(object):
    url=None
    html=None

    headers=None
    proxies=None
    cookies=None

    def __init__(self,base_url,cookies=None,proxies=None,headers=None):
        self.url=base_url
        self.headers=headers
        self.proxies=proxies
        self.cookies=cookies

    def get_html_response(self,url,method='GET',params=None):
        if method=='GET':
            html=requests.get(url,cookies=self.cookies,proxies=self.proxies,headers=self.headers)
        elif method=="POST":
            html=requests.get(url,cookies=self.cookies,proxies=self.proxies,headers=self.headers,params=params)
        else:
            html=None
        return html



class Maoyan(Spider):
    __date=0

    def __init__(self,base_url,date,cookies=None,proxies=None,headers=None,):
        super(Maoyan,self).__init__(base_url,cookies=cookies,proxies=proxies,headers=headers)
        self.__date=date
        self.url=base_url+'?date='+date
        print(self.url)
        self.html=self.get_html_response(self.url).text



    def get_today_box(self):
        root=etree.HTML(self.html)

        res=root.xpath('//div[@class="content strip"]//ul')
        returnRes=[]
        r=[-1,-1,-1,-1,-1,-1]
        for i in res:

            r[0]=0

            r[1]=i.xpath('li[@class="c1"]//b/text()')
            r[2]=i.xpath('li[2]//b/text()')

            r[3]=i.xpath('li[3]/text()')
            r[4]=i.xpath('li[4]/text()')
            r[5]=i.xpath('li[5]//span[1]/text()')
            str1=str(r[3][0])
            pattern=re.compile('\d+\.\d+')
            piaofang_zhanbi=re.findall(pattern,str1)
            r[3]=piaofang_zhanbi
            paipian_zhanbi=re.findall(pattern,r[4][0])
            r[4]=paipian_zhanbi
            try:
                shangzuo=re.findall(pattern,r[5][0])
                print(shangzuo)
                if(len(shangzuo)==0):
                    raise IndexError
                r[5]=shangzuo
            except IndexError:
                r[5]=['-1']


            returnRes.append(copy.deepcopy(r))

        return returnRes





        # rrr=res[0].xpath('li[@class="c1"]//b/text()')
        #
        # print(rrr)



# if __name__=='__main__':
    # url="http://piaofang.maoyan.com/"
    #
    # headers={'Host':'piaofang.maoyan.com',
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    #             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #             'Accept-Language': 'en-US,en;q=0.5',
    #             'Accept-Encoding': 'gzip, deflate',
    #             'DNT': '1',
    #             'Connection': 'keep-alive',
    #             'Cache-Control':'max-age=0'}
    #
    # maoyan=Maoyan(url,"2016-06-12",headers=headers)
    #
    # # maoyan.get_main_html()
    # maoyan.get_today_box()

    # print(html.text)





