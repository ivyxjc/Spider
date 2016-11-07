# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import copy
import pymysql
import logging
from tutorial.db_util import db_about






class DoubanMovieDetailPipeline(object):
    """
    处理'movie_id'， 'movie_imdb_id'，'movie_length','movie_name',
    'movie_rating','movie_rating_distribute','movie_rating_people_num',
    """
    def open_spider(self, spider):
        self.db=db_about()

    def process_item(self, item, spider):
        item=self.replace_colon(item=item)
        sql=self.build_insert_movie_detail_sql(item)
        self.db.commit_to_db_buffer(sql)
        self.db.commit()
        return item

    def replace_colon(self,item):
        for i in ['casts', 'directors', 'writers']:
            for j in item[i]:
                item[i][j] = item[i][j].replace('\'', '`')
        item['movie_name'] = item['movie_name'].replace('\'', '`')

        for i in ['movie_genre', 'movie_tags']:
            for j in range(len(item[i])):
                item[i][j] = item[i][j].replace('\'', '`')
        return item


    def build_insert_movie_detail_sql(self,item):
        map=self.build_sql_map(item)
        sql = self.db.format("insert ignore into `douban`.`movie_detail` ({}) values({})",map)
        return sql


    def build_sql_map(self,item):
        map={}
        map=self.build_map(map,item,'movie_id','movie_id')
        map =self.build_map(map,item,'movie_name','movie_name')
        map =self.build_map(map,item,'movie_length','movie_length')
        map =self.build_map(map,item,'movie_imdb_id','movie_imdb_id')
        map =self.build_map(map,item,'movie_rating','movie_rating')
        map =self.build_map(map,item,'movie_rating_people_num','movie_rating_people_num')
        map =self.build_map(map,item['movie_rating_distribute'],'rating_5',0)
        map =self.build_map(map,item['movie_rating_distribute'],'rating_4',1)
        map =self.build_map(map,item['movie_rating_distribute'],'rating_3',2)
        map =self.build_map(map,item['movie_rating_distribute'],'rating_2',3)
        map =self.build_map(map,item['movie_rating_distribute'],'rating_1',4)
        return map

    def build_map(self, map, item, map_key, item_key):
        if (item[item_key] == None or item[item_key] == {} or item[item_key] == ''):
            logging.log(level=logging.INFO, msg="---no item[{}]".format(item_key))
            return map
        else:
            map[map_key] = item[item_key]
            return map





class DoubanCelebrityPipeline(object):
    """
    处理'casts':,'directors','writers
    """
    def open_spider(self, spider):
        self.db = db_about()

    def process_item(self, item, spider):

        sql_celebrity_list=self.build_insert_sql(item,'celebrity')
        sql_movie_celebrity_list=self.build_insert_sql(item,'movie_celebrity')
        # print(sql_celebrity)
        # print(sql_movie_celebrity)
        for i in sql_celebrity_list:
            self.db.commit_to_db_buffer(i)
        for i in sql_movie_celebrity_list:
            self.db.commit_to_db_buffer(i)
        self.db.commit()
        return item


    def build_celebrity_map(self, item):
        """

        :param map:
        :param item:
        :param map_key:
        :param item_key:
        :return: list[map]  [{'celebrity_id:'1231241','celebrity_name:'asff'}...]
        """
        res=[]
        for i in ['casts', 'directors', 'writers']:
            for j in item[i]:
                map={'celebrity_id':j,
                     'celebrity_name':item[i][j]}
                res.append(map)
        return res

    def build_insert_sql(self, item,table_name):
        """

        :param item:
        :param table_name:
        :return: list[sql]
        """
        res=[]
        if(table_name=='celebrity'):
            map_list = self.build_celebrity_map(item)
            for i in map_list:
                sql = self.db.format("insert ignore into `douban`.`celebrity` ({}) values({})", i)
                res.append(sql)
            return res
        elif(table_name=='movie_celebrity'):
            map_list=self.build_movie_celebrity_map_list(item)
            for i in map_list:
                sql = self.db.format("insert ignore into `douban`.`movie_celebrity` ({}) values({})", i)
                res.append(sql)
            return res


    def build_movie_celebrity_map_list(self, item):
        """

        :return:list[map]  [{'celebrity_id:1231241,'celebrity_name:'asff',movie_id:1114321,}...]
        """
        res=[]
        celebrity=['directors', 'writers','casts']
        for i in range(len(celebrity)):
            for j in item[celebrity[i]]:
                map={'celebrity_id':j,
                     'celebrity_name':item[celebrity[i]][j],
                     'role':i,
                     'movie_id':item['movie_id']}
                res.append(map)
        return res

class DoubanListPipeline(object):
    def open_spider(self, spider):
        self.db = db_about()

    def process_item(self, item, spider):
        list=['movie_aka','movie_genre','movie_similar','movie_tags','movie_language','movie_country']
        for i in list:
            sql_list=self.build_insert_sql(i,item)
            for j in sql_list:
                print(j)
                self.db.commit_to_db_buffer(j)
        self.db.commit()
        return item


    def build_insert_sql(self,category,item):
        tags={
            'movie_aka':'movie_aka',
            'movie_genre':'movie_genre',
            'movie_similar':'movie_similar',
            'movie_tags':'movie_tags',
            'movie_language':'movie_language',
            'movie_country':'movie_country',
        }
        res=[]
        s="insert ignore into `douban`.`"+tags[category] +"` ({}) values({})"
        map_list=self.build_map_list(item,category)
        for i in map_list:
            sql=self.db.format(s, i)
            res.append(sql)
        return res


    def build_map_list(self,item,category):
        list=item[category]
        tags={
            'movie_aka': 'movie_aka',
            'movie_genre':'movie_genre',
            'movie_similar':'movie_similar_id',
            'movie_tags':'tags',
            'movie_language': 'movie_language',
            'movie_country': 'movie_country',
        }

        movie_id_tags={
            'movie_aka': 'movie_id',
            'movie_genre':'movie_id',
            'movie_similar':'movie_base_id',
            'movie_tags':'movie_id',
            'movie_language': 'movie_id',
            'movie_country': 'movie_id',
        }

        map_list=[]
        for i in list:
            map_list.append({movie_id_tags[category]:item['movie_id'],
                             tags[category]:i})
        return map_list


class DoubanMovieMapPipeline(object):
    def open_spider(self, spider):
        self.db = db_about()

    def process_item(self, item, spider):
        list = ['rating_better_than', 'release_date']
        for i in list:
            sql_list = self.build_insert_sql(i, item)
            for j in sql_list:
                self.db.commit_to_db_buffer(j)
        self.db.commit()
        return item

    def build_insert_sql(self, category, item):
        tags = {
            'rating_better_than': 'movie_better_than',
             'release_date':  'release_date',
        }
        res = []
        s = "insert ignore into `douban`.`" + tags[category] + "` ({}) values({})"
        map_list = self.build_map_list(item, category)
        for i in map_list:
            sql = self.db.format(s, i)
            res.append(sql)
        return res

    def build_map_list(self, item, category):
        # if(category=='rating_better_than'):
        tag_1={
            'rating_better_than':'tag',
            'release_date':'release_country'
        }
        tag_2={
            'rating_better_than': 'percent',
            'release_date': 'release_date'
        }
        map_list=[]
        item_cat=item[category]
        for i in item_cat:
            map={
                'movie_id':item['movie_id'],
                tag_1[category]:i,
                tag_2[category]:item_cat[i],
            }
            map_list.append(map)
        return map_list
