#! python3
# flight_scraper.py

import sys
from lxml import html
import requests
import re




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
                         '_ajax[requestParams][oneway]': '',
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

# two_ways_page = session.post(response.url, 
# 	                         data={
                            
#                '_ajax[requestParams][departure]': 'TXL',
#              '_ajax[requestParams][destination]': 'MUC',
#          '_ajax[requestParams][returnDeparture]': '',
#        '_ajax[requestParams][returnDestination]': '',	
#             '_ajax[requestParams][outboundDate]': '2017-10-27',
#               '_ajax[requestParams][returnDate]': '2017-10-27',
#               '_ajax[requestParams][adultCount]': '1',
#               '_ajax[requestParams][childCount]': '0',
#              '_ajax[requestParams][infantCount]': '0',
#         '_ajax[requestParams][openDateOverview]': '',	
#                   '_ajax[requestParams][oneway]': '',
#                   # '_ajax[templates][]': 'priceoverview',
#                   # '_ajax[templates][]': 'main',
                   
#                   #           #'_ajax[templates][]': 'infos',
#                   #           #'_ajax[templates][]': 'flightinfo'
#                   '_ajax[templates][]': 'flightinfo',
#                                    '_ajax[templates][]':'infos',
#                                    '_ajax[templates][]':'priceoverview',
#                                    '_ajax[templates][]':'main'
#                                     },
#                                 headers={
#                                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.48 Safari/537.36',
#                               'Content-Type': 'application/x-www-form-urlencoded',
#                                     'Referer': response.url
#                                          }       
#                             )	
table_head = "FLIGHT    START/END   DURATION      CLASS          PRICE"
print(page.status_code)
#print(two_ways_page.json()['templates']['main'])
#print(two_ways_page.text)
# //*[@id="flighttables"]/div[1]/div[2]
# //*[@id="flighttables"]/div[1]
# tree = html.fromstring(page.json()['templates']['main'], "html.parser")
tree = html.fromstring(page.json()['templates']['main'], "html.parser")
currency = tree.xpath('//th[@id="flight-table-header-price-ECO_PREM"]/text()')[0]
#print(currency)

print("Outbound block".center(60, '='))
print(table_head)
box = tree.xpath('//div[@class="outbound block"]//div[@class="lowest"]') 
num = 0
for title in box:
    num += 1
    data = title.xpath('./span/@title')
    #price = float(((((data[0]).split(","))[-1]).split())[-1])
    print(data[0], currency)
    #print(price)
print('Total count of outbound flights:', num)    

print('')
print('Return block'.center(60, '='))
print(table_head)
return_box = tree.xpath('//div[@class="return block"]//div[@class="lowest"]')
num = 0
for title in return_box:
    num += 1
    data = title.xpath('./span/@title')
    #price = float(((((data[0]).split(","))[-1]).split())[-1])
    print(data[0], currency)
    #print(price)
print('Total count of return flights:', num)        

