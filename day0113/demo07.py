
'''
3、爬取梨视频案例

'''

from selenium import webdriver
from bs4 import BeautifulSoup

import time
import re

def getHtml(url):
    # 打开浏览器
    browser = webdriver.Chrome()
    # 用浏览器访问url
    browser.get(url)
    # 隐式等待
    browser.implicitly_wait(10)
    time.sleep(2)
    #最大化窗口
    browser.maximize_window()

    for i in range(10):
        btn = browser.find_element_by_id("listLoadMore")
        btn.click()
        time.sleep(1)


    # 获取加载后的页面html代码
    htmlCode = browser.page_source

    browser.close()

    return htmlCode


def parseHtml(htmlCode):

    soup = BeautifulSoup(htmlCode,'lxml')
    lis = soup.select("#categoryList > li")

    for li in lis:
        ta = li.select("div.vervideo-bd > a")[0]
        href = "https://www.pearvideo.com/"+ta["href"]
        imgStr = ta.select("div.vervideo-img>div.verimg-view>div.img")[0]["style"]
        vtime = ta.select("div.vervideo-img>div.cm-duration")[0].get_text()
        title = ta.select("div.vervideo-title")[0].get_text()

        res=re.search('background-image: url\((.*)\);',imgStr)
        imgSrc = res.group(1)
        print(title,href,imgSrc,vtime)


if __name__=="__main__":

    url = "https://www.pearvideo.com/category_130"
    htmlCode = getHtml(url)
    parseHtml(htmlCode)