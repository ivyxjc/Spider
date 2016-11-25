import pymysql
import json
import matplotlib

import matplotlib.pyplot as plt

# connection = pymysql.connect(user='root',
#                                           passwd='123456',
#                                           host='localhost',
#                                           port=3306,
#                                           db='douban',
#                                           cursorclass=pymysql.cursors.SSCursor,
#                                           )
# connection.set_charset('utf8')
# connection.cursor().execute('SET NAMES utf8;')
# connection.cursor().execute('SET CHARACTER SET utf8;')
# connection.cursor().execute('SET character_set_connection=utf8;')
#
# cursor=connection.cursor()
# cursor.execute("SELECT celebrity_id,role,celebrity_name FROM douban.movie_celebrity;")
#
# list=[0 for i in range(0,200)]
#
# map={}
# for i in cursor:
#     if(i[1]==2):
#         if(i[0] in map.keys()):
#             map[i[0]]+=1
#         else:
#             map[i[0]]=1
#
# sortedList= sorted(map.items(), key=lambda d:d[1], reverse = True)
#
# flag=0
# for i in sortedList:
#     flag+=1
#     if(flag==20):
#         break
#     print(i[0])
#
# # for i in map:
# #     if(i==0):
# #         continue
# #     list[map[i]]+=1
# # print(list)
#
# with open("text//movie_celebrity.json",'w') as f:
#     json.dump(map,f)



Y0=[0, 7803, 2523, 1367, 842, 543, 378, 272, 243, 196, 147, 121, 109, 63, 70, 51, 56, 54, 34, 27, 28, 20, 21, 16, 15, 21, 10, 13, 8, 8, 3, 10, 6, 4, 6, 5, 5, 5, 2, 2, 2, 0, 3, 1, 2, 3, 1, 1, 2, 1, 1, 1, 2, 0, 0, 1, 0, 1, 1, 1, 3, 1, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Y1=[0, 9586, 2719, 1352, 760, 459, 355, 239, 176, 138, 106, 66, 66, 54, 30, 31, 32, 32, 14, 13, 13, 13, 15, 5, 5, 5, 6, 5, 5, 4, 4, 1, 2, 2, 2, 2, 1, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Y2=[0, 25259, 7760, 3910, 2453, 1701, 1246, 972, 686, 625, 460, 417, 382, 342, 261, 249, 196, 191, 179, 161, 125, 129, 109, 120, 92, 75, 78, 70, 86, 66, 56, 46, 48, 43, 54, 50, 49, 30, 32, 23, 28, 24, 23, 23, 24, 14, 10, 16, 13, 17, 9, 6, 8, 9, 8, 7, 10, 6, 3, 7, 2, 5, 9, 3, 0, 5, 2, 4, 4, 1, 2, 1, 2, 2, 3, 2, 2, 1, 3, 0, 1, 1, 0, 1, 3, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
X=[i for i in range(40,200)]
fig = plt.figure(figsize=(10,6),dpi=100)
plt.plot(X, Y0[40:200], color="blue",linestyle="-",lw=1.5,label=u"导演")
plt.plot(X, Y1[40:200], color="red",linestyle="-",lw=1.5,label=u"编剧")
plt.plot(X, Y2[40:200], color="black",linestyle="-",lw=1.5,label=u"演员")
plt.legend(loc='upper right')
plt.show()