
# 爬虫爬取 猎聘网

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

def getHtml(url):

    resp = requests.get(url,headers=headers)
    return resp.text


def parseHtml(htmlCode):

    soup = BeautifulSoup(htmlCode,'lxml')
    lis = soup.select("div.left-list-box > ul > li")

    for li in lis:
        baseObj = li.select("div.job-detail-box > a  div.job-title-box")[0]
        title = baseObj.select("div.ellipsis-1")[0].get_text()
        address = baseObj.select("div.job-dq-box")[0].get_text()
        address = address.replace("\n","")
        salary = li.select("div.job-detail-box > a span.job-salary")[0].get_text()

        print(title,address,salary)


if __name__=="__main__":


    url = "https://www.liepin.com/zhaopin/?headId=9320b955ecb7bef28961932a070fb0bd&ckId=ey1y0hr7kpsn6woagg267ue5qzkiej3b&oldCkId=1107abf73ee39762b9e594a74015ccea&fkId=e47kmpgccgpzyfd957twg5myerayggh9&skId=60c16ee512299a19a5a5a6087b06353e&sfrom=search_job_pc&key=python%20%E7%88%AC%E8%99%AB&dq=270020&currentPage=0&scene=page"
    htmlCode = getHtml(url)
    parseHtml(htmlCode)
