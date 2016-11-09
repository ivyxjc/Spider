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

# def parse_detail_contents_celebrity( list):
#     """
#     将['/celebrity/1009555/', '/celebrity/1357971/'] conver to [1009555,1357971]
#     :param list:
#     :return: list[str]
#     """
#     res = []
#     for i in list:
#         print(i.split('/'))
#         res.append(i.split('/')[-2])
#     print(res)
#     return res
#
# parse_detail_contents_celebrity(['/celebrity/1009555/', '/celebrity/1357971/'])


# import copy
# a= "insert into {} (movie_id,movie_name,movie_url) values({} {} {})".format('ss',1,2,5)
# a="{}".format([1,2,3],1,2,4)
# print(a)
#
# def format(s,list):
#     # 1=<repeat_num <10
#     s_copy=copy.deepcopy(s)
#     index=0
#     for i in range(len(s)):
#         if(s[i]=='{'):
#             index=i
#     s_copy=s_copy[:i]
#     for i in list:
#         s_copy=s_copy+'{}'
#
#
#     res=s_copy+s[index+2:]
#     res=copy.deepcopy(res)
#     return res
#
#
# a=format("insert into (movie_id,movie_name,movie_url) values({})",[1,2,3,4,5,6])
# print(a)
#
#
# def format(s,map):
#     first=0
#     second=0
#     flag=True
#     for i in range(len(s)):
#         if (s[i] == '{' and not flag):
#             second = i
#             break
#         if(s[i]=='{' and flag):
#             first=i
#             flag=False
#
#     keys=""
#     values=""
#     for i in map:
#         keys+=str(i)+","
#         values+='\''+str(map[i])+'\','
#
#     res=s[:first]+keys[:-1]+s[first+2:second]+values[:-1]+s[second+2:]
#     return res
#
#
# a=format("insert into ss ( {}) values( {})",{"11":111,"sssaf":"jgjk","adfaf":"ghkghk"})
# print(a)

# import os
#
# # os.mkdir("text")
# # with open('text\\a.json','w') as f:
# #     f.write("ss")
#
# a=os.path.exists("text\\aa.config.json")
# print(a)
#
# url='https://music.douban.com/subject/1948400/'
# url_list=url.split('/')
# print(url_list)

from douban.db_util import db_about

#
#
# db=db_about()
# res=db.fetch_data('SELECT * FROM douban.movie_name where flag=0 and movie_id>2500000 and movie_id<3000000')
# print(res[0]['movie_id'])
# print(res[0]['flag'])
# print(res)

# import pymysql
#
# connection = pymysql.connect(user='root',
#                                   passwd='123456',
#                                   host='localhost',
#                                   port=3306,
#                                   db='douban',
#                                   cursorclass=pymysql.cursors.DictCursor,
#                                   )
# connection.set_charset('utf8')
# connection.cursor().execute('SET NAMES utf8;')
# connection.cursor().execute('SET CHARACTER SET utf8;')
# connection.cursor().execute('SET character_set_connection=utf8;')
#
# try:
#     with connection.cursor() as cursor:
#         aa = cursor.execute('SELECT * FROM douban.movie_name where flag=0 and movie_id>2500000 and movie_id<3000000')
#         aa=cursor.fetchall()
#         print(aa)
#
# finally:
#     pass


# a = "sss'sdf'sadf"
# a=a.replace('\'', '`')
# print(a)

