from selenium import webdriver
import time
import datetime

'''get the url of the aim'''
url = 'http://1.1.1.1'

browser = webdriver.Chrome('F:/chromedriver.exe')
browser.get(url)
time.sleep(10)

html_text = browser.page_source

time.sleep(5)

# get all elements that their css style contian class = 'extra-header-right'
elements = browser.find_elements_by_id("modifyPortal")
# get the aim
# element = elements[1]
browser.execute_script("modifyPortal.click()", elements)
# get the url of the aim
aimurl = browser.current_url

'''drop the scroll bar'''
js = "return action = document.body.scrollHeight"
height = browser.execute_script(js)

browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(5)

dates = browser.find_elements_by_xpath("//uni-view[@class = 'item item']/uni-view[@class = 'time']")

status = True

# Number
num = 0
# the position of starting index
n = 0

# judge the last date in one page is more than 5, or less than 5. former, flag = 1, else flag = 0
flag = 0

while status:
    for date in dates[n:]:
        num += 1
        if date.text[1] in ['小', '分', '秒', '天'] or date.text[2] in ['小', '分', '秒']:
            if date.text[1] == '天' and date.text[0] > '5':
                flag = 1
                break
        else:
            flag = 1
            break

    if flag == 0:
        new_height = browser.execute_script(js)
        if new_height > height:
            time.sleep(1)
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            # get the new page's height
            height = new_height
    else:
        print("已抓取完所需要的信息")
        status = False
        browser.execute_script('window.scrollTo(0, 0)')
        break

    time.sleep(3)
    n = num
    dates = browser.find_elements_by_xpath("//uni-view[@class = 'item item']/uni-view[@class = 'time']")

time.sleep(2)
html_text = browser.page_source
time.sleep(2)
names = browser.find_elements_by_xpath("//uni-view[@class = 'item item']/uni-view[@class = 'info']")
things = browser.find_elements_by_xpath("//uni-view[@class = 'item item']/uni-view[@class = 'title']")
prices = browser.find_elements_by_xpath("//uni-view[@class = 'item item']/uni-view[@class = 'price']")

'''save in excel'''
n = 0
datas = xlwt.Workbook()

sheet1 = datas.add_sheet(u'purchase', cell_overwrite_ok=True)

rowTitle = [u'用户名', u'商品', u'价格', u'购买时间']

for i in range(0, len(rowTitle)):
    sheet1.write(0, i, rowTitle[i])

for j in range(1, num):
    sheet1.write(j, 0, names[j - 1].text)
    sheet1.write(j, 1, things[j - 1].text)
    sheet1.write(j, 2, prices[j - 1].text)

'''cope with the time'''
z = 1
for date in dates[0:num - 1]:
    if date.text[2] in ['小', '分', '秒'] or date.text[1] in ['小', '分', '秒']:
        dt = datetime.datetime.now()
        if date.text[2] == '小':
            if dt.hour < int(date.text[0:2]):
                dt -= datetime.timedelta(days=1)
        elif date.text[1] == '小':
            if dt.hour < int(date.text[0]):
                dt -= datetime.timedelta(days=1)
        m = str(dt.month) + '月' + str(dt.day) + '日'
        sheet1.write(z, 3, m)
    elif date.text[1] == '天':
        tmp = int(date.text[0])
        datestart = datetime.datetime.now()
        datestart -= datetime.timedelta(days=tmp)
        n = str(datestart.month) + '月' + str(datestart.day) + '日'
        sheet1.write(z, 3, n)
    else:
        sheet1.write(z, 3, date.text)
    z += 1

datas.save('purchase.xls')