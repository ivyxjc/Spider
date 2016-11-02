# encoding=utf8
import requests
from http import cookiejar
from lxml import etree
from zhihuAnalysis.LogAndError import *
import re
import pymysql
import json
from bs4 import BeautifulSoup
import time
import math
import os
import queue

requests = requests.Session()
requests.cookies = cookiejar.LWPCookieJar('cookies')
connection = pymysql.connect(user='root',
           passwd='123456',
           host='localhost',
           port=3306,
           db='zhihuanalysis',
           cursorclass=pymysql.cursors.DictCursor,
           )

connection.set_charset('utf8')
connection.cursor().execute('SET NAMES utf8;')
connection.cursor().execute('SET CHARACTER SET utf8;')
connection.cursor().execute('SET character_set_connection=utf8;')


try:
    requests.cookies.load(ignore_discard=True)
except:
    Logging.error(u"你还没有登录知乎哦 ...")
    Logging.info(u"执行 `python auth.py` 即可以完成登录。")
    raise Exception("无权限(403)")

def keyMapInit():
    keyMap={
        "hash_id":None,
        "user_custom_url":None,
        "user_name":None,
        "agree_num":None,
        "thanks_num":None,
        "gender":None,

        "questions":None,
        "answers":None,
        "articles":None,
        "collections":None,
        "commonEdits":None,

        "followees":None,
        "followers":None,

        "bio":None,
        "description":None,

        "location_item":None,
        "business_item":None,

        "employment_item":None,
        "position_item":None,
        "education_item":None,
        "education_extra_item":None,

    }
    return keyMap


def get_xsrf(url):
    r=requests.get(url)
    if int(r.status_code)!=200:
        raise NetworkError("验证码请求失败")
    else:
        result = re.compile(r"\<input\stype=\"hidden\"\sname=\"_xsrf\"\svalue=\"(\S+)\"", re.DOTALL).findall(r.text)
    if len(result)<1:
        Logging.error("提取xsrf失败")
        return None
    return result


def get_hash_id(html):
    root=etree.HTML(html)
    hash_id=root.xpath('//button[@data-follow="m:button"]/@data-id')[0]
    if hash_id is None:
        raise ParseError("hash_id为None")

    return hash_id

def get_target_data(html):
    keymap=keyMapInit()
    root=etree.HTML(html)
    #not null
    keymap['hash_id'] = get_hash_id(html)
    # keymap['user_custom_url']
    keymap['user_name'] =root.xpath('//a[@class="name"]/text()')[0]
    # keymap['agree_num'] =(int)(root.xpath('//span[@class="zm-profile-header-user-agree"]/strong/text()')[0])
    keymap['gender'] = get_gender(root)
    user_info_agree_thanks = root.xpath('//div[@class="zm-profile-header-info-list"]')
    keymap['agree_num'] = user_info_agree_thanks[0].xpath('//span/strong/text()')[0]
    keymap['thanks_num'] = user_info_agree_thanks[0].xpath('//span/strong/text()')[1]


    keymap['questions'] = root.xpath('//div[@class="profile-navbar clearfix"]/a/span/text()')[1]
    keymap['answers'] = root.xpath('//div[@class="profile-navbar clearfix"]/a/span/text()')[2]
    keymap['articles'] = root.xpath('//div[@class="profile-navbar clearfix"]/a/span/text()')[3]
    keymap['collections'] = root.xpath('//div[@class="profile-navbar clearfix"]/a/span/text()')[4]
    keymap['commonEdits'] = root.xpath('//div[@class="profile-navbar clearfix"]/a/span/text()')[5]

    keymap['location_item'] = get_data(root,'//span[@class="location item"]/@title',0)
    keymap['business_item'] = get_data(root,'//span[@class="business item"]/@title',0)
    keymap['employment_item'] = get_data(root,'//span[@class="employment item"]/@title',0)
    keymap['position_item'] = get_data(root,'//span[@class="position item"]/@title',0)
    keymap['education_item'] = get_data(root,'//span[@class="education item"]/@title',0)
    keymap['education_extra_item'] = get_data(root,'//span[@class="education-extra item"]/@title',0)


    follow=root.xpath('//div[@class="zm-profile-side-following zg-clear"]/a/strong/text()')
    keymap['followees'] = follow[0]
    keymap['followers'] = follow[1]

    # can be null
    bio=get_data(root,'//span[@class="bio"]/@title',0)
    if bio is None:
        keymap['bio']='0'
    else:
        keymap['bio']='1'
    p=re.compile(r'<span class="content">([\s\S]+?)</span>')

    res=re.findall(p,html)
    if len(res)!=0:
        keymap['description']='1'
    else:
        keymap['description']='0'
    return keymap

def get_gender(root):
    gender_description=root.xpath('//span[@class="item gender"]/i/@class')
    if len(gender_description)==0:
        return '3'
    elif re.match(r".*female.*",gender_description[0]):
        return '0'
    elif re.match(r".*male.*",gender_description[0]):
        return '1'
    else:
        return '2'



    # print(user_info_agree.xpath('//span/strong'))

    keymap['location_item']=get_data(root,'//span[@class="location item"]/@title',0)
    keymap['business_item']=get_data(root,'//span[@class="business item"]/@title',0)
    keymap['employment_item']=get_data(root,'//span[@class="employment item"]/@title',0)
    keymap['position_item']=get_data(root,'//span[@class="position item"]/@title',0)

    keymap['education_item']=get_data(root,'//span[@class="education item"]/@title',0)
    keymap['education_extra_item']=get_data(root,'//span[@class="education-extra item"]/@title',0)

    return keymap


def get_data(root,pattern,rank):
    target=root.xpath(pattern)

    if len(target)!=0:
        return target[rank]
    else:
        return None

def build_insert_data_sql(map):
    list=[]

    sql1="insert INTO zhihu2("
    for i in map:
        sql1+=i+","
        list.append(map[i])

    sql1=sql1[0:-1]+')'
    sql1+="""
    VALUES (
    """
    for i in list:
        if i is not None:
            if re.match(r'^\d*$',i):
                sql1+=i+","
            else:
                sql1+='\''+i+"\',"
        else:
            sql1+="null,"

    sql1=sql1[0:-1]+')'
    # print(sql1)
    return sql1

#判断user_custom_url在table中是否出现过
def is_user_exists(user_custom_url,tableName):
    sql_search='SELECT * FROM zhihuanalysis.'+tableName +\
	'where user_custom_url= %s'

    try:
        with connection.cursor() as cursor:
            aa=cursor.execute(sql_search,user_custom_url)
            return aa
    finally:
        pass



def commit_to_db(sql1):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql1)
    finally:
        pass


def push_target_data_to_db(url):
    r=requests.get(url)
    if(r.status_code==200):
        map=get_target_data(r.text)
        user_custom_url=url.split('/')[-2]
        map['user_custom_url']=user_custom_url
        sql=build_insert_data_sql(map)
        commit_to_db(sql)
    else:
        raise NetworkError("网络故障")


def get_followees(user_custom_url,start_num,end_num):
    followees_all_list=[]
    base_url = "https://www.zhihu.com/people/"
    url = base_url+user_custom_url+"/followees"
    r = requests.get(url)
    Logging.info("sleeping")
    hash_id=get_hash_id(r.text)
    xsrf=get_xsrf(url)

    for i in range(max(int(start_num/20),1),int(end_num/20)):
        offset=i*20
        post_url="https://www.zhihu.com/node/ProfileFolloweesListV2"
        params = json.dumps({"offset": offset, "order_by": "created", "hash_id": hash_id})
        data={
            '_xsrf':xsrf,
            'method':'next',
            'params':params
        }

        header = {
            'Host': 'www.zhihu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.zhihu.com/people/excited-vczh/followees',
            'Content-Length': '172',
            'Connection': 'keep-alive'
                    }
        time.sleep(1)
        Logging.info("sleeping....")
        r_post=requests.post(post_url,data=data,headers=header)
        if r_post.status_code!=200:
            continue
        followees_list = r_post.json()["msg"]
        Logging.info("followee_list Append"+str(i)+"th page")
        for i in followees_list:
            followees_all_list.append(i)

    followees_user_custom_url=[]
    for j in range(0,len(followees_all_list)):
        followee_soup = BeautifulSoup(followees_all_list[j], "lxml")
        followee_etree=etree.HTML(followees_all_list[j])
        user_custom_url=get_data(followee_etree,"//a[@class='zm-item-link-avatar']/@href",0)
        if user_custom_url is not None:
            user_custom_url=user_custom_url.split('/')[-1]
            followees_user_custom_url.append(user_custom_url)
    return followees_user_custom_url



def get_followers(user_custom_url,start_num,end_num):

    base_url = "https://www.zhihu.com/people/"
    url = base_url+user_custom_url+"/followers"
    r = requests.get(url)
    try_times=0
    while(r.status_code!=200 and try_times<5):
        r=requests.get(url)
        try_times+=1

    if(r.status_code!=200):
        raise NetworkError("网络问题，无法获得_xsrf和hash_id")


    hash_id=get_hash_id(r.text)
    Logging.info(hash_id)
    xsrf=get_xsrf(url)
    Logging.info(xsrf)
    followers_user_custom_url=[]
    filename="followers\\"+user_custom_url+'_followers.txt'
    for i in range(max(int(start_num/20),1),min(530,int(end_num/20))):
        followers_user_custom_url=[]
        followers_all_list=[]
        offset=i*20
        post_url="https://www.zhihu.com/node/ProfileFollowersListV2"
        params = json.dumps({"offset": offset, "order_by": "created", "hash_id": hash_id})
        data={
            '_xsrf':xsrf,
            'method':'next',
            'params':params
        }

        header = {
            'Host': 'www.zhihu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.zhihu.com/people/excited-vczh/followers',
            'Content-Length': '172',
            'Connection': 'keep-alive',
                    }

        time.sleep(1)
        Logging.info("sleeping....")

        r_post=requests.post(post_url,data=data,headers=header)
        if r_post.status_code!=200:
            continue
        followers_list = r_post.json()["msg"]
        Logging.info("follower_list Append "+str(i)+"th page")

        if(i%10==0):
            Logging.info_important(str(i))
            Logging.info("follower_list Append "+str(i)+"th page")

        for k in followers_list:
            followers_all_list.append(k)



        for j in range(0,len(followers_all_list)):
            followee_etree=etree.HTML(followers_all_list[j])
            user_custom_url_tmp=get_data(followee_etree,"//a[@class='zm-item-link-avatar']/@href",0)
            if(user_custom_url_tmp!=None):
                p='//div[@class="details zg-gray"]/a[@href="'+user_custom_url_tmp+'"]/text()'
            else:
                continue
            user_agree_num=get_data(followee_etree,p,0)
            user_agree_num=re.findall(r'(\d+)',user_agree_num)[0]
            if user_custom_url_tmp is not None and int(user_agree_num)>=10 :
                user_custom_url_tmp=user_custom_url_tmp.split('/')[-1]
                followers_user_custom_url.append(user_custom_url_tmp)

        with open(filename,'a') as f:
            Logging.info("写入"+user_custom_url+" "+str(i*20))
            for i in followers_user_custom_url:
                f.write(i+"\n")
    Logging.info_important("200000")
    return followers_user_custom_url

