import scrapy


from scrapy.selector import Selector
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/chart",
    ]

    def parse(self, response):

        for table in Selector(response=response).xpath('//div[@class="article"]/div/div/table'):
            print(table)

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