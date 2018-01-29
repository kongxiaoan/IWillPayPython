# coding = UTF-8
from src.RequestsFactory import *
import re


class MenuInfo:
    '菜单的详细数据'

    __requests = None
    requestFactory = None
    __all_data = None

    def __init__(self):
        self.requestFactory = RequestFactory()

    def get_menu_info(self, url):
        self.__requests = self.requestFactory.getInfo('http://www.meishij.net' + url)
        self.__all_data = self.__requests.select('.listtyle1_w')
        print(self.__all_data[0].select('.big'))
        results = self.__all_data[0].select('.big')
        for result in results:
            title = result['title']
            conn = result['href']
            image = result.select('img')[0]['src']
            comments = result.select('.c1')[0].select('span')[0].text  # 评论和人气需要提取一下里面的数字
            author = result.select('.c1')[0].select('em')[0].text
            # print(comment)
            comment = comments.split("人气")[0].split("评论")[0]
            popularity = comments.split("人气")[0].split("评论")[1]
            # print(re.sub("\D","",comment))
