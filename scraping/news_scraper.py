#! python3
# news_scraper.py

import sys
import requests
from bs4 import BeautifulSoup
import re


valid_date = r"(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d"

while True:

    keyword = input("Введите ключевое слово: ")
    from_date = input("В период с дд.мм.гггг: ")
    to_date = input("По дд.мм.гггг: ")

    # Validation of date. 
    if re.match(valid_date, from_date) and re.match(valid_date, to_date):
        
        # Create url with specific params
        my_url = "https://www.gazeta.ru/search.shtml?p=search&page=0&text={}&article=&section=&from={}&to={}&sort_order=published_desc&input=utf8".format(keyword, from_date, to_date)
    else:

    	# So, at that moment if you type wrong date, the program will interrupted
        print("Sorry, you have typed wrong date")
        sys.exit()
   
    # get request
    my_req = requests.get(my_url)

    # html parsing
    soup = BeautifulSoup(my_req.content, "html.parser")

    # grabs each article
    news_data = soup.find_all("div", {"class":"div_res"})

    # start of the execution
    print("Входные параметры: ключевое слово - {}, даты - {} - {}".format(keyword, from_date, to_date))

    for item in news_data[:9]:

        '''Date'''
        print("Дата: {}".format(item.find("time", {"class": "date_time"}).text))
    
        '''Author'''
        try:
            print("Автор: {}".format(item.find("span", {"class": "s_author_name"}).text))
        except AttributeError as e:
            print("Автор: Неизвестен")
    
        '''Title'''
        print("Название статьи: {}".format(item.find("h2", {"class": "h3 no_float"}).text))
    
        '''Link'''
        for link in item.h2.find_all('a'):
            print("Ссылка: {}".format(link.get('href')))
    
        '''Summary'''
        print(item.find("p", {"class": "intro"}).text)
    
        '''-'''
        print("-"*30)

        value = input("Вы хотите продолжить посик? [Y to continue]: ")
        
        if value == 'Y':
        	break
        else:
            print("Посик закончен")
            sys.exit()	
