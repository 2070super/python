
# 爬虫爬取 bilibili 科技频道

from selenium import webdriver
from bs4 import BeautifulSoup


def getHtml(url):
    # 打开浏览器
    browser = webdriver.Chrome()
    # 用浏览器访问百度
    browser.get(url)
    # 隐式等待
    browser.implicitly_wait(10)
    #获取加载后的页面html代码
    htmlCode = browser.page_source

    browser.close()
    return htmlCode


def parseHtml(htmlCode):

    soup = BeautifulSoup(htmlCode,'lxml')
    lis = soup.select("#videolist_box > div.vd-list-cnt > ul.vd-list > li")

    for li in lis:
        liobj = li.select("div.l-item > div.r > a")[0]

        infoUrl = "https:"+liobj["href"]
        title = liobj.get_text()

        print(title,infoUrl)

        v_desc = li.select("div.l-item > div.r > div.v-desc")[0].get_text()
        print(v_desc)

        print("-+"*50)



if __name__=="__main__":

    for i in range(1,7594):
        url = f"https://www.bilibili.com/v/tech/application/?spm_id_from=333.5.b_7375626e6176.3#/all/default/0/{i}/"
        htmlCode = getHtml(url)
        parseHtml(htmlCode)