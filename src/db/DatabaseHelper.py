# coding = UTF-8
import pymysql

pymysql.install_as_MySQLdb()


class DatabaseHelper:
    'DatabaseHelper'
    __db = None
    __cursor = None

    def __init__(self):
        self.__db = pymysql.connect(host="localhost", user="root", passwd="123456a", db="TESTDB", use_unicode=True,
                                    charset="utf8")
        self.__cursor = self.__db.cursor()

    def createTable(self):
        self.__cursor.execute("DROP TABLE IF EXISTS TAG")
        sql = """CREATE TABLE TAG (
         TAG_NAME  VARCHAR(20) NOT NULL,
         TAG_CONTENT  VARCHAR(60),
         TAG_URL VARCHAR(60),
         TAG_NUM INT
         )"""
        self.__cursor.execute(sql)

    def insert(self, content, url, number):
        sql = "INSERT INTO TAG(TAG_NAME,TAG_CONTENT,TAG_URL,TAG_NUM) VALUES ('%s','%s','%s','%d')" % (
            'tag', content, url, int(number))
        self.__cursor.execute(sql)
        self.__db.commit()

        # 发生错误的时候回滚

    # self.__db.rollback()

    def select(self):
        '查询全表'
        sql = "select * from TAG"
        self.__cursor.execute(sql)
        results = self.__cursor.fetchall()
        # print(results)
        for result in results:
            TAG_NAME = result[0]
            TAG_CONTENT = result[1]
            TAG_URL = result[2]
            TAG_UNM = result[3]
            # print("TAG_NAME=%s,TAG_CONTENT=%s,TAG=%s,TAG_NUM=%d" % (TAG_NAME, TAG_CONTENT, TAG_URL, TAG_UNM))

        return results

    def appointSelect(self, sql):
        '''指定查询'''
        self.__cursor.execute(sql)
        results = self.__cursor.fetchone()
        return results
