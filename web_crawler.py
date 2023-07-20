from bs4 import BeautifulSoup
import requests
import pprint


if __name__ == '__main__':
    # 1. "Get" google news 網站
    r = requests.get(
        "https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant")
    # 2. 取的回傳的DOM文字資料
    doc = r.text
    # 3. 把doc(DOM Tree)送給BeautifulSoup class, 做物件assign給soup這個變數
    soup = BeautifulSoup(doc, 'html.parser')
    # 4. 拿到國際新聞的頁面連結, 並取得內容
    elements_a = [
        element for element in soup.find_all('a')
        if element.get("href") and element.get("aria-label")
    ]
    international_news_href = ""
    for element in elements_a:
        if element.get("aria-label") == '國際':
            international_news_href = \
                'https://news.google.com' + element.get("href")[1:]
            break
    international_page_text = requests.get(international_news_href).text
    international_soup = BeautifulSoup(international_page_text, 'html.parser')

    # 5. 分塊拿到國際新聞: element tag=c-wiz, class=PO9Zff Ccj79 kUVvS
    internal_news_block = international_soup.find_all(
        'c-wiz', {'class': 'PO9Zff Ccj79 kUVvS'})

    # 6. 找到每個block內, 所有的新聞標題與超連結
    block_news = dict()
    for block_index, block in enumerate(internal_news_block):
        titles = list()
        for title_element in block.find_all('h4', {'class': 'gPFEn'}):
            titles.append(title_element.string)

        links = list()
        for link_element in block.find_all('a', {'class': 'WwrzSb'}):
            links.append('https://news.google.com' +
                         link_element.get("href")[1:])

        result = list(zip(titles, links))
        if result:
            block_news[block_index] = list(result)

    pprint.pprint(block_news[0])
    
        




