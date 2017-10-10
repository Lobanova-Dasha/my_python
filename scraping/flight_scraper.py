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
                   '_ajax[requestParams][outboundDate]': '2017-10-18',
                     '_ajax[requestParams][returnDate]': '2017-10-18',
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
print(tree)

for element in tree:
	# Selects all div elements no matter where they are in the document
	# that have an attribute named class with a value of "current"
    box = tree.xpath('//div[@class = "current"]')
    for i in box:
    	# Selects all the span elements that have an attribute named title
        
        #item = box.xpath('.//span[@title]/text()')
        item = box.xpath('.//span[@id = "price"]/title/text()')[1]
        print(item)



#//*[@id="priceLabelIdBASEFi_0"]
    #test = tree.xpath('//span[@title]/text()')[2]
    # test = box.xpath('.//@title')
    # print(test)
#     #time = tree.xpath('//span[@id="flightDurationFi_1"]/text()')[0]
#     #time = tree.xpath('//div[@class = "table-text-left"]')

#     #print(time)
#     print(test)

# data = tree.xpath('//div[@class="current"]')

# for item in data:
#     test = data.xpath('//@title')
#     print(test)


#//*[@id="flightDurationFi_1"]
# //*[@id="flighttables"]/div[1]/div[2]/table/tbody/tr[3]/td[4]

#soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
#tree = html.fromstring(page.content, "html.parser") 


# grab each article //*[@id="priceLabelIdPREMFi_1"]//*[@id="price-59da83fa1ae59"] //*[@id="price-59da83fa1ae59"] //*[@id="price-59da83fa1ae59"] './/*[contains(@class, "author_name")]/text()')[0]
#test = tree.xpath('.//*[contains(@class, "lowest")]/text()')
#//div[@class = "div_res //*[@id="price-59da83fa1ae59"]
#//*[@id="flightDepartureFi_0"] //*[@id="flighttables"]/div[1]/div[2]/table/tbody/tr[1]/td[2]
# test = tree.xpath('//*[@id="flightDepartureFi_0"]/text()')
# print(test)
# test = tree.xpath('//div[@class = "lowest"]')
# test = tree.xpath('//td[@class = "table-text-left"]')
#//*[@id="vacancy_flighttable"]
# test = tree.xpath('//div[@id = "vacancy_flighttable"]')

# print(len(test))
# for item in test:
#     time = test.xpath('.//span[@id = "flightDepartureFi_0"]/time/text()')[2]   
#     print(time)

# soup = BeautifulSoup(page.content, "html.parser")
# print(soup.title)

# # grabs each article //*[@id="priceLabelIdPREMFi_1"]/div[1]
# news_data = soup.find_all("label", {"id":"priceLabelIdPREMFi_1"}) #//*[@id="priceLabelIdPREMFi_1"]
# print(type(news_data))
# print(len(news_data))

