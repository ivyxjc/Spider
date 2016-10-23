import pymysql
from maoYanBoxOffice.maoyan import Spider,Maoyan
from maoYanBoxOffice.date import *
import copy
import time


connection = pymysql.connect(user='root',
           passwd='123456',
           host='localhost',
           port=3306,
           db='maoyanpiaofang',
           cursorclass=pymysql.cursors.DictCursor,
           )

connection.set_charset('utf8')
connection.cursor().execute('SET NAMES utf8;')
connection.cursor().execute('SET CHARACTER SET utf8;')
connection.cursor().execute('SET character_set_connection=utf8;')

def keyMapInit():
    keyMap={
        "date":0,
        "movies_box":-1,
        "movies_name":None,
        "piaofang_zhanbi":-1,
        "paipian_zhanbi":-1,
        "shangzuolv":-1
    }
    return keyMap

def build_insert_data_sql(map,table_name):
    list=[]
    map_copy=copy.deepcopy(map)
    sql1="insert INTO "+'`'+table_name+'`'+'('
    for i in map_copy:
        sql1+=i+","
        list.append(map[i])

    sql1=sql1[0:-1]+')'

    sql1+="""
    VALUES (
    """

    for i in list:
        if i !=-1 and i is not None:
            sql1+='\''+str(i)+"\',"
        else:
            sql1+="null,"
    sql1=sql1[0:-1]+')'
    return sql1

def commit_to_db(sql1):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql1)
    finally:
        pass

def push_data_to_db(date,date_sql):
    if(is_date_exists(date_sql)!=0):
        return
    time.sleep(2)
    maoyan=Maoyan("http://piaofang.maoyan.com/",date)
    map=keyMapInit()

    data=maoyan.get_today_box()

    for i in data:
        map['movies_name']=i[1][0]
        map['movies_box']=i[2][0]
        map['piaofang_zhanbi']=i[3][0]
        map['paipian_zhanbi']=i[4][0]
        map['shangzuolv']=i[5][0]
        map['date']=date_sql
        sql=build_insert_data_sql(map,'movies_box')
        print(sql)
        commit_to_db(sql)
        connection.commit()

#判断该日期是否已经插入数据库
def is_date_exists(datesql):
    sql_search='SELECT * FROM maoyanpiaofang.movies_box' +\
	' where date= %s'

    try:
        with connection.cursor() as cursor:
            aa=cursor.execute(sql_search,int(datesql))
            return aa
    finally:
        pass


# def is_movie_name_exists(datesql):
#     sql_search='SELECT * FROM maoyanpiaofang.movies_box' +\
# 	' where movies_name= %s'
#
#     try:
#         with connection.cursor() as cursor:
#             aa=cursor.execute(sql_search,int(datesql))
#             return aa
#     finally:
#         pass

# for i in range(0,30):
    # dateList=get_previous_date(2016,6,12)
    # date=None
    # date=str(dateList[0])+"-"+str(dateList[1])+"-"+str(dateList[2])
    # date_sql=str(dateList[0])+str(dateList[1])+str(dateList[2])
    #
    # push_data_to_db('2016-06-11','20160611')

def main(year,month,day,days):

    yearTmp=year
    monthTmp=month
    dayTmp=day
    while(days>=0):
        dateList=get_previous_date(yearTmp,monthTmp,dayTmp)
        if(dateList[1]<10 and dateList[2]<10):
            date=str(dateList[0])+"-0"+str(dateList[1])+"-0"+str(dateList[2])
            date_sql=str(dateList[0])+"0"+str(dateList[1])+"0"+str(dateList[2])
        elif(dateList[1]<10):
            date=str(dateList[0])+"-0"+str(dateList[1])+"-"+str(dateList[2])
            date_sql=str(dateList[0])+"0"+str(dateList[1])+str(dateList[2])
        elif(dateList[2]<10):
            date=str(dateList[0])+"-"+str(dateList[1])+"-0"+str(dateList[2])
            date_sql=str(dateList[0])+str(dateList[1])+"0"+str(dateList[2])
        else:
            date=str(dateList[0])+"-"+str(dateList[1])+"-"+str(dateList[2])
            date_sql=str(dateList[0])+str(dateList[1])+str(dateList[2])


        push_data_to_db(date,date_sql)

        yearTmp=dateList[0]
        monthTmp=dateList[1]
        dayTmp=dateList[2]
        days-=1


main(2012,1,20,500)


