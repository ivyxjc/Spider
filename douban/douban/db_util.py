
import json
import copy
import pymysql
import logging


class db_about(object):
    # -*- coding: utf-8 -*-

    # Define your item pipelines here
    #
    # Don't forget to add your pipeline to the ITEM_PIPELINES setting
    # See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
    # def __init__(self):
    #     self.connection = pymysql.connect(user='root',
    #                                       passwd='123456',
    #                                       host='localhost',
    #                                       port=3306,
    #                                       db='douban',
    #                                       cursorclass=pymysql.cursors.DictCursor,
    #                                       )
    #     self.connection.set_charset('utf8')
    #     self.connection.cursor().execute('SET NAMES utf8;')
    #     self.connection.cursor().execute('SET CHARACTER SET utf8;')
    #     self.connection.cursor().execute('SET character_set_connection=utf8;')


    connection = pymysql.connect(user='root',
                                          passwd='123456',
                                          host='localhost',
                                          port=3306,
                                          db='douban',
                                          cursorclass=pymysql.cursors.DictCursor,
                                          )
    connection.set_charset('utf8')
    connection.cursor().execute('SET NAMES utf8;')
    connection.cursor().execute('SET CHARACTER SET utf8;')
    connection.cursor().execute('SET character_set_connection=utf8;')

    @classmethod
    def format(self, s, map):
        """
        map={1:aa,
            2:bb,
            3:cc}
        将"insert into table ({}) values ({}) " 转换为insert into table (1,2,3) values (aa,bb,cc)
        便于插入
        :param s:
        :param map:
        :return:
        """
        first = 0
        second = 0
        flag = True
        for i in range(len(s)):
            if (s[i] == '{' and not flag):
                second = i
                break
            if (s[i] == '{' and flag):
                first = i
                flag = False

        keys = ""
        values = ""
        for i in map:
            keys += str(i) + ","
            values += '\'' + str(map[i]) + '\','

        res = s[:first] + keys[:-1] + s[first + 2:second] + values[:-1] + s[second + 2:]
        return res



    ## db操作
    @classmethod
    def commit_to_db_buffer(self, sql1):
        try:
            with self.connection.cursor() as cursor:
                return cursor.execute(sql1)
        except Exception:
            logging.log(level=logging.WARN, msg="commit to db fails "+sql1)
        finally:
            pass

    @classmethod
    def commit(self):
        self.connection.commit()

    @classmethod
    def fetch_data(self,sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception:
            logging.log(level=logging.WARN, msg="fail to fetch data "+sql)
        finally:
            pass

