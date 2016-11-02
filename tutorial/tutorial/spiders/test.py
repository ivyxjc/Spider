# from scrapy import Selector
#
# sel = Selector(text="""
#      <ul class="list">
#          <li>1</li>
#          <li>2</li>
#          <li>3</li>
#      </ul>
#      <ul class="list">
#          <li>4</li>
#          <li>5</li>
#          <li>6</li>
#      </ul>""")
#
# xp=lambda x:sel.xpath(x).extract()
#
# print(xp("//li[1]"))



# import scrapy
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import Join, MapCompose, TakeFirst
# from w3lib.html import remove_tags
#
# def filter_price(value):
#     if value.isdigit():
#         return value
#
# class Product(scrapy.Item):
#     name = scrapy.Field(
#         input_processor=MapCompose(remove_tags),
#         output_processor=Join(),
#     )
#     price = scrapy.Field(
#         input_processor=MapCompose(remove_tags, filter_price),
#         output_processor=TakeFirst(),
#     )
#     # name=scrapy.Field()
#     # price=scrapy.Field()
#
#
# il = ItemLoader(item=Product())
# il.add_value('name', [u'Welcome to my', u'<strong>website</strong>'])
# il.add_value('price', [u'&euro;', u'<span>1000</span>'])
# print(il.load_item())
# print(il)




# import requests
#
# proxies = {
#     "http": "http://127.0.0.1:8080",
#     "https": "http://127.0.0.1:8080",
# }
#
# response=requests.get("https://movie.douban.com/chart",proxies=proxies)
# print(response.status_code)

def parse_detail_contents_celebrity( list):
    """
    将['/celebrity/1009555/', '/celebrity/1357971/'] conver to [1009555,1357971]
    :param list:
    :return: list[str]
    """
    res = []
    for i in list:
        print(i.split('/'))
        res.append(i.split('/')[-2])
    print(res)
    return res

parse_detail_contents_celebrity(['/celebrity/1009555/', '/celebrity/1357971/'])