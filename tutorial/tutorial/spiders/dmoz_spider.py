import scrapy
from lxml import etree
from tutorial.items import DmozItem
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/",
    ]

    def parse(self, response):
        # print(response.body.split('\r\n\r\n'))
        'div.cat-list.results.leaf-nodes > div.cat-item > a '
        for href in response.xpath('//div[@id="cat-list-content-main"]/div[@class="cat-item"]/a/@href'):
            print('http://www.dmoz.org'+href.extract())
            url='http://www.dmoz.org/'+href.extract()

            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//div/div'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            # item['desc'] = sel.xpath('text()').extract()
            yield item