#! python3
# flight_scraper.py

import sys
from lxml import html
import requests
import re
from bs4 import BeautifulSoup



# payload = {
#            'departure': 'BER',
#          'destination': 'MUC',
#         'outboundDate': 2017-12-11,
#           'returnDate': '',
#               'oneway': 1,
#     'openDateOverview': 0,
#           'adultCount': 1,
#           'childCount': 0,
#          'infantCount': 0
#           }

headers = {'Content-Type': 'application/x-www-form-urlencoded',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'Referer': 'https://www.flyniki.com/en/start.php'
           }

session = requests.Session()


response = session.get(url='http://www.flyniki.com/en/booking/flight/vacancy.php?',
                        #params=payload,
                        headers=headers
                       )

#print(response.text)
# '_ajax[requestParams][adultCount]'	'1'
# _ajax[requestParams][childCount]	'0'
# _ajax[requestParams][departure]	'Berlin - Tegel'
# _ajax[requestParams][destination]	'Paris - Charles de Gaulle'
# _ajax[requestParams][infantCount]	'0'
# _ajax[requestParams][oneway]	'on'
# _ajax[requestParams][openDateOverview]	
# _ajax[requestParams][outboundDate]	'2017-12-17'
# _ajax[requestParams][returnDate]	'2017-12-17'
# _ajax[requestParams][returnDeparture]''	
# _ajax[requestParams][returnDestination]	''
# _ajax[templates][]	'flightinfo'
# _ajax[templates][]	'infos'
# _ajax[templates][]	'priceoverview'
# _ajax[templates][]	'main'

page = session.post(response.url,
                    data= {
                     '_ajax[requestParams][adultCount]': '1',
                     '_ajax[requestParams][childCount]': '0',
                      '_ajax[requestParams][departure]':  'Berlin - Tegel',
                    '_ajax[requestParams][destination]': 'Paris - Charles de Gaulle',
                    '_ajax[requestParams][infantCount]':  '0',
                         '_ajax[requestParams][oneway]': 'on',
               '_ajax[requestParams][openDateOverview]': '',    
                   '_ajax[requestParams][outboundDate]': '2017-12-17',
                     '_ajax[requestParams][returnDate]': '2017-12-17',
                '_ajax[requestParams][returnDeparture]': '', 
              '_ajax[requestParams][returnDestination]': '',   
                                   '_ajax[templates][]': 'flightinfo',
                                   '_ajax[templates][]':'infos',
                                   '_ajax[templates][]':'priceoverview',
                                   '_ajax[templates][]':'main'
                            },
                    headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.48 Safari/537.36',
                        'Content-Type': 'application/x-www-form-urlencoded',
                             'Referer': response.url
                            }
                    )

print(page.status_code)
#print(page.text)

tree = html.fromstring(page.content, "html.parser") 
    
# grab each article //*[@id="priceLabelIdPREMFi_1"]//*[@id="price-59da83fa1ae59"] //*[@id="price-59da83fa1ae59"] //*[@id="price-59da83fa1ae59"] './/*[contains(@class, "author_name")]/text()')[0]
#test = tree.xpath('.//*[contains(@class, "lowest")]/text()')
#//div[@class = "div_res //*[@id="price-59da83fa1ae59"]
#//*[@id="flightDepartureFi_0"]
test = tree.xpath('//*[@id="flightDepartureFi_0"]/text()')
print(test)
# test = tree.xpath('//div[@class = "lowest"]')
# for item in test:

#     test2 = test.xpath('.//span[@id = "price-59da83fa1ae59"]/text()')   
#     print(len(test2))

# soup = BeautifulSoup(page.content, "html.parser")
# print(soup.title)

# # grabs each article //*[@id="priceLabelIdPREMFi_1"]/div[1]
# news_data = soup.find_all("label", {"id":"priceLabelIdPREMFi_1"}) #//*[@id="priceLabelIdPREMFi_1"]
# print(type(news_data))
# print(len(news_data))

# for item in news_data:
#     print(item.text)
    #print(item.find("div", {"class": "icon"}).text)
    
        # '''Author'''
        # try:
        #     print("Автор: {}".format(item.find("span", {"class": "s_author_name"}).text))
        # except AttributeError as e:
        #     print("Автор: Неизвестен")
    
        # '''Title'''
        # print("Название статьи: {}".format(item.find("h2", {"class": "h3 no_float"}).text))
    
        # '''Link'''
        # for link in item.h2.find_all('a'):
        #     print("Ссылка: {}".format(link.get('href')))
    
        # '''Summary'''
        # print(item.find("p", {"class": "intro"}).text)

