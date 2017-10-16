#! python3
# flight_scraper.py

import sys
import requests
from lxml import html
from itertools import product
from operator import itemgetter
from datetime import date, datetime, timedelta


def validate_date(input_date):
    
    today = date.today()
    one_year = today + timedelta(days=360) 
  
    try:
        '''checks format of input_date'''
        datetime.strptime(input_date, '%Y-%m-%d') 
        print('good dep and dest format')

        date_format = date(*map(int, input_date.split('-')))
        
        if today<=date_format<=one_year:
            print('Valid dep')
            return True
        else:
            print('Not valid dep or dest: past time')
        
    except ValueError as e:
        print("Incorrect data format of departure_date or dest format: ", e)


def choose(**kwargs):
    if not params['return_date']:
        params['oneway']='on'
        print("You've choosen to search oneway")
        if validate_date(params['departure_date']):
            return True   
    
    else:

        print("You've choosen to search in two ways direction")
        if validate_date(params['departure_date']) and validate_date(params['return_date']):
            print('Sucsess')
            return True
        else:
            print('not valid, Try Again!')  


def validate_iata(**kwargs):
    if params['departure'].isalpha() and params['destination'].isalpha():
    
        if len(params['departure'])==3 and len(params['destination'])==3:
            return True
        else:
            print('Sorry, IATA code must contain definitely 3 letters.Try again!')
            return False    
    else:
        print('Sorry, IATA code must contain only letters. Try again!')
        return False 


def build_request(**kwargs):

    session = requests.Session()
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                    'Referer': 'https://www.flyniki.com/en/start.php'
              }

    get_req = session.get(url='http://www.flyniki.com/en/booking/flight/vacancy.php?',
                       headers=headers
                       )


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


def build_tree_lxml(page):
    try:
        tree = html.fromstring(page.json()['templates']['main'], "html.parser")
        currency = tree.xpath('//th[@id="flight-table-header-price-ECO_PREM"]/text()')[0]
    except IndexError as e:
        print(e)
    # except TypeError as e:
    #     print(e)    
    else:        
        return tree, currency
    

def oneway_flight(response, coin):

    outbound_tree = tree.xpath('//div[@class="outbound block"]//div[@class="lowest"]')
    outbound_flights = [title.xpath('./span/@title')[0] for title in outbound_tree]

    if params['oneway']:
        for flight in enumerate(outbound_flights[:10], 1):
            print(*flight, currency)
    else:
        pass        

    return outbound_flights
           
        
def twoways_flight(response, coin):

    outbound_flights = oneway_flight(tree, currency)

    return_tree = tree.xpath('//div[@class="return block"]//div[@class="lowest"]')
    return_flights = [title.xpath('./span/@title')[0] for title in return_tree]

    combinations = [*product(outbound_flights, return_flights)]
    table_head = "  FLIGHT    START/END    DURATION      CLASS         PRICE      "

    print('The total count of outbound flights: {}'.format(len(outbound_flights)))
    print('The total count of return flights: {}'.format(len(return_flights)))
    print('The total count of flights combinations: {}\n'.format(len(combinations)))

    result = []
    for i in combinations[:10]:
        out_price = float(i[0].split()[-1])
        return_price = float(i[-1].split()[-1])
        total = round((out_price + return_price),2)
     
        element = '{}, {}, {}, {} Total price: {}'.format(i[0], currency, i[1], currency, total)
        result.append(element)
    
    print(table_head*2)
    for flight in enumerate(sorted(result, key=itemgetter(-1)), 1):
        print(*flight, currency)


# the program's execution
if __name__ == '__main__':

    params = {
               "departure": input("Введите IATA-код откуда летим: ").upper(),
             "destination": input("IATA-код куда летим: ").upper(),
             "oneway": "",
          "departure_date": input("Дата вылета: гггг-мм-дд "),
             "return_date": input("Дата возврата: гггг-мм-дд  "),
                }

    if validate_iata() and choose():
    
        page = build_request()
        try:
            tree, currency = build_tree_lxml(page)
        except TypeError as e:
            print(e)     

        if params['oneway']:
            oneway_flight(tree, currency)
        else:
            twoways_flight(tree, currency)




  
