#! python3
# flight_scraper.py

import sys
import requests
import re
from lxml import html
from itertools import product
from operator import itemgetter


valid_keyword = r"(\S)"
valid_date = re.compile(r'''
                  (2017|2018)  # the year
                          [-]  # separator
              (0[1-9]|1[012])  # the month
                          [-]  # separator
     (0[1-9]|[12][0-9]|3[01])  # the day
             ''', re.VERBOSE)


def get_flight_info(**kwargs):

    session = requests.Session()
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                    'Referer': 'https://www.flyniki.com/en/start.php'
              }

    get_req = session.get(url='http://www.flyniki.com/en/booking/flight/vacancy.php?',
                       headers=headers
                       )

    if re.match(valid_date, params["departure_date"]) and re.match(valid_date, params["return_date"]):
        return session.post(get_req.url,
                            data= {
                           '_ajax[requestParams][adultCount]': '1',
                           '_ajax[requestParams][childCount]': '0',
                            '_ajax[requestParams][departure]': params['departure'],
                          '_ajax[requestParams][destination]': params['destination'],
                          '_ajax[requestParams][infantCount]':  '0',
                               '_ajax[requestParams][oneway]': params['oneway'],
                     '_ajax[requestParams][openDateOverview]': '',    
                         '_ajax[requestParams][outboundDate]': params['departure_date'],
                           '_ajax[requestParams][returnDate]': params['return_date'],
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
                             'Referer': get_req.url
                                   }
                            )

    else:
        print("Sorry, you have typed wrong dates or didn't type them at all")
        sys.exit()
 

def oneway_flight(response, coin):
    #tree = html.fromstring(page.json()['templates']['main'], "html.parser")

    box = tree.xpath('//div[@class="lowest"]')
    flights = [title.xpath('./span/@title') for title in box]


    #currency = tree.xpath('//th[@id="flight-table-header-price-ECO_PREM"]/text()')[0]
    table_head = " FLIGHT      START/END     DURATION      CLASS        PRICE"
    
    print(table_head)
    i = 0
    for flight in flights[:10]:
        i += 1
        print(str(i)+')', *flight, currency)
        
        
def twoways_flight(response, coin):
    #tree = html.fromstring(page.json()['templates']['main'], "html.parser")
    #currency = tree.xpath('//th[@id="flight-table-header-price-ECO_PREM"]/text()')[0]
    #print(currency)

    outbound_tree = tree.xpath('//div[@class="outbound block"]//div[@class="lowest"]')
    outbound_flights = [title.xpath('./span/@title')[0] for title in outbound_tree]

    return_tree = tree.xpath('//div[@class="return block"]//div[@class="lowest"]')
    return_flights = [title.xpath('./span/@title')[0] for title in return_tree]

    combinations = [*product(outbound_flights, return_flights)]
    table_head = "    FLIGHT      START/END     DURATION     CLASS      PRICE     "

    print('The total count of outbound flights: {}'.format(len(outbound_flights)))
    print('The total count of return flights: {}'.format(len(return_flights)))
    print('The total count of flights combinations: {}\n'.format(len(combinations)))

    result = []
    for i in combinations[:10]:
        out_price = float(i[0].split()[-1])
        return_price = float(i[-1].split()[-1])
        #print("Out {}, return {}".format(out_price, return_price))
        total = out_price + return_price
        #print("total price:", round(total,2), currency)
        element = [i[0], currency, '   ', i[1], currency, '   Total price: ', round(total,2)]
        result.append(element)
    
    i=0
    print(table_head*2)
    for flight in sorted(result, key=itemgetter(-1)):
        i +=1
        print(str(i)+')', *flight, currency)




# the program's execution
params = {
               "departure": input("Введите IATA-код откуда летим: "),
             "destination": input("IATA-код куда летим: "),
             "oneway": input("Если желаете выполнить посик в одном направлении, введите 'on', иначе пропустите "),
          "departure_date": input("Дата вылета: гггг-мм-дд "),
             "return_date": input("Дата возврата: гггг-мм-дд  "),
                }


page = get_flight_info()

try:
    tree = html.fromstring(page.json()['templates']['main'], "html.parser")

except KeyError as e:
    print("\nЭто фиаско")

else:    
    currency = tree.xpath('//th[@id="flight-table-header-price-ECO_PREM"]/text()')[0]


try:
    twoways_flight(tree, currency)
    #oneway_flight(tree, currency)
except NameError as e:
    print(':(')
except lxml.etree.XMLSyntaxError as e:
    print('bad')    
        
  
