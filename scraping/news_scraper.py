#news_scraper.py

import requests
from bs4 import BeautifulSoup

my_req = requests.get("https://www.gazeta.ru/search.shtml?text=%EC%EE%F1%EA%E2%E0&p=search&how=pt")
soup = BeautifulSoup(my_req.content, "html.parser")
g_data = soup.find_all("div", {"class":"div_res"})


for item in g_data[:9]:
	    
    
    print("Дата: {}".format(item.find("time", {"class": "date_time"}).text))
    try:
        print("Автор: {}".format(item.find("span", {"class": "s_author_name"}).text))
    except AttributeError as e:
        print("Автор: Неизвестен")

    print("Дата: {}".format(item.find("time", {"class": "date_time"}).text))
    print("Название статьи: {}".format(item.find("h2", {"class": "h3 no_float"}).text))
    #print("Ссылка: {}".format(item.find({"a"})))
    print(item.find("p", {"class": "intro"}).text)