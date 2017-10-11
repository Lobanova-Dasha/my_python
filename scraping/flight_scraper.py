#! python3
# flight_scraper.py

import sys
from lxml import html
import requests
import re
from bs4 import BeautifulSoup



headers = {'Content-Type': 'application/x-www-form-urlencoded',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'Referer': 'https://www.flyniki.com/en/start.php'
           }

session = requests.Session()


response = session.get(url='http://www.flyniki.com/en/booking/flight/vacancy.php?',
                       headers=headers
                       )

page = session.post(response.url,
                    data= {
                     '_ajax[requestParams][adultCount]': '1',
                     '_ajax[requestParams][childCount]': '0',
                      '_ajax[requestParams][departure]':  'TXL',
                    '_ajax[requestParams][destination]': 'MUC',
                    '_ajax[requestParams][infantCount]':  '0',
                         '_ajax[requestParams][oneway]': 'on',
               '_ajax[requestParams][openDateOverview]': '',    
                   '_ajax[requestParams][outboundDate]': '2017-10-27',
                     '_ajax[requestParams][returnDate]': '2017-10-27',
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

two_ways_page = session.post(response.url, data={
                      '_ajax[templates][]':'main',
                      '_ajax[templates][]': 'priceoverview',
                      '_ajax[templates][]': 'infos',
                      '_ajax[templates][]': 'flightinfo',
         '_ajax[requestParams][departure]':	'Berlin - Tegel',
       '_ajax[requestParams][destination]': 'Munich',
   '_ajax[requestParams][returnDeparture]': '',
 '_ajax[requestParams][returnDestination]':'',	
      '_ajax[requestParams][outboundDate]': '2017-10-27',
        '_ajax[requestParams][returnDate]':	'2017-10-27',
        '_ajax[requestParams][adultCount]':	'1',
        '_ajax[requestParams][childCount]':	'0',
       '_ajax[requestParams][infantCount]':	'0',
  '_ajax[requestParams][openDateOverview]':'',	
            '_ajax[requestParams][oneway]': ''
                                                },
                                           headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.48 Safari/537.36',
                        'Content-Type': 'application/x-www-form-urlencoded',
                             'Referer': response.url
                            }
                                                )	

print(two_ways_page.status_code)


tree = html.fromstring(two_ways_page.json()['templates']['main'], "html.parser")

#outbound_block = tree.xpath('//div[@class="outbound block"]')
box = tree.xpath('//div[@class="current"]')


for title in box:
    data = title.xpath('./span/@title')
    price = float(((((data[0]).split(","))[-1]).split())[-1])
    print(data[0])
    print(price)

