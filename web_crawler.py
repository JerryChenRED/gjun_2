from bs4 import BeautifulSoup
import requests

# 1. Get google news 網站
r = requests.get("https://news.gooogle.com/home?h1=zh-TW&ceid=TW:zh-Hant")
# 2. 取的回傳的DOM文字資料
doc = r.text
# 3. 把doc(DOM Tree)資料送給BeautifulSoup pythclass, 做物件assign給soup這個變數
soup = BeautifulSoup(doc, "html.parser")
# print(soup.prettify())
print(soup.title)
print(soup.title.text)
