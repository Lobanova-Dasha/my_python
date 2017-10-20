# scraper_flights.py
#! python2.7

import sys
import requests
from datetime import date, datetime, timedelta
from itertools import product
from operator import itemgetter
from lxml import html


class CustomError(Exception):
    sys.tracebacklimit = 0
    pass


def check_interval(input_date, min_date=date.today()):
    """
    Checks dates for the correct time interval:
    (min_date <= dep_date <= dest_date <= max_date)
    """
    max_date = date.today()+timedelta(days=360)
    if min_date <= input_date <= max_date:
        return True
    else:
        raise CustomError("{} must be between {} and {}".format(input_date, min_date, max_date))       
   

def validate_dates(params):
    """
    Returns True if both check_date_format(date) and check_interval(date) are True.
    If return_date is empty, request will be built in oneway searching.
    """
    check_date_format = lambda x: datetime.strptime(x, '%Y-%m-%d').date()
    max_date = date.today()+timedelta(days=360)

    try:
        dep_date = check_date_format(params['dep_date'])
        if check_interval(dep_date):
            if not params['return_date']:
                params['oneway'] = 'on'
                print "\nThe search will be executed in oneway direction\n"
                return True
            else:
                return_date = check_date_format(params['return_date'])
                if check_interval(return_date, min_date=dep_date):
                    return True
    except ValueError as err:
        raise CustomError('Sorry, {}. Please, try again!'.format(err))
       

def validate_iata(params):
    """Vaidates IATA codes: must contain only 3 letters """
    for iata in (params["dep_iata"], params["dest_iata"]):
        if not iata.isalpha() or len(iata) != 3:
            raise CustomError("Invalid IATA {}. Try again!".format(iata))            
    return True


def build_request(params):
    with requests.Session() as session:
        get_req = session.get(url='http://www.flyniki.com/en/booking/flight/vacancy.php')
        get_req.raise_for_status()          
        page = session.post(get_req.url, 
                            data={
                                '_ajax[requestParams][adultCount]': '1',
                                '_ajax[requestParams][childCount]': '0',
                                '_ajax[requestParams][departure]': params['dep_iata'],
                                '_ajax[requestParams][destination]': params['dest_iata'],
                                '_ajax[requestParams][infantCount]': '0',
                                '_ajax[requestParams][oneway]': params['oneway'],
                                '_ajax[requestParams][openDateOverview]': '',    
                                '_ajax[requestParams][outboundDate]': params['dep_date'],
                                '_ajax[requestParams][returnDate]': params['return_date'],
                                '_ajax[requestParams][returnDeparture]': '', 
                                '_ajax[requestParams][returnDestination]': '',   
                                '_ajax[templates][]': 'main'
                            })

        page.raise_for_status()
        return page                         
                                   

def search_for_flights(tree):
    """
    Outputs information about oneway flights (start/end, duration, class, price, currency).
    In the case of return flight, outputs all possible combinations with the total price
    """
    try:
        currency = tree.xpath('//th[@id="flight-table-header-price-ECO_PREM"]/text()')[0]
        outbound_tree = tree.xpath('//div[@class="outbound block"]//div[@class="lowest"]')
        outbound_flights = [i.xpath('./span/@title')[0] for i in outbound_tree]
    except (IndexError, AttributeError) as err:
        raise CustomError("Sorry, no connections found for the entered data. Please, try again!", err)       
  
    if params['oneway']:
        for flight in enumerate(outbound_flights[:10], 1):
            print flight[0], flight[-1], currency
    else:
        return_tree = tree.xpath('//div[@class="return block"]//div[@class="lowest"]')
        return_flights = [i.xpath('./span/@title')[0] for i in return_tree]
        combinations = list(product(outbound_flights, return_flights))
        
        result = []
        for row in combinations[:10]:
            total_price = [float(j.split()[-1]) for j in row]
            element = '{}, {}, {}, {} Total price: {}'.format(row[0], currency, row[1], currency, sum(total_price))
            result.append(element)

        print '\nThe total count of outbound flights: {}'.format(len(list(outbound_flights)))
        print 'The total count of return flights: {}'.format(len(list(return_flights)))
        print 'The total count of flights combinations: {}\n'.format(len(list(combinations)))
        
        print "  FLIGHT    START/END     DURATION     CLASS         PRICE     " * 2
        for flight in enumerate(sorted(result, key=itemgetter(-1)), 1):
            print flight[0], flight[-1], currency
    

# the program's execution
if __name__ == '__main__':

    params = {
        "dep_iata": raw_input("Enter the IATA code of the departure:").upper(),
        "dest_iata": raw_input("Enter the IATA code of the destination:").upper(),
        "oneway": "",
        "dep_date": raw_input("Enter the departure date YYYY-MM-DD:"), 
        "return_date": raw_input("Enter the return date YYYY-MM-DD [optional parameter]:")
    }
      

    if validate_iata(params) and validate_dates(params):
        page_fly = build_request(params)
        
        try:
            tree_of_flights = html.fromstring(page_fly.json()['templates']['main'], "html.parser")            
        except Exception as err:
            raise CustomError("Sorry, probably entered iata code isn't available or doesn't exist.Please, try again!", err)
        else:
            search_for_flights(tree_of_flights)