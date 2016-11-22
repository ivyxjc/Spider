import pymysql
import json

# connection = pymysql.connect(user='root',
#                              passwd='123456',
#                              host='localhost',
#                              port=3306,
#                              db='douban',
#                              cursorclass=pymysql.cursors.SSCursor,
#                              )
# connection.set_charset('utf8')
# connection.cursor().execute('SET NAMES utf8;')
# connection.cursor().execute('SET CHARACTER SET utf8;')
# connection.cursor().execute('SET character_set_connection=utf8;')
#
# cursor=connection.cursor()
# cursor.execute("SELECT `celebrity_id`,`role`,`celebrity_name` FROM douban.movie_celebrity;")
map={

}
# count=0
# for i in cursor:
#     if(i[1]==0):
#         if(i[0] in map.keys()):
#             map[i[0]]+=1
#         else:
#             map[i[0]]=0
#     count+=1
#
#
# with open("E:\\Coding\\Spider\\douban\\douban\\analysis\\text\\movie_celebrity.json", "w") as f:
#     json.dump(map, f)

# print(count)


with open("E:\\Coding\\Spider\\douban\\douban\\analysis\\text\\movie_celebrity.json", 'r') as f:
    map = json.load(f)

map= sorted(map.items(), key=lambda d:d[1], reverse = True)

flag=0
# for i in map:
#     print(i[1])
list=[0 for i in range(0,120)]
# print(list)
for i in map:
    try:
        list[i[1]]+=1
    except IndexError:
        print(i[1])

print(list)
