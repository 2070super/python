'''
7.新浪财金 美国股票 1月12日的 名称  代码 最新价    涨跌额    涨跌幅    振幅 昨收/今开盘 最高/最低价 成交量    市值(亿)  市盈率    行业板块   上市地
http://finance.sina.com.cn/stock/usstock/sector.shtml


'''

import requests
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup

import time


def getHtml(url):
    # 隐藏浏览器运行
    opt = ChromeOptions()
    opt.headless = True
    # 创建浏览器对象
    browser = webdriver.Chrome(options=opt)
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
    trs = soup.select("#data > table > tbody > tr")
    for tr in trs:

        tds = tr.select("td")
        ths = tr.select("th")

        code = tds[0].get_text()
        zxj = tds[1].get_text()
        zde = ths[0].get_text()
        zdf = ths[1].get_text()
        zf = ths[2].get_text()
        kpj = ths[3].get_text()
        zdj = tds[2].get_text()
        cjl = tds[3].get_text()
        sz = ths[4].get_text()
        syl = ths[5].get_text()
        bk = ths[6].get_text()
        ssd = tds[4].get_text()
        ssd2 = tds[5].get_text()

        info = {"code":code,"zxj":zxj,"zde":zde,"zdf":zdf,"zf":zf,"kpj":kpj,"zdj":zdj,"cjl":cjl,"sz":sz,"syl":syl,"bk":bk,"ssd":ssd,"ssd2":ssd2}
        print(info)
if __name__ == "__main__":
    url = "http://finance.sina.com.cn/stock/usstock/sector.shtml"
    htmlCode = getHtml(url)
    parseHtml(htmlCode)