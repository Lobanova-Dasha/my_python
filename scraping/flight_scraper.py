#! python3
# flight_scraper.py

import sys
from lxml import html
import requests
import re



payload = {
           'departure': 'BER',
         'destination': 'MUC',
        'outboundDate': 2017-12-11,
          'returnDate': '',
              'oneway': 1,
    'openDateOverview': 0,
          'adultCount': 1,
          'childCount': 0,
         'infantCount': 0
          }

headers = {'Content-Type': 'application/x-www-form-urlencoded',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'Referer': 'https://www.flyniki.com/en/start.php'
           }

session = requests.Session()


response = session.get(url='http://www.flyniki.com/en/booking/flight/vacancy.php?',
                        params=payload,
                        headers=headers
                       )

#print(response.text)

page = session.post(response.url,
                    data= {
                     '_ajax[requestParams][adultCount]': '1',
                     '_ajax[requestParams][childCount]': '0',
                      '_ajax[requestParams][departure]':  'Berlin',
                    '_ajax[requestParams][destination]': 'Munich',
                    '_ajax[requestParams][infantCount]':  '0',
                         '_ajax[requestParams][oneway]': 'on',
               '_ajax[requestParams][openDateOverview]': '',    
                   '_ajax[requestParams][outboundDate]': '2017-10-06',
                     '_ajax[requestParams][returnDate]': '2017-10-06',
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
print(page.text)
