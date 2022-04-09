
'''
6.安居客 西安二手房信息
https://xa.anjuke.com/sale/?from=navigation
存csv

'''


import requests
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup

import time

def getHtml(url):
    # 隐藏浏览器运行
    opt = ChromeOptions()
    opt.headless = False
    # 创建浏览器对象
    browser = webdriver.Chrome(options=opt)
    # 用浏览器访问百度
    browser.get(url)
    # 隐式等待
    browser.implicitly_wait(10)
    time.sleep(5)
    # 获取加载后的页面html代码
    htmlCode = browser.page_source

    browser.close()

    return htmlCode


def parseHtml(htmlCode):

    soup = BeautifulSoup(htmlCode,'lxml')
    divs = soup.select("section.list-left > section.list > div.property")

    for div in divs:
        imgsrc = div.select("a > div.property-image > img")[0]["src"]

        title = div.select("a > div.property-content > div.property-content-detail > div.property-content-title > h3")[0].get_text().strip()
        content = div.select("a > div.property-content > div.property-content-detail > section")[0].get_text().strip()
        zy = div.select("a > div.property-content > div.property-content-detail > div.property-extra-wrap > div.property-extra")[0].get_text().strip()
        priceDiv = div.select("a > div.property-content > div.property-price > p")

        totalPrice = priceDiv[0].get_text()
        unitPrice = priceDiv[1].get_text()

        content = content.replace("\n","")

        print(title)
        print(imgsrc)
        print(content)
        print(zy)
        print(totalPrice)
        print(unitPrice)

        print("*"*100)

if __name__=="__main__":

    for i in range(1,51):
        url = f"https://xa.anjuke.com/sale/p{i}/?from=navigation"
        htmlCode = getHtml(url)
        parseHtml(htmlCode)

        time.sleep(2)