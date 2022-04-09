
# 爬虫爬取 拉勾网

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

import time

def getHtml(url):
    # 打开浏览器
    browser = webdriver.Chrome()
    # 用浏览器访问百度
    browser.get(url)
    # 隐式等待
    browser.implicitly_wait(10)
    time.sleep(3)
    # 获取加载后的页面html代码
    htmlCode = browser.page_source

    browser.close()

    return htmlCode


def parseHtml(htmlCode):

    soup = BeautifulSoup(htmlCode,'lxml')
    divs = soup.select("div.list__YibNq > div.item__10RTO")

    for div in divs:

        tmp01 = div.select("div.item-top__1Z3Zo > div.position__21iOS > div.p-top__1F7CL")[0]
        title = tmp01.select("a")[0].get_text()
        fbtime = tmp01.select("span")[0].get_text()
        print(title,fbtime)



if __name__=="__main__":

    url = "https://www.lagou.com/wn/jobs?cl=false&fromSearch=true&labelWords=sug&suginput=python&city=%E8%A5%BF%E5%AE%89&kd=python"
    htmlCode = getHtml(url)
    parseHtml(htmlCode)