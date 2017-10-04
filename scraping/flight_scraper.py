#! python3
# flight_scraper.py

import sys
from lxml import html
import requests
import re


# "_ajax[requestParams][openDateOverview]": "",
# "_ajax[requestParams][departure]": 'TXL',
#  "_ajax[requestParams][childCount]": 0,

_ajax = {'requestParams': {'departure':'BER',
               'destination':'FRA',
              'outboundDate':'2017-12-11',
                'returnDate':'2017-12-11',
                    'oneway': 0,
          'openDateOverview': 0,
                'adultCount': 1,
                'childCount': 0,
               'infantCount': 0}}

print(_ajax['requestParams']['departure'])               

# payload = {
# 	  'departure':'BER',
#      'destination':'FRA',
#     'outboundDate':'2017-12-11',
#       'returnDate':'2017-12-11',
#            'oneway': 0,
#    'openDateOverview': 0,
#       'adultCount': 1,
#     'childCount': 0,
#      'infantCount': 0
#      }



# session = requests.Session()

# session.get("https://www.flyniki.com/")
# resp = session.post("http://www.flyniki.com/en/booking/flight/vacancy.php?", params=payload)
# print(resp.url)
#Sprint(resp.text)

# req_2 = session.get(resp.url, params=params)
# print(req_2.url)

# test = requests.get(resp.url, params={
# 	  'departure':'BER',
#      'destination':'FRA',
#     'outboundDate':'2017-12-11',
#       'returnDate':'2017-12-11',
#            'oneway': 0,
#    'openDateOverview': 0,
#       'adultCount': 1,
#     'childCount': 0,
#      'infantCount': 0
#      })
# print(resp.url)


# s = requests.Session()
# s.get('https://www.flyniki.com/cookies/set/sessioncookie/1507047956')
# r = s.get('https://www.flyniki.com/cookies')
# # print(r.url)


# # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
# #   'cookie':'id=2279ae9ae5060045||t=1458472344|et=730|cs=002213fd48bbbe24e42eb62b9d; IDE=AHWqTUltsd0TfQxbEcZA4T-c8i68uAvZLl4j7De3zr02hmMMDEWR72qILAwdAw41'}

# req = s.get(r.url, params={
# 	  'departure':'BER',
#      'destination':'FRA',
#     'outboundDate':'2017-12-11',
#       'returnDate':'2017-12-11',
#            'oneway': 0,
#    'openDateOverview': 0,
#       'adultCount': 1,
#     'childCount': 0,
#      'infantCount': 0
#      })

# print(req.url)

# resp = s.post(req.url, 
# 	data={
# 	  'departure':'BER',
#      'destination':'FRA',
#     'outboundDate':'2017-12-11',
#       'returnDate':'2017-12-11',
#            'oneway': 0,
#    'openDateOverview': 0,
#       'adultCount': 1,
#     'childCount': 0,
#      'infantCount': 0
#      })

# print(resp.status_code)
# print(resp.url)
