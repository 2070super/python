
'''
2、爬取京东案例
'''

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
    time.sleep(2)

    browser.maximize_window()
    browser.find_element_by_id("J_bottomPage").click()

    time.sleep(2)
    # 获取加载后的页面html代码
    htmlCode = browser.page_source

    browser.close()

    return htmlCode


def parseHtml(htmlCode):

    soup = BeautifulSoup(htmlCode,'lxml')
    lis = soup.select("#J_goodsList >ul > li")

    for li in lis:

        #img = li.select("div.p-img > a > img")[0]["src"]
        price = li.select("div.p-price > strong > i")[0].get_text()

        #print(img)
        print(price)



if __name__=="__main__":

    url = "https://search.jd.com/Search?keyword=%E9%BC%A0%E6%A0%87&enc=utf-8&suggest=7.his.0.0&wq=&pvid=c4e2166a41b84573b4748bfdf42cccf3"
    htmlCode = getHtml(url)
    parseHtml(htmlCode)