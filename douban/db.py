import pymysql

from douban.get_sitemap_xml import SiteMap



class db(object):
    """
    处理与数据库相关的操作
    """
    def __init__(self):
        self.__connection = pymysql.connect(user='root',
                                     passwd='123456',
                                     host='localhost',
                                     port=3306,
                                     db='zhihuanalysis',
                                     cursorclass=pymysql.cursors.DictCursor,
                                     )

        self.__connection.set_charset('utf8')
        self.__connection.cursor().execute('SET NAMES utf8;')
        self.__connection.cursor().execute('SET CHARACTER SET utf8;')
        self.__connection.cursor().execute('SET character_set_connection=utf8;')


    def commit_to_db(self,sql1):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(sql1)
        finally:
            pass

    def push_target_data_to_db(url, table_name):
        r = requests.get(url)
        if (r.status_code == 200):
            map = get_target_data(r.text)
            user_custom_url = url.split('/')[-2]
            map['user_custom_url'] = user_custom_url
            sql = build_insert_data_sql(map, table_name)
            commit_to_db(sql)

        else:
            Logging.info_important("this name is not valid: " + url)

    def build_insert_data_sql(map, table_name):
        list = []
        map_copy = copy.deepcopy(map)
        sql1 = "insert INTO " + '`' + table_name + '`' + '('
        for i in map_copy:
            sql1 += i + ","
            map_copy[i] = replace_punctuation(map_copy[i])
            list.append(map_copy[i])

        sql1 = sql1[0:-1] + ')'

        sql1 += """
        VALUES (
        """

        for i in list:
            if i is not None:
                if (i == "agree_num" or i == "thanks_num" or i == "followees" or i == "followers"):
                    sql1 += i + ','
                else:
                    sql1 += '\'' + i + "\',"
            else:
                sql1 += "null,"

        sql1 = sql1[0:-1] + ')'
        print(sql1)
        return sql1