# list=["safd","asd'f'"]
# for j in range(len(list)):
#     list[j]=list[j].replace('\'','|')
# print(list)
#
# item={'casts': {'1009405': '本尼迪克特·康伯巴奇',
#            '1009409': '迈克尔·斯图巴',
#            '1010581': '切瓦特·埃加福特',
#            '1017912': '斯科特·阿金斯',
#            '1025152': '蒂尔达·斯文顿',
#            '1036383': '本杰明·布拉特',
#            '1040529': '麦斯·米科尔森',
#            '1053587': '瑞秋·麦克亚当斯',
#            '1232518': '阿拉·萨菲',
#            '1301179': '本尼迪克特·王',
#            '1319615': 'Zara Phythian'},
#  'directors': {'1320372': '斯科特·德瑞克森'},
#   'writers': {'1013888': '斯坦·李',
#              '1041593': '史蒂夫·迪特寇',
#              '1293605': '约书亚·奥本海默',
#              '1320120': '乔·斯派茨',
#              '1328309': '托马斯·迪恩·唐纳利'},
#
#  'movie_rating_distribute': ['30.0', '48.9', '19.0', '1.6', '0.4'],
#   'movie_id': '3025375',
#  'movie_imdb_id': 'tt1211837',
#  'movie_length': '115',
#  'movie_name': "奇异博士 ''Doctor Strange",
#  'movie_rating': '8.1',
#   'movie_rating_people_num': '48811',
#
#
#
#  'movie_genre': ['动作', '科幻', '奇幻', '冒险'],
#  'movie_similar': ['6390825',
#                    '25937854',
#                    '25821634',
#                    '25820460',
#                    '26636712',
#                    '24773958',
#                    '10485647',
#                    '24753477',
#                    '25894431',
#                    '25765735'],
#  'movie_tags': ['漫威', '美国', '科幻', '超级英雄', '奇幻', '2016', '漫画改编', '动作'],
#  'rating_better_than': ['88% 奇幻片', '88% 冒险片'],
#  'release_date': ['2016-11-04(中国大陆/美国)', '2016-10-25(英国)'],
# }
# print(item['movie_name'])
# print(item['movie_tags'][1])
#
# def replace_colon( item):
#     for i in ['casts', 'directors', 'writers']:
#         for j in item[i]:
#             item[i][j] =  item[i][j].replace('\'', '`')
#     item['movie_name'] =  item['movie_name'].replace('\'', '`')
#
#     for i in ['movie_genre', 'movie_tags']:
#         for j in range(len(item[i])):
#             item[i][j] =  item[i][j].replace('\'', '`')
#     return item
#
# item=replace_colon(item)
# print(item)


# encoding=utf-8
# author: walker
# date: 2014-05-15
# function: 更改图片尺寸大小
# import os
# import os.path
# from PIL import Image
#
# '''
# filein:  输入图片
# fileout: 输出图片
# width: 输出图片宽度
# height:输出图片高度
# type:输出图片类型（png, gif, jpeg...）
# '''
#
#
# def ResizeImage(filein, fileout, width, height, type):
#     img = Image.open(filein)
#     out = img.resize((width, height), Image.ANTIALIAS)  # resize image with high-quality
#     out.save(fileout, type)
#
#
# if __name__ == "__main__":
#     filein = r'C:\Users\jc\Pictures\aa.png'
#     fileout = r'C:\Users\jc\Pictures\testout.png'
#     width = 295
#     height = 328
#     type = 'png'
#     ResizeImage(filein, fileout, width, height, type)


# from douban.db_util import db_about
#
# db_url=db_about.fetch_data('SELECT movie_id FROM douban.movie_name where flag=0 LIMIT 5;')
# urls=[]
# for i in db_url:
#     urls.append('https://movie.douban.com/subject/'+str(i['movie_id'])+'/')

# import re
# import time
# t1=time.time()
# # time.sleep(3)
# a="1924.30.0"
# if(re.findall('\((.*)\)',a)==[]):
#     print("ss")
#
# print(re.findall('\((.*)\)',a))
# print(time.time()-t1)
# print("{} ---- {}".format('ount', 's'))

# map={}
# print('a' in map.keys())
# list=[]
# for i in range(len(list)):
#     print(i)
#     print(list[i])

def foo():
    count=0
    while (count<10):
        for i in range(10):
            yield i*count
        count+=1


for i in foo():
    print(i)