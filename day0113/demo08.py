
#爬取视频

from selenium import webdriver
from bs4 import BeautifulSoup

import time
import re
import requests

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


    # 获取加载后的页面html代码
    htmlCode = browser.page_source

    browser.close()

    return htmlCode


def parseHtml(htmlCode):

    soup = BeautifulSoup(htmlCode,'lxml')

    videoLink = soup.select("#drag_target1 video")[0]["src"]
    title = soup.select("h1.video-tt")[0].get_text()
    save(title,videoLink)


def save(title,videoLink):

    resp = requests.get(videoLink)

    with open("./videos/"+title+".mp4","wb") as file:
        file.write(resp.content)


if __name__=="__main__":

    url = "https://www.pearvideo.com/video_1749156"
    htmlCode = getHtml(url)
    parseHtml(htmlCode)