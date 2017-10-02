#! python3
# flight_scraper.py

import sys
from lxml import html
import requests
import re

# req = requests.get("https://www.flyniki.com/",
#                                      params={
#                      'random':'1506928452909',
#                                      'cv':'8',
#                         'fst':'1506927600000',
#                                     'num':'1',
#                                     'fmt':'3',
#                  'label':'8q6UCJXkaBDF1Iv9Aw',
#                                   'guid':'ON',
#                                  'u_h':'1080',
#                                  'u_w':'1920',
#                                 'u_ah':'1040',
#                                 'u_aw':'1920',
#                                   'u_cd':'24',
#                                   'u_his':'2',
#                                  'u_tz':'180',
#                              'u_java':'false',
#                                 'u_nplug':'4',
#                                 'u_nmime':'5',
# 'data':'flight_originid=BER;flight_destid=PAR;flight_startdate=2017-12-11;flight_pagetype=searchresults',
#                                       'frm':'0'
# })
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
req = requests.get("https://www.flyniki.com/ru/booking/flight/vacancy.php?", 
                                                                    params={
                                                            'currency':'RUB',
                                                        'totalprice':'15109',
                                                        'adultprice':'15109',
                                                           'departure':'TXL',
                                                         'destination':'CDG',
                                                 'outboundDate':'2017-12-11',
                                                   'returnDate':'2017-12-11',
                                                            'adultcount':'1',
                                                            'childcount':'0',
                                                           'infantcount':'0',
                                                               'market':'en',
                                                                  'lang':'en'
                                                                           },
                                                            headers=headers)


print(req.status_code)
print(req.url)