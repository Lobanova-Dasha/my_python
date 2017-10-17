#! python3
# flight_scraper.py
"""nnnnnnnnnnnnnnnnnnnnnnnnnn"""

from datetime import date, datetime, timedelta
from itertools import product
from operator import itemgetter
from lxml import html
import requests


def check_date_format(input_date):
    """checks format of input_date"""
    try:
        datetime.strptime(input_date, '%Y-%m-%d') 
        return date(*map(int, input_date.split('-')))          
    except ValueError as err:
        print("Incorrect data format of the entered date: {}. Please, try again!".format(err))


def validate_dates(**kwargs):
    """nnnn"""
    today = date.today()
    one_year = today + timedelta(days=360) 
    if check_date_format(params['dep_date']):
        dep_date = check_date_format(params['dep_date'])
        if today <= dep_date <= one_year:
            if not params['return_date']:
                params['oneway'] = 'on'
                print("\nThe search will be executed in oneway direction\n")
                return True
            else:
                if check_date_format(params['return_date']):
                  return_date = check_date_format(params['return_date'])
                  if dep_date <= return_date <= one_year:
                      return True
                  else:
                      print("Return date must be between {} and {}. Please, try again!". format(str(dep_date), str(one_year)))                
        else:
            print("Depature date must be between {} and {}. Please, try again!". format(str(today), str(one_year)))


def validate_iata(dep_iata, dest_iata):
    """nnnn"""
    if dep_iata.isalpha() and dest_iata.isalpha():
        if len(dep_iata) == 3 and len(dest_iata) == 3:
            if dep_iata != dest_iata: 
                return True
            else:
                print('Departure IATA and destination IATA can not be the same')    
        else:
            print('Sorry, IATA code must contain definitely 3 letters.Please, try again!')          
    else:
        print('Sorry, IATA code must contain only letters. Please, try again!')
       

def build_request(**kwargs):
    """nnnn"""
    session = requests.Session()
    get_req = session.get(url='http://www.flyniki.com/en/booking/flight/vacancy.php?')
                       
    return session.post(get_req.url, 
                        data={'_ajax[requestParams][adultCount]': '1',
                              '_ajax[requestParams][childCount]': '0',
                              '_ajax[requestParams][departure]': params['dep_iata'],
                              '_ajax[requestParams][destination]': params['dest_iata'],
                              '_ajax[requestParams][infantCount]':  '0',
                              '_ajax[requestParams][oneway]': params['oneway'],
                              '_ajax[requestParams][openDateOverview]': '',    
                              '_ajax[requestParams][outboundDate]': params['dep_date'],
                              '_ajax[requestParams][returnDate]': params['return_date'],
                              '_ajax[requestParams][returnDeparture]': '', 
                              '_ajax[requestParams][returnDestination]': '',   
                              '_ajax[templates][]': 'flightinfo',
                              '_ajax[templates][]': 'infos',
                              '_ajax[templates][]': 'priceoverview',
                              '_ajax[templates][]': 'main'}) 
                                   
    
def build_tree_lxml(page):
    """nnnn"""
    try:
        tree = html.fromstring(page.json()['templates']['main'], "html.parser")
        currency = tree.xpath('//th[@id="flight-table-header-price-ECO_PREM"]/text()')[0]   
    except IndexError:
        print("No connections found for the entered data. Please, try again!")
    except KeyError:
        print("Sorry, probably entered iata code isn't available or doesn't exist. Please, try again!")
    else:        
        return tree, currency
    

def search_oneway_flights(tree):
    """nnnn"""
    outbound_tree = tree.xpath('//div[@class="outbound block"]//div[@class="lowest"]')
    outbound_flights = [title.xpath('./span/@title')[0] for title in outbound_tree]  
    
    if params['oneway']:
        for flight in enumerate(outbound_flights[:10], 1):
            print(*flight, currency)
    else:
        pass        
    return outbound_flights
           
        
def search_return_flights(tree):
    """nnnn"""
    outbound_flights = search_oneway_flights(tree_of_flights)
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
        total = round((out_price+return_price), 2)
        element = '{}, {}, {}, {} Total price: {}'.format(i[0], currency, i[1], currency, total)
        result.append(element)
    
    print(table_head*2)
    for flight in enumerate(sorted(result, key=itemgetter(-1)), 1):
        print(*flight, currency)


# the program's execution
if __name__ == '__main__':

    params = {"dep_iata": input("Enter the IATA code of the departure:").upper(),
              "dest_iata": input("Enter the IATA code of the destination:").upper(),
              "oneway": "",
              "dep_date": input("Enter the departure date YYYY-MM-DD:"),
              "return_date": input("Enter the return date YYYY-MM-DD [optional parameter]:")}
              

    if validate_iata(params["dep_iata"], params["dest_iata"]) and validate_dates():
        page = build_request()
        page.raise_for_status()
        
        if build_tree_lxml(page):
            tree_of_flights, currency = build_tree_lxml(page)
             
            if params['oneway']:
                search_oneway_flights(tree_of_flights)
            else:
                search_return_flights(tree_of_flights)



  
