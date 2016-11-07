# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanItem(scrapy.Item):
    #电影id int
    movie_id = scrapy.Field()
    #电影名称 str
    movie_name=scrapy.Field()
    #电影风格   list[str]
    movie_genre=scrapy.Field()

    #电影时长  int
    movie_length=scrapy.Field()
    #imdb编号, str
    movie_imdb_id=scrapy.Field()
    #上映日期 map{district: date,...}
    release_date=scrapy.Field()

    # 电影评分 decimal
    movie_rating=scrapy.Field()
    # 电影评价人数 int
    movie_rating_people_num=scrapy.Field()
    # 电影评价分布 decimal
    movie_rating_distribute=scrapy.Field()
    # 电影better than  list[]
    rating_better_than=scrapy.Field()

    #电影标签 list[str]
    movie_tags=scrapy.Field()

    movie_similar=scrapy.Field()

    # 国家或者地区  list[str]
    movie_country = scrapy.Field()
    # 电影别名  list[str]
    movie_aka = scrapy.Field()
    # 电影语言 list[str]
    movie_language=scrapy.Field()

    #导演 list[str]
    directors = scrapy.Field()
    #编剧 list[str]
    writers=scrapy.Field()
    #演员 list[str]
    casts=scrapy.Field()



