from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%84%A4%EC%95%84") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

i = 1
thumnails = soup.select('#imgList > div > a > img')
for thumnail in thumnails:
    img = thumnail['src']
    dload.save(img, f'imgs_homework/{i}.jpg')
    i += 1


driver.quit() # 끝나면 닫아주기

