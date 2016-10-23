import pymysql.cursors



connection = pymysql.connect(user='root',
                       passwd='123456',
                       host='localhost',
                       port=3306,
                       db='zhihuanalysis',
                       cursorclass=pymysql.cursors.DictCursor
                       )


try:
    with connection.cursor() as cursor:
#         sql1="""
#         CREATE TABLE `zhihu` (
#     `user-custom-url` VARCHAR (255) NOT NULL,
#     `user-name` VARCHAR (255) NOT NULL ,
#     `agree_num` varchar(255)  NOT NULL,
#     `diagree_num` varchar(255)  NOT NULL,
#     PRIMARY KEY (`user-custom-url`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
#         """
        sql1="""
        select table_name from information_schema.tables where table_schema='zhihuanalysis' and table_type='base table';
        """
        res=cursor.execute(sql1)
        data = cursor.fetchall()
        connection.commit()
        table_names=[]
        for i in data:
            for key in i:
                table_names.append(i[key])
finally:
    pass



def build_insert_sql(table_name_list):
    sql1="insert into zhihu_temp "
    for i in table_name_list:
        sql1+="select * from zhihuanalysis."
        sql1+='`'+i+'`'+"\nunion\n"
    return sql1[:-7]




sql=build_insert_sql(table_names)
print(sql)

