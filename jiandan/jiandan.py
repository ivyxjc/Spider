import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
import random
import os
import time

class Jiandan(object):
    __url="http://jandan.net/ooxx/"
    __html=None
    __header={'Host': 'jandan.net',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'DNT': '1',
                'Connection': 'keep-alive'}

    #目前最大页面的页码
    __pageNum=2012

    __session=None
    __proxies=None
    __cookies=None


    def __init__(self,cookies=None,proxies=None):
        if(cookies!=None and proxies!=None):
            self.__session=requests.session()
            self.__proxies=proxies
            self.__cookies=cookies
        elif cookies!=None:
            self.__session=requests.session()
            self.__cookies=cookies
        elif proxies!=None:
            self.__session=requests.session()
            self.__proxies=proxies
        else:
            pass

        self.__html=self.__get_html_str(self.__url)
        # print(self.__html)


    #读取煎蛋网页面使用
    def __get_html_str(self,url):
        html=None

        if(self.__cookies!=None and self.__proxies!=None):
            html=self.__session.get(url,proxies=self.__proxies,cookies=self.__cookies,headers=self.__header)
        elif self.__cookies!=None:
            html=self.__session.get(url,cookies=self.__cookies,headers=self.__header)
        elif self.__proxies!=None:
            html=self.__session.get(url,proxies=self.__proxies,headers=self.__header)
        else:
            html=requests.get(url,headers=self.__header)
        if(html.status_code==200):
            return html.text
        else:
            print("html读取失败")
            return None

    #读取煎蛋网页面使用
    def __get_html_byte(self,url):
        html=None

        if(self.__cookies!=None and self.__proxies!=None):
            html=self.__session.get(url,proxies=self.__proxies,cookies=self.__cookies,headers=self.__header)
        elif self.__cookies!=None:
            html=self.__session.get(url,cookies=self.__cookies,headers=self.__header)
        elif self.__proxies!=None:
            html=self.__session.get(url,proxies=self.__proxies,headers=self.__header)
        else:
            html=requests.get(url,headers=self.__header)
        if(html.status_code==200):
            return html.content
        else:
            print("html读取失败")
            return None



    #读取图片使用
    def __get_img_byte(self,url):
        res=requests.get(url,proxies=None,cookies=None)
        return res.content


    def get_page_num(self):
        if(self.__html)!=None:
            a=self.__html.find('current-comment-page')+23
            b=self.__html.find(']',a)
        self.__pageNum=self.__html[a:b]
        return self.__html[a:b]

    # 根据页面内获得图片网址,图片赞同数,反对数,并以列表形式返回,
    def get_imgs_details(self,pageNum):
        time.sleep(5)
        res=[]
        # http://jandan.net/ooxx/page-2011#comments
        url=self.__url+"page-"+str(pageNum)+"#comments"
        # print(url)
        html=self.__get_html_str(url)
        # soup=BeautifulSoup(html,'html.parser')
        # source_html=soup.find_all("ol","commentlist")
        # print(source_html)
        # soup=BeautifulSoup(str(source_html),"html.parser")
        # source_list=soup.findAll("li",attrs={"id":re.compile("comment-\d+")})
        # print(source_list)
        soup=BeautifulSoup(html,'html.parser')
        source_list=soup.findAll("div",attrs={"class":"text"})
        for i in source_list:
            # print(i)
            imgPattern=re.compile("\"http://ww\d\.sinaimg\.cn/large.+?\"")
            imgUrl=re.findall(imgPattern,str(i))

            #获取整个投票部分的源码
            soup=BeautifulSoup(str(i),"html.parser")
            voteHtml=soup.findAll("div",attrs={"class","vote"})
            #获取赞成票的数量
            upVoteNumPattern=re.compile("cos_support-\d+\">+(\d+)</span>")
            upVoteNum=re.findall(upVoteNumPattern,str(voteHtml))
            #获取反对票的数量
            downVoteNumPattern=re.compile("cos_unsupport-\d+\">+(\d+)</span>")
            downVoteNum=re.findall(downVoteNumPattern,str(voteHtml))
            dict=self.dict_init()
            try:
                dict["img_url"]=imgUrl[0][1:-1]
                dict["upvote"]=upVoteNum[0]
                dict['downvote']=downVoteNum[0]
            except IndexError:
                print(pageNum)
                print(i)
                print(imgUrl)
            res.append(dict)
        for i in res:
            print(i)
        return res

    def dict_init(self):
        dict={"img_url":None,
             "upvote":-1,
             "downvote":-1,}
        return dict

    #存储图片到硬盘
    def save_imgs(self,startPageNum,savePagesNum=40,saved=0):
        pageNum=startPageNum-saved
        foldername=int(saved/40)
        while(pageNum>=startPageNum-saved-savePagesNum):
            if(pageNum%40==0):
                foldername=int((1912-pageNum)/40)

            if(os.path.exists("E:\\program\\python\\spider\\jiandan\\pic\\"+str(foldername))):
                os.chdir("E:\\program\\python\\spider\\jiandan\\pic\\"+str(foldername))
            else:
                os.mkdir("E:\\program\\python\\spider\\jiandan\\pic\\"+str(foldername))
                os.chdir("E:\\program\\python\\spider\\jiandan\\pic\\"+str(foldername))

            pageNum-=1
            imgDetailsList=self.get_imgs_details(pageNum)
            for i in imgDetailsList:
                if(int(i['downvote'])==0):
                    continue
                if(int(i['upvote'])/int(i['downvote'])<1.5):
                    continue
                filename=i['upvote']+"__"+i['downvote']+"__"+i["img_url"][-12:]
                img_content=self.__get_img_byte(i["img_url"])

                with open(filename,'wb')as f:
                    f.write(img_content)

            if(pageNum%10==0):
                print("+++++++++++++++++++++++")
                print(pageNum)
                print("+++++++++++++++++++++++")


if __name__=='__main__':
    proxies = {
            'http':'180.169.18.145:3128',
            'http':'106.75.128.90:80',
            'http':'119.147.161.55:3128',
            'http':'120.25.202.201:8090',
            'http':'123.126.32.102:8080',
            'http':'183.61.236.54:3128',
            'http':'113.108.82.29:8080',
            'http':'101.200.179.38:3128',
            'http':'112.74.206.59:3128',
            'http':'61.135.217.16:80'}

    cookies={
        "336678870":"97c2E7jZx/U21qf6YL7XjNdTKFne5zH0W+0JD0Gu0Q",
        "Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c":"1465539564",
        "Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c":"1465529586,1465529814",
        "_ga":"GA1.2.1552856505.1465529586",
        "jdna":"596e6fb28c1bb47f949e65e1ae03f7f5#1465540803721",
        "nsfw-click-load":"off"}


    jiandan=Jiandan(cookies=cookies)
    jiandan.save_imgs(2012,600,380)

