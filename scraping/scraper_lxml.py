#! python3
# scraper_lxml.py

import sys
from lxml import html
import requests
import re

valid_date = r"(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d"

    
def get_article_info(**kwargs):

    my_url = "https://www.gazeta.ru/search.shtml?p=search&page=0&text={text}&article=&section=&from={from}&to={to}&sort_order=published_desc&input=utf8"
   
    if re.match(valid_date, params["from"]) and re.match(valid_date, params["to"]):
        return requests.get(my_url, params=params) 
        
    else:
        print("Sorry, you have typed a wrong date")
        sys.exit()      


def parse_articles(requests):
    
    # html parsing
    tree = html.fromstring(my_req.content, "html.parser")
    
    # grab each article
    page = tree.xpath('//div[@class = "div_res"]')
  
    print("Входные параметры: ключевое слово - {text}, даты - {from} - {to}".format(**params))
    
    num = 0
    for item_lxml in page[:10]:
    
        num += 1
        
        """Date"""
        dates = item_lxml.xpath('.//time[@class = "date_time"]/text()')[0]
    
        """Author"""
        try:
            author = item_lxml.xpath('.//*[contains(@class, "author_name")]/text()')[0]
        except IndexError as e:
            author = "Неизвестен" 
        
        """Title"""
        title= item_lxml.xpath('.//h2[@class = "h3 no_float"]/a/text()')[0]       
        
        """Link"""
        link = item_lxml.xpath('.//h2[@class = "h3 no_float"]/a/@href')[0]
        
        """Summary"""
        summary = item_lxml.xpath('.//p[@class = "intro"]/a/text()')[0]

        print(num)
        print("Дата: {}".format(dates))
        print("Автор: {}".format(author))
        print("Название статьи: {}".format(title))
        print("Ссылка: {}".format(link))
        print(summary)
        print("-"*20)


# the program's execution
while True:

    params = {"text": input("Введите ключевое слово: "),
              "from": input("В период с дд.мм.гггг: "),
                "to": input("По дд.мм.гггг: ")}
  
    my_req = get_article_info() 
    parse_articles(my_req)
    
    # Ask an user does he want to continue the search?
    value = input("Вы хотите продолжить поиск? [y to continue]: ")
        
    if value == 'y':
        continue
    else:
        print('Have a nice day! Bye!')
        break     