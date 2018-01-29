# coding = UTF-8
import json
# 测试各种数据
from src.Category import *
from src.db.DatabaseHelper import *
from src.MenuInfo import *

category = Category()
db = DatabaseHelper()

category_info = category.getCategory()
# print(json.dumps(category_info, ensure_ascii=False))  # ensure_ascii=False 防止汉字被编译成其他格式
# db.createTable()
# print(str(json.dumps(category_info, ensure_ascii=False)))
# db.insert(json.dumps(category_info, ensure_ascii=False))
results = db.appointSelect("select * from TAG")
menuInfo = MenuInfo()
menuInfo.get_menu_info(results[2])
# for result in results:
#     # print(result[2])
#     menuInfo.get_menu_info(result[2])
