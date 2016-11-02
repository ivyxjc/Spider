import scrapy


from scrapy.selector import Selector
from tutorial.items import DoubanItem
import logging

class DmozSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/chart",
    ]

    def parse(self, response):
        i=0
        for href in Selector(response=response).xpath('//div[@class="article"]/div/div/table/tr/td/a/@href'):
            url=href.extract()
            i+=1
            if(i==1):
                yield scrapy.Request(url, callback=self.parse_detail_contents)

    def parse_detail_contents(self,response):
        sel=Selector(response=response)
        text=response.body
        text=text.decode('utf-8')
        text=text.replace('\n\n','')

        item = DoubanItem()
        item['title'] = sel.xpath("//div[@id='content']/h1/span/text()").extract()
        directors=sel.xpath("//div[@id='info']/span[1]/span[@class='attrs']/a/@href").extract()
        print(directors)
        item['directors']=self.parse_detail_contents_celebrity(directors)
        casts=sel.xpath("//div[@id='info']/span[@class='actor']/span[@class='attrs']/span/a/@href").extract()
        print(casts)
        item['casts']=self.parse_detail_contents_celebrity(casts)
        print(item['directors'])
        print(item['casts'])


    def parse_detail_contents_celebrity(self,list):
        """
        将['/celebrity/1009555/', '/celebrity/1357971/'] conver to [1009555,1357971]
        :param list:
        :return: list[str]
        """
        res=[]
        for i in list:
            print(i.split('/'))
            res.append(i.split('\/')[-2])
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