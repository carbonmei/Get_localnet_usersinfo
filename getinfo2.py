import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'http://1.1.1.1'

headers = {'user-agent': 'Mozilla/5.0'}
reg = requests.get(url, headers=headers).text
# print(reg)
# print("\n-------------------------------------------------")
data = []
soup = BeautifulSoup(reg, 'html.parser')
netinfo = {
    'wlanuserip': soup.find(id="wlanuserip")['value'],
    'mac': soup.find(id="mac")['value'],
    'macc': soup.find(id="mac")['value'].replace(":", ""),
    'tip': soup.find(class_="succ-content").text.replace("\n", "")
}
userId = soup.find(id="userId")['value']
netinfo['userId'] = [userId]
# print(name)
url_netName = "http://1.1.1.1:8888/self/toChangePassword.do?accountId="+userId
print(url_netName)
regs = requests.get(url=url_netName, headers=headers).text
soup = BeautifulSoup(regs, 'html.parser')
netinfo['Name'] = soup.find(id="accountName")['value']
# print(soup.prettify())
data.append(netinfo)
# netdata = pd.DataFrame(data)
# netdata.to_excel("netinfo.xlsx")
print(data)

# print(soup.find(value=))
