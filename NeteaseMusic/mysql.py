#encoding=utf8
import pymysql


class MySQL:
    def __init__(self):
        info = {}

    @staticmethod
    def insert_sql(info):
        # 修改你的mysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='XGCxiagu0cha0515', db='NeteaseMusic')
        cur = conn.cursor()
        for key in info:
            cur.execute("REPLACE into song values(%s,%s,%s,%s)",
                        (key, info[key][0].encode('utf-8'), info[key][2], info[key][4]))
            cur.execute("REPLACE into author values(%s,%s)",
                        (info[key][2], info[key][1].encode('utf-8')))
            cur.execute("REPLACE into album values(%s,%s,%s,%s,%s,%s)",
                        (info[key][4], info[key][3].encode('utf-8'), info[key][5][3], info[key][2], '', ''))

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def insert_artist(info):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='XGCxiagu0cha0515', db='NeteaseMusic')
        cur = conn.cursor()
        for key in info:
            cur.execute("REPLACE into author values(%s,%s)",
                        (info[key][2], info[key][1].encode('utf-8')))

        conn.commit()
        cur.close()
        conn.close()
