from douban.db_util import db_about
import os
from xml.dom.minidom import parse
import xml.dom.minidom


os.chdir("E:\\Coding\\douban_data\\sitemap_xml")

db=db_about()

for i in range(95,115):
    with open('E:\Coding\Spider\\douban\\douban\\sitemap\\text\\sitemap_to_db.txt','w') as f:
        f.write("------------------"+str(i)+"------------------------")
    print("------------------",i,"------------------------")
    with open('sitempa{}.xml'.format(i),'r') as f:
        xml_str=f.read()

    DOMTree = xml.dom.minidom.parseString(xml_str)
    collection = DOMTree.documentElement
    elements = collection.getElementsByTagName("url")
    for i in range(len(elements)):
        url=elements[i].getElementsByTagName("loc")[0].childNodes[0].nodeValue
        url_list=url.split('/')
        if(url_list[-3]=="subject"):
            map={'subject_class':-1,
                 'subject_url':url,
                 'subject_id':url_list[-2]}

        if(url_list[2]=='book.douban.com' and url_list[-3]=="subject"):
            map['subject_class'] = 'book'
        elif(url_list[2]=='movie.douban.com'and url_list[-3]=="subject"):
            map['subject_class'] = 'movie'
            movie_map = {'movie_id': url_list[-2]}
            movie_sql=db.format("insert ignore into `movie_name` ({}) values ({})",movie_map)
            db.commit_to_db_buffer(movie_sql)
        elif(url_list[2]=='music.douban.com'and url_list[-3]=="subject"):
            map['subject_class'] = 'music'
        else:
            print("not match: ",url)


        sql=db.format("insert ignore into `douban_sitemap` ({}) values ({})",map)
        db.commit_to_db_buffer(sql)

    db.commit()