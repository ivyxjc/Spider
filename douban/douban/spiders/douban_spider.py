import scrapy

from scrapy.selector import Selector
from douban.items import DoubanItem
import logging
import re
from douban.db_util import db_about
import time


class DmozSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]

    start_urls = [
       'https://movie.douban.com/subject/7054604/',
    ]

    t1=time.time()

    # def parse(self, response):
    #     i=0
    #     for href in Selector(response=response).xpath('//div[@class="article"]/div/div/table/tr/td/a/@href'):
    #         url=href.extract()
    #         i+=1
    #         if(i==1):
    #             yield scrapy.Request(url, callback=self.parse_detail_contents)

    def parse(self, response):

        count=0
        for i in range(0,10):
            db_url = db_about.fetch_data('SELECT movie_id FROM douban.movie_name where flag=0 LIMIT 15000;')
            urls = []
            for i in db_url:
                urls.append('https://movie.douban.com/subject/' + str(i['movie_id']) + '/')

            for i in range(len(urls)):
                yield scrapy.Request(urls[i],callback=self.parse_detail_contents)

            count+=1

        print("{} ------------------------------".format(count))
        print(time.time() - self.t1)


        # urls=['https://movie.douban.com/subject/1291583/']
        # for i in urls:
        #     yield scrapy.Request(i,callback=self.parse_detail_contents)



    def parse_detail_contents(self,response):
        #由整个网页构成的selector
        full_sel=Selector(response=response)
        info_sel = Selector(text=full_sel.xpath("//div[@id='info']").extract()[0])
        # text=response.body
        # text=text.decode('utf-8')
        # text=text.replace('\n\n','')
        # print(text)
        item = DoubanItem()

        #str
        item['movie_name'] = self.parse_single_line_excetpion("movie_name",full_sel,"//div[@id='content']/h1/span/text()",False,logging.WARN)


        item['movie_id']=response.url.split('/')[-2]
        # print(response.body)



        # 获取电影导演
        # directors_html=info_sel.xpath("//div[@id='info']/span[1]/span[@class='attrs']/a").extract()
        # item['directors']={}
        # for i in directors_html:
        #     item['directors'][self.parse_detail_contents_celebrity(Selector(text=i).xpath('//a/@href').extract())[0]]\
        #                 =Selector(text=i).xpath('//a/text()').extract()[0]


        item['directors']=self.parse_list_exception('directors',info_sel,"//div[@id='info']/span[1]/span[@class='attrs']/a[@rel='v:directedBy']")
        # print(info_sel.xpath("//div[@id='info']/span[1]/span[@class='attrs']").extract())
        # for i in item['directors']:
        #     print(i,item['directors'][i])
        #
        # print("---------------")

        # 获取电影编剧
        # writers_html = info_sel.xpath("//div[@id='info']/span[2]/span[@class='attrs']/a").extract()
        # item['writers'] = {}
        # for i in writers_html:
        #     item['writers'][self.parse_detail_contents_celebrity(Selector(text=i).xpath('//a/@href').extract())[0]] \
        #         = Selector(text=i).xpath('//a/text()').extract()[0]
        if(item['directors']=={}):
            try:
                if(info_sel.re('<span class="pl">编剧</span>')!=[]):
                    item['writers'] = self.parse_list_exception('directors', info_sel,
                                              "//div[@id='info']/span[1]/span[@class='attrs']/a")
            except:
                logging.log(level=logging.INFO, msg='---Not find 编剧')
        else:
            try:
                if (info_sel.re('<span class="pl">编剧</span>') != []):
                    item['writers'] = self.parse_list_exception('directors', info_sel,
                                                            "//div[@id='info']/span[2]/span[@class='attrs']/a")
            except:
                item['writers']={}
                logging.log(level=logging.INFO, msg='---Not find 编剧')



        # 获取电影演员
        # casts_html=info_sel.xpath("//div[@id='info']/span[@class='actor']/span[@class='attrs']/a").extract()
        # item['casts']={}
        # for i in casts_html:
        #     item['casts'][self.parse_detail_contents_celebrity(Selector(text=i).xpath('//a/@href').extract())[0]] \
        #         = Selector(text=i).xpath('//a/text()').extract()[0]

        item['casts'] = self.parse_list_exception('directors', info_sel,
                                                      "//div[@id='info']/span[@class='actor']/span[@class='attrs']/a")
        # for i in item['casts']:
        #     print(i,item['casts'][i])

        #获取电影风格 list[str]
        # genre=info_sel.xpath("//div[@id='info']/span[@property='v:genre']/text()").extract()
        # item['movie_genre']=genre

        genre=self.parse_single_line_excetpion("movie_genre", info_sel, "//div[@id='info']/span[@property='v:genre']/text()", True)
        item['movie_genre']=genre


        # 获取电影时长
        movie_length=self.parse_single_line_excetpion('movie_length',info_sel,'//span[@property="v:runtime"]/@content',False)
        item['movie_length']=movie_length

        # 获取电影上映日期
        try:
            release_date=self.parse_single_line_excetpion('release_date',info_sel,'//span[@property="v:initialReleaseDate"]/text()',True)
            release_date_map={}
            if(release_date!=None):
                for i in release_date:
                    district=re.findall('\((.*)\)',i)
                    if(district==[]):
                        district='Undefined'
                    else:
                        district=district[0]
                    date=re.findall('(\d{4}-\d{2}-\d{2})',i)[0]
                    release_date_map[district]=date
            item['release_date']=release_date_map
        except:
            release_date_map = {}
            item['release_date'] = release_date_map
            logging.log(level=logging.INFO, msg="--Not find release date")


        # 获取电影又名
        movie_aka=self.parse_re_exception("movie_country",info_sel,'<span class="pl">又名:</span>(.*)<br>')
        item['movie_aka'] = movie_aka

        # try:
        #     movie_aka = info_sel.re('<span class="pl">又名:</span>(.*)<br>')[0]
        #     movie_aka=movie_aka.split(' /')
        #     movie_aka_list=[]
        #     for i in movie_aka:
        #         if(i!=" " and i!="" and i!=None and i!='/'):
        #             movie_aka_list.append(i)
        #     item['movie_aka'] = movie_aka_list
        # except:
        #     logging.log(level=logging.INFO,msg="--Not find movie aka")

        # 获取电影国家 list[str]
        movie_country=self.parse_re_exception("movie_country",info_sel,'<span class="pl">制片国家/地区:</span>(.*)<br>')
        item['movie_country']=movie_country
        # try:
        #     movie_country = info_sel.re('<span class="pl">制片国家/地区:</span>(.*)<br>')[0]
        #     movie_country = movie_country.split(' /')
        #     movie_country_list = []
        #     for i in movie_aka:
        #         if (i != " " and i != "" and i != None and i != '/'):
        #             movie_country_list.append(i)
        #     item['movie_country'] = movie_country
        # except:
        #     logging.log(level=logging.INFO, msg="--Not find movie aka")

        movie_language = self.parse_re_exception("movie_country", info_sel, '<span class="pl">语言:</span>(.*)<br>')
        item['movie_language'] = movie_language

        # try:
        #     movie_language = info_sel.re('<span class="pl">语言:</span>(.*)<br>')[0]
        #     movie_language = movie_language.split(' /')
        #     movie_language_list = []
        #     for i in movie_aka:
        #         if (i != " " and i != "" and i != None and i != '/'):
        #             movie_language_list.append(i)
        #     item['movie_language'] = movie_language
        # except:
        #     logging.log(level=logging.INFO, msg="--Not find movie aka")

        #获取电影imdb id
        try:
            imdb= info_sel.re('http://www.imdb.com/title/(.+?)\"')[0]
            item['movie_imdb_id']=imdb
        except:
            item['movie_imdb_id']=None
            logging.log(level=logging.INFO,msg='---Not find imdb id')


        # 获取电影评分 decimal
        # rating=full_sel.xpath('//div[@id="interest_sectl"]/div/div[@class="rating_self clearfix"]/strong/text()').extract()[0]
        # item['movie_rating']=rating
        rating=self.parse_single_line_excetpion("movie_rating", full_sel, '//div[@id="interest_sectl"]/div/div[@class="rating_self clearfix"]/strong/text()', False)
        item['movie_rating']=rating


        # 获取电影评价人数 , int 可能为空
        # rating_people_num=full_sel.xpath('//div[@class="rating_sum"]/a/span/text()').extract()[0]
        # item['movie_rating_people_num']=rating_people_num
        rating_people_num=self.parse_single_line_excetpion("rating_people_num", full_sel, '//div[@class="rating_sum"]/a/span/text()', False)
        item['movie_rating_people_num']=rating_people_num

        #获取电影评价分布 list[decimal] len=5 可能为空
        rating_distribute=[]
        try:
            for i in range(2,11,2):
                # rating_distribute.append(full_sel.xpath('//div[@class="rating_wrap clearbox"]/span[{}]/text()'.format(i)).extract()[0][:-1])
                rating_distribute.append(self.parse_single_line_excetpion(
                    "movie_rating_distribute",full_sel,'//div[@class="rating_wrap clearbox"]/span[{}]/text()'.format(i),False)[:-1])
        except:
            logging.log(level=logging.INFO,msg="---No distribute")
        item['movie_rating_distribute']=rating_distribute


        #获取电影better than
        rating_better_than=self.parse_single_line_excetpion('rating_better_than',full_sel,'//div[@class="rating_betterthan"]/a/text()',True)
        item['rating_better_than']={}

        try:
            rating_better = {}
            for i in rating_better_than:
                tmp=re.findall('(\d+)\% (.+)',i)
                rating_better[tmp[0][1]]=tmp[0][0]
                item['rating_better_than']=rating_better
        except:
            logging.log(level=logging.INFO, msg="--Not find better than")

        #获取电影标签
        # tags=full_sel.xpath('//div[@class="tags-body"]/a/text()').extract()
        # item['movie_tags']=tags
        tags=self.parse_single_line_excetpion('movie_tags', full_sel, '//div[@class="tags-body"]/a/text()', True)
        item['movie_tags'] = tags

        #获取相似电影
        movie_similar_urls=self.parse_single_line_excetpion('movie_similar',full_sel,'//div[@class="recommendations-bd"]/dl/dd/a/@href',True)
        re_pattern=re.compile('subject/(\d+)/')
        movie_similar=[]
        for i in movie_similar_urls:
            res=re.findall(re_pattern,i)
            movie_similar.append(res[0])
        item['movie_similar']=movie_similar

        yield item


    def parse_re_exception(self,info_title:str,selector:Selector,re:str):
        try:
            movie_aka = selector.re(re)[0]
            movie_aka = movie_aka.split(' /')
            movie_aka_list = []
            for i in movie_aka:
                if (i != " " and i != "" and i != None and i != '/'):
                    movie_aka_list.append(i.replace(" ",""))
            return movie_aka_list
        except:
            logging.log(level=logging.INFO, msg="--Not find "+info_title)
            return []



    def parse_list_exception(self,info_title:str,selecotr:Selector,xpath:str):
        res = {}
        try:
            part_html = selecotr.xpath(xpath).extract()

            for i in part_html:
                res[self.parse_detail_contents_celebrity(Selector(text=i).xpath('//a/@href').extract())[0]] \
                    = Selector(text=i).xpath('//a/text()').extract()[0]
            return res
        except:
            logging.log(level=logging.WARN,msg="---Not find {}".format(info_title))
            return res



    def parse_single_line_excetpion(self, info_title:str, selector:Selector, xpath:str, listOrNot:bool,level=logging.INFO):
        """

        :param selector: Selector
        :param xpath: xpath语句
        :param listOrNot boolean  true  返回 list  ,  false 返回 单个值
        :return:
        """

        try:
            if(listOrNot):
                res=selector.xpath(xpath).extract()
            else:
                res=selector.xpath(xpath).extract()[0]
            return res
        except:
            logging.log(level=level,msg="---Not find {}".format(info_title))
            return None




    def parse_detail_contents_celebrity(self,list):
        """
        将['/celebrity/1009555/', '/celebrity/1357971/'] conver to [1009555,1357971]
        :param list:
        :return: list[str]
        """
        res = []
        for i in list:
            res.append(i.split('/')[-2])
        return res






























        # for table in Selector(response=response).xpath('//div[@class="article"]/div/div/table'):
        #     table=Selector(text=table.extract())
        #     item = DoubanItem()
        #     item['title'] = table.xpath("//table/tr/td/a[@class='nbg']/@title")
        #     item['movie_url'] = table.xpath("//table/tr/td/a[@class='nbg']/@href")
        #     # print(table.xpath("//table/tr/td/a[@class='nbg']/@href").extract())
        #     print(table.xpath("//table/tr/td/a[@class='nbg']/@href"))
        #     print(table.xpath("//table/tr/td/a[@class='nbg']/@href").extract())
        #     print()
        #     # item['movie_id'] = table.xpath("//table/tr/td/a[@class='nbg']/@href").extract().split('/')[-1]
        #     # i+=1
        #     print(table.xpath("//table/tr/td/a[@class='nbg']/@href"))
        #     # print(item['movie_id'])
        #     yield item
        # for href in Selector(response=response).xpath('//div[@id="cat-list-content-main"]/div[@class="cat-item"]/a/@href'):
        #     print('http://www.dmoz.org'+href.extract())
        #     url='http://www.dmoz.org/'+href.extract()
        #
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)

        # def parse_dir_contents(self, response):
        #     for sel in response.xpath('//div/div'):
        #         item = DmozItem()
        #         item['title'] = sel.xpath('a/text()').extract()
        #         item['link'] = [sel.xpath('a/@href').extract(),"sss"]
        #         # item['desc'] = sel.xpath('text()').extract()
        #         yield item