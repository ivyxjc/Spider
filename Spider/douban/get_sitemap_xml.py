import requests
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import gzip
import threading
import random
import json

class SiteMap(threading.Thread):

    """
    豆瓣sitemap_index.xml格式如下(2016-10-29):

    <sitemapindex>
        <sitemap>
            <loc>https://www.douban.com/sitemap3782.xml.gz</loc>
            <lastmod>2016-10-19T10:36:31Z</lastmod>
        </sitemap>
        <sitemap>
            <loc>https://www.douban.com/sitemap3783.xml.gz</loc>
            <lastmod>2016-10-19T10:36:31Z</lastmod>
        </sitemap>
    </sitemapindex>

    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.__base_url = "https://www.douban.com/sitemap_index.xml"
        self.__pattern_sitemap= "sitemap"
        self.__pattern_loc="loc"

        self.__sitemap_tar_prefix="sitemap"
        self.__lock= threading.Lock()

        self.__download_num=0

        #文件位置
        self.__sitemap_text_path="text\\sitemap.txt"
        self.__sitemap_json_path="text\\sitemap_config.json"

        self.__map = self.__json_to_map()



    def __json_to_map(self):
        self.__lock.acquire()
        with open("text\\sitemap_config.json", 'r') as f:
            map= json.load(f)
        return map
        self.__lock.release()

    def __map_to_json(self):
        self.__lock.acquire()
        with open(self.__sitemap_json_path, "w") as f:
            json.dump(self.__map, f)
        self.__lock.release()

    def __get_html_byte(self,url):
        response=requests.get(url)
        return response.content

    def __get_html_text(self,url):
        response=requests.get(url)
        return response.text

    def get_sitemap(self):
        """
        :return: [https://www.douban.com/sitemap.xml.gz, https://www.douban.com/sitemap.xml1.gz...]
        """
        sitemap=[]
        if(os.path.exists(self.__sitemap_text_path)):
            print("yes")
            with open(self.__sitemap_text_path,'r') as f:
                site_str=f.read()
                sitemap=site_str.split('\n')
        else:
            xml_str=self.__get_html_text(self.__base_url)
            DOMTree =xml.dom.minidom.parseString(xml_str)
            collection = DOMTree.documentElement
            elements=collection.getElementsByTagName(self.__pattern_sitemap)
            for i in elements:
                tmp_a=i.getElementsByTagName(self.__pattern_loc)
                (tmp_a[0].childNodes[0].nodeValue)
                sitemap.append(tmp_a[0].childNodes[0].nodeValue)
            with open(self.__sitemap_text_path, 'w') as f:
                for i in sitemap:
                    f.write(i+'\n')

        return sitemap

    # def save_sitemap_detail(self,start,end):
    #     sitemap=self.get_sitemap()
    #     os.chdir("sitemap")
    #     length=len(sitemap)
    #     if(end>=length):
    #         end=length
    #     for i in range(start,end):
    #         filename=self.__sitemap_tar_prefix+str(i)+'.gz'
    #         with open(filename,"wb") as f:
    #             f.write(self.__get_html_byte(sitemap[i]))

    def save_sitemap_detail(self,page_num):
        sitemap = self.get_sitemap()
        str_page_num=str(page_num)

        os.chdir("site")
        length = len(sitemap)
        if (page_num >= length):
            return
        if(self.__map[str_page_num]!=0):
            return

        filename = self.__sitemap_tar_prefix + str_page_num + '.gz'

        self.__lock.acquire()
        self.__map[str_page_num]=1
        self.__lock.acquire()
        with open(filename, "wb") as f:
            f.write(self.__get_html_byte(sitemap[page_num]))
        self.__lock.acquire()
        self.__map[str_page_num]=2
        self.__download_num += 1
        if(self.__download_num%20==0):
            self.__map_to_json()




    def creat_thread(self,start,end):

        print('thread %s is running...' % threading.current_thread().name)
        num=random.randint(start,end)
        print(num)
        self.save_sitemap_detail(num)


    def create_multiple_thread(self,start,end,thread_num):
        t=[]
        for i in range(thread_num):
            t.append(threading.Thread(target=self.creat_thread(start,end), name="CreateThread " + str(i)))
        for i in range(thread_num):
            t[i].start()

    def run(self):
        self.create_multiple_thread(0,2000,10)

        # for i in range(thread_num):
        #     t[i].join()

s=SiteMap()

thread_num=10
t=[]
for i in range(thread_num):
    t.append(threading.Thread(target=s.run(), name="CreateThread " + str(i)))
for i in range(thread_num):
    t[i].start()








