import requests
from xml.dom.minidom import parse
import xml.dom.minidom
import os

import threading

import json

class SiteMap(object):

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

        self.__download_num=0

        #文件位置
        self.__sitemap_text_path="text\\"
        self.__sitemap_json_path="text\\"

        # sitemap存储位置

        self.__sitemap_save_path="E:\\Coding\\douban_data\\"

        self.__sitemap_text_name="sitemap.txt"
        self.__sitemap_json_name="sitemap_config.json"
        self.__map={}


    def __json_to_map(self,filename):

        with open(filename, 'r') as f:
            map= json.load(f)
        return map


    def __map_to_json(self,map,filename):

        with open(filename, "w") as f:
            json.dump(map, f)


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
        json_all_path=self.__sitemap_json_path+self.__sitemap_json_name
        text_all_path=self.__sitemap_text_path+self.__sitemap_text_name
        if(os.path.exists(text_all_path)):
            with open(text_all_path,'r') as f:
                site_str=f.read()
                sitemap=site_str.split('\n')
        else:

            xml_str = self.__get_html_text(self.__base_url)
            DOMTree = xml.dom.minidom.parseString(xml_str)
            collection = DOMTree.documentElement
            elements = collection.getElementsByTagName(self.__pattern_sitemap)
            for i in elements:
                tmp_a = i.getElementsByTagName(self.__pattern_loc)
                sitemap.append(tmp_a[0].childNodes[0].nodeValue)


            if(os.path.exists(self.__sitemap_text_path)):
                with open(text_all_path, 'w') as f:
                    for i in sitemap:
                        f.write(i + '\n')
            else:
                os.mkdir(self.__sitemap_text_path)
                with open(text_all_path, 'w') as f:
                    for i in sitemap:
                        f.write(i+'\n')

        if(os.path.exists(json_all_path)):
            self.__map=self.__json_to_map(json_all_path)
        else:
            map={}
            for i in range(len(sitemap)):
                map[str(i)]=0
            self.__map_to_json(map,json_all_path)
            self.__map =self.__json_to_map(json_all_path)
        return sitemap
    #
    # def save_sitemap_detail(self,start,end):
    #     sitemap=self.get_sitemap()
    #     length=len(sitemap)
    #     if(end>=length):
    #         end=length
    #     for i in range(start,end):
    #         filename=self.__sitemap_save_path+self.__sitemap_tar_prefix+str(i)+'.gz'
    #         with open(filename,"wb") as f:
    #             f.write(self.__get_html_byte(sitemap[i]))

    def save_sitemap_detail(self,page_num):
        sitemap = self.get_sitemap()
        str_page_num=str(page_num)
        length = len(sitemap)
        if (page_num >= length):
            return
        if(self.__map[str_page_num]!=0):
            return

        filename = self.__sitemap_save_path+self.__sitemap_tar_prefix + str_page_num + '.gz'


        self.__map[str_page_num]=1

        with open(filename, "wb") as f:
            f.write(self.__get_html_byte(sitemap[page_num]))

        self.__map[str_page_num]=2
        self.__download_num += 1
        if(self.__download_num%20==0):
            self.__map_to_json(self.__map,self.__sitemap_json_path+self.__sitemap_json_name)











