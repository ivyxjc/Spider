import json
import requests
import bs4
import re
from lxml import etree
import json
import sys
import time
from tutorial.log import Log
import json

#从kuaidaili获取代理并存储为proxy.json

class GetProxy(object):
    def __init__(self):
        self.__proxy_url="http://www.xicidaili.com/nn/"
        self.__filename="proxy.json"
        self.__page="pageNum.txt"
        self.__max_page=10


    def __get_html_byte(self,url):
        response = requests.get(url)
        return response


    def __get_html_text(self,url):
        proxy={"http":"http://127.0.0.1:8080"}
        response = requests.get(url,proxies=proxy)
        if(response.status_code!=200):
            print("fail to get html")
        print(response.text)
        print(Log.log_str("get html text of ",url))
        return response.text


    def __build_selector(self,num):
        selector = etree.HTML(self.__get_html_text(self.build_url(num)))
        return selector

    def __get_page_num(self):
        with open(self.__page,'r') as f:
            a=int(f.read())
        return a

    def __write_page_num(self,num):
        with open(self.__page,'w') as f:
            print(Log.log_str("write page num", num))
            f.write(str(num))

    def build_url(self, num):
        url = self.__proxy_url + str(num)
        return url

    # 快代理
    # def get_ips_ports(self,num):
    #     """
    #
    #     :return: list[str]
    #     """
    #     selector=self.__build_selector(num)
    #     ips = selector.xpath('//td[@data-title="IP"]/text()')
    #     ports = selector.xpath('//td[@data-title="PORT"]/text()')
    #     res=[]
    #     if (len(ips) != len(ports)):
    #         print("ips' length is not equal to posts' length")
    #     else:
    #         for i in range(len(ips)):
    #             a = ips[i] + ":" + ports[i]
    #             res.append(a)
    #     return res

    #西祠代理
    def get_ips_ports(self,num):
        """

        :return: list[str]
        """
        selector=self.__build_selector(num)
        ips = selector.xpath('//tr[@class="odd"]/td[2]/text()')
        ports = selector.xpath('//tr[@class="odd"]/td[3]/text()')
        ips_2 = selector.xpath('//tr[@class=""]/td[2]/text()')
        ports_2 = selector.xpath('//tr[@class=""]/td[3]/text()')
        res=[]
        if (len(ips) != len(ports)):
            print("ips' length is not equal to posts' length")
        else:
            for i in range(len(ips)):
                a = ips[i] + ":" + ports[i]
                res.append(a)
        if (len(ips_2) != len(ports_2)):
            print("ips' length is not equal to posts' length")
        else:
            for i in range(len(ips_2)):
                a = ips_2[i] + ":" + ports_2[i]
                res.append(a)
        print(res)
        return res

    def write(self):
        """
        向filename中写入proxy
        :return:
        """
        num=self.__get_page_num()
        while(num<self.__max_page):
            num+=1
            ip_ports=self.get_ips_ports(num)

            with open(self.__filename,'a') as f:
                for i in ip_ports:
                    f.write(i+'\n')
            print(Log.log_str("write proxy", num))
            a=self.__get_page_num()
            a+=1
            self.__write_page_num(a)

        with open(self.__filename,'r') as f:
            proxy=f.read()
            proxy=proxy.split('\n')
            map={}
            for i in range(len(proxy)):
                map[i]=proxy[i]
        with open(self.__filename,'w') as f:
            json.dump(map,f)

    def refresh(self):
        """
        将pageNum设为1
        清空filename文件
        重新write
        :return:
        """
        self.__write_page_num(0)
        with open(self.__filename,'w') as f:
            f.truncate()
        print(Log.log_str("refresh",'\n',"-------------------------------------------"))
        self.write()



gp=GetProxy()
gp.refresh()