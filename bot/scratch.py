from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
import time
import requests
url = 'http://5850web.moneydj.com/z/zg/zgb/zgb0.djhtm?a=9200&b=9268&c=E&e=2022-6-10&f=2022-6-10'
headers = {'user-agent': 'Mozilla/5.0'}
re =requests.get(url,headers=headers)
temp =BeautifulSoup(re.text,'html.parser')
# for i in range(1,10):
index = temp.find_all('td',class_='t4t1',limit=10)
tempp = temp.find_all('td',class_='id')
print(temp)
print('====================================================')
for a in temp.find_all('a',href=True):
    print(a.text)

