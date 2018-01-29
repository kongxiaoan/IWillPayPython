# coding = UTF-8
import requests
from bs4 import BeautifulSoup


class RequestFactory:
    '请求'
    __baseUrl = ""

    def __init__(self):
        print("初始化")

    def getInfo(self, url):
        print(url)
        if url:
            res = requests.get(url)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text, 'html.parser')
            return soup
