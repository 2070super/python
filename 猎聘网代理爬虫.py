from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
import requests
import MySQLdb

def getHtml(url,headers):
    response = requests.get(url, headers=headers)
    time.sleep(10)
    response.encoding = "UTF-8"
    return response.text

def saveData(ip,port):
    # 打开数据库
    db = MySQLdb.connect(host="localhost", user="root", passwd="live2018", database="test")
    cursor = db.cursor()

    # 添加
    sql = "insert into c values(%s,%s)"
    cursor.execute(sql, (ip, port))

    db.commit()
    db.close()


def parseHtml(html):
    soup = BeautifulSoup(html, "lxml")
    network = soup.select("#list > table > tbody > tr")
    print(len(network))
    for net in network:
        ip = net.select("td")[0].get_text()
        port = net.select("td")[1].get_text()
        saveData(ip,port)


if __name__ == "__main__":
    for i in range(1,4412):
        url = f"https://www.kuaidaili.com/free/inha/{i}/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        }
        html = getHtml(url,headers)
        parseHtml(html)
        time.sleep(3)

