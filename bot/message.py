from bs4 import BeautifulSoup
import re as regex
# from selenium import webdriver
# from selenium.webdriver.common.by import By
import time
import requests
url = 'http://5850web.moneydj.com/z/zg/zgb/zgb0.djhtm?a=9200&b=9268&c=E&e=2022-6-13&f=2022-6-13'
re = requests.get(url)
# print(re.status_code)
bs = BeautifulSoup(re.text,'html.parser')
def temppp():
    tables=bs.find_all(id="oMainTable")[0] #先找到對應的table id出來 不然javascipt再傳送 可能會傳送多次導致結果過多 你可以將bs印出來看看 看你要的欄位在哪裡 由大範圍開始搜尋
    trtd=tables.find_all(class_="t0")[0] #這裡的0是 買超 欄位 如果設定1就是賣超
    for i in trtd:
        found=i.find('script')
        if (found==-1) or (found==None):
            pass
        else:
            xe=regex.findall("GenLink2stk(.*);",str(found))
            print(xe[0].replace("'","").replace("(","").replace(")","").split(","))
            #GenLink2stk('AS3491','昇達科');\