def get_followers_param_num(i):
    return (i*i+i)*10

def sqrt(i):
    return int(math.sqrt(i))

#查看cusr_cutom_url是否是合法的
def is_user_custom_url_valid(user_custom_url):
    base_url="https://www.zhihu.com/people/"
    url=base_url+user_custom_url+"/followers"
    r=get_html_from_url(url)
    if(r!=None):
        return r
    else:
        return None


#从url获取html，最多尝试5次（可更改）,若5次均失败，返回None
def get_html_from_url(url):
    r=requests.get(url)
    count=0
    while(r.status_code!=200 and count<=5):
        r=requests.get(url)
        count+=1
    if(r.status_code==200):
        print("True")
        return r
    else:
        print("False")
        return None


def get_followers_final(user_custom_url):
    with open('logging.txt','r') as f:
        num=f.readline()
    if num =='' or num is None or num=='\n':
        start_num=1;
    else:
        num=num[:-1]
        start_num=int(num)
        start_num=start_num*20
    r=is_user_custom_url_valid(user_custom_url)
    if(r!=None):
        map=get_target_data(r.text)
        end_num=int(map.get('followers'))
        get_followers(user_custom_url,start_num,end_num)
    else:
        return None

if __name__ == "__main__":

    user=''
    with open('users.txt','r') as f:
        user=f.readline()
        user=user[:-1]
        print(user)
    while not (user =='' or user is None or user=='\n'):
        user=user[:-1]
        Logging.info(user)
        with open('logging.txt','r') as f:
            num=f.readline()
            if num =='' or num is None or num=='\n':
                pass
            else:
                num=num[:-1]
                num=int(num)
                print(num==200000)
            if(num==200000):
                with open("users.txt",'r') as f:
                    a=f.readlines()
                    a=a[1:]
                with open('users.txt','w') as g:
                    g.writelines(a)
                with open('logging.txt','w') as f:
                    f.write('1\n')
        with open('users.txt','r') as f:
            user=f.readline()
            user=user[:-1]
        if not (user =='' or user is None or user=='\n'):
            get_followers_final(user)




    # login(account="xxxx@email.com", password="xxxxx")
    # login()
    # sss=get_followees("excited-vczh",200)
    # for i in sss:
    #     print(i)
    # print(is_user_exists("excited-vczh"))
    # push_target_data_to_db("https://www.zhihu.com/people/biubiubiuy2/followees")
    # followees_tmp=get_followees("excited-vczh",1564)
    # followees=[]
    # #去重
    # for i in followees_tmp:
    #     #若不存在
    #     if(is_user_exists(i)==0):
    #         followees.append(i)
    #     else:
    #         pass
    # base_url="https://www.zhihu.com/people/"
    #
    # with open("followees.txt","w") as f:
    #     for i in followees:
    #         f.write(i+"\n")
    # count=1;
    # for i in followees:
    #     url=base_url+i+"/followees"
    #     Logging.info("get_data: "+i)
    #     time.sleep(3)
    #     Logging.info("sleeping....")
    #     push_target_data_to_db(url)
    #     count+=1
    #     if(count%5==0):
    #         connection.commit()

    #获取文件中的用户的个人信息并存储到数据库中
    # followers=[]
    # base_url="https://www.zhihu.com/people/"
    #
    # with open("followers2.txt",'r') as f:
    #     s=f.read()
    # followees=s.split("\n")
    # count=1
    # for i in followees:
    #     if(is_user_exists(i)==0):
    #         url=base_url+i+"/followers"
    #         Logging.info("get_data: "+url)
    #         time.sleep(1)
    #         Logging.info("sleeping....")
    #         push_target_data_to_db(url)
    #         count+=1
    #         if(count%10 ==0):
    #             connection.commit()
    #     else:
    #         pass

    #存储某用户的所有关注者（赞同数超过10）到文件\
    # followers=get_followers("zhang-jia-wei",1,11000)

