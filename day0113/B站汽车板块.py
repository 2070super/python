
"""
爬取B站汽车板块的标题和url
https://www.bilibili.com/v/car/geek/?spm_id_from=333.6.b_7375626e6176.4#/all/default/0/
"""

import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions


#请求服务器器，获取html代码
def reqUrl(url):
    # 隐藏浏览器运行
    opt = ChromeOptions()
    opt.headless = True
    # 创建浏览器对象
    driver = webdriver.Chrome(options=opt)
    # 打开浏览器访问页面
    driver.get(url)
    # 最大化页面
    #driver.maximize_window()
    # 隐式等待
    driver.implicitly_wait(10)

    html = driver.page_source

    driver.close()

    return html


#解析html
def parseHtml(html):

    soup = BeautifulSoup(html, "lxml")

    lis = soup.select("ul.vd-list > li")
    for li in lis:

        a = li.select("div.r > a")[0]

        title = a.get_text()
        href = "https:"+a["href"]
        print(title,href)



#保存数据
def saveData(data):

    with open("proxy.csv", "a+",encoding="GBK") as file:
        file.write(data)


# 类似于java的main方法
if __name__=="__main__":

    for i in range(1,987):
        url = f"https://www.bilibili.com/v/car/geek/?spm_id_from=333.6.b_7375626e6176.4#/all/default/0/{i}/"
        html = reqUrl(url)
        parseHtml(html)

