# coding = UTF-8
from src.RequestsFactory import *
from src.db.DatabaseHelper import *


class Category:
    '# 分类 获取信息'
    allDatas = ""
    __categoryInfo = ""
    categoryInfo = []
    categoryInfos = {}
    __db = None

    def __init__(self):
        requestFactory = RequestFactory()
        self.__db = DatabaseHelper()
        result = requestFactory.getInfo("http://www.meishij.net/list.php?sortby=update&lm=271&yl=688")
        # print(result)
        self.allDatas = result.select('.tabcon')

    def getCategory(self):
        categories = self.allDatas[1].select('a')
        if categories:
            self.__db.createTable()
            for category in categories:
                self.__categoryInfo = category.select('strong')[0].text  # 分类的详细信息
                self.__db.insert(self.__categoryInfo, category['href'], category.select('em')[0].text)
                self.categoryInfo.append(self.__categoryInfo)  # 保存数据
        self.categoryInfos["tag"] = self.categoryInfo
        return self.categoryInfos
