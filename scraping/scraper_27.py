#scraper_flights.py
#! python2.7

import requests
from datetime import date, datetime, timedelta
from itertools import product
from operator import itemgetter
from lxml import html


def check_date_format(input_date):
    """checks format of input_date"""
    try:
        dep = datetime.strptime(input_date, '%Y-%m-%d')
        return dep.date()         
    except ValueError as err:
        print "Incorrect data format of the entered date: {}. Please, try again!".format(err)


def check_interval(input_date, min_date=date.today()):
    """nnnn"""
    one_year = date.today()+timedelta(days=360) 
    my_date = check_date_format(input_date)
    
    if my_date is not None:
        if min_date <= my_date <= one_year:    
            return True       
        else:
            print "Invalid date {}. Must be between {} and {}. Please, try again!". format(input_date, str(min_date), str(one_year))

def validate_dates(params):
    if check_interval(params['dep_date']):
        if not params['return_date']:
            params['oneway'] = 'on'
            print "\nThe search will be executed in oneway direction\n"
            return True
        elif check_interval(params['return_date'], min_date=check_date_format(params['dep_date'])):
            return True 


def validate_iata(params):
    """nnnn"""
    for iata in (params["dep_iata"], params["dest_iata"]):
        if not iata.isalpha() or len(iata) != 3:
            print "Invalid IATA {}. Try again!".format(iata)
            sys.exit()
    return True


def build_request(params):
    """nnnn"""
    with requests.Session() as session:
        get_req = session.get(url='http://www.flyniki.com/en/booking/flight/vacancy.php')
        get_req.raise_for_status()            
        page = session.post(get_req.url, 
                            data={
                              '_ajax[requestParams][adultCount]': '1',
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
                              '_ajax[templates][]': 'main'
                            })
        page.raise_for_status() 
        return page                            
                                   
    
def build_tree_lxml(page):
    """nnnn"""
    try:
        tree = html.fromstring(page.json()['templates']['main'], "html.parser")  
    except KeyError:
        print "Sorry, probably entered iata code isn't available or doesn't exist. Please, try again!"
    else:        
        return tree

def search_for_flights(tree):
    """nnnn"""
    try:
        currency = tree.xpath('//th[@id="flight-table-header-price-ECO_PREM"]/text()')[0]
    except (IndexError, AttributeError):
        print "No connections found for the entered data. Please, try again!"    

    if tree is not None:
        outbound_tree = tree.xpath('//div[@class="outbound block"]//div[@class="lowest"]')
        outbound_flights = [i.xpath('./span/@title')[0] for i in outbound_tree]
    else:
        sys.exit()    
       
    if params['oneway']:
        for flight in enumerate(outbound_flights[:10], 1):
            print flight, currency
    else:
        return_tree = tree.xpath('//div[@class="return block"]//div[@class="lowest"]')
        return_flights = [i.xpath('./span/@title')[0] for i in return_tree]
        combinations = product(outbound_flights, return_flights)
        
        print '\nThe total count of outbound flights: {}'.format(len(outbound_flights))
        print 'The total count of return flights: {}'.format(len(return_flights))
        print 'The total count of flights combinations: {}\n'.format(len(combinations))

        result = []
        for row in combinations[:10]:
            total_price = [float(j.split()[-1]) for j in row]
            element = '{}, {}, {}, {} Total price: {}'.format(row[0], currency, row[1], currency, sum(total_price))
            result.append(element)
    
        #print("  FLIGHT    START/END     DURATION     CLASS         PRICE     " * 2)
        for flight in enumerate(sorted(result, key=itemgetter(-1)), 1):
            print flight, currency
    

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
            tree_of_flights = build_tree_lxml(page_fly)
        except Exception:
            print "Sorry, no connections found for the entered data. Please, try again!"
        else:
            search_for_flights(tree_of_flights)