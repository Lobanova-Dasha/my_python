# date_time.py - I'm learning how to work with Dates, 
# Times, Timedeltas, and Timezones
# Thanks a lot Corey Schafer for the great explanation
# https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g


import datetime
import pytz

d = datetime.date(2017, 8, 14)
print(d)
tday = datetime.date.today()
# print(tday)
# print(tday.isoweekday())
# print(tday.year())
# print(tday.weekday())

tdelta = datetime.timedelta(days=7)

# print(tday + tdelta)
# print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2018, 1, 17)
till_bday = bday - tday
# print(till_bday.total_seconds())


t = datetime.time(9, 30, 45, 100000)
# print(t.hour)

t = datetime.datetime(2017, 7, 25, 12, 30, 45, 10000)
# print(dt)
# print(dt.time())

tdelta = datetime.timedelta(days=12)

# print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# Using pytz

dt = datetime.datetime(2017, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
#print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
#print(dt_now)

# current utc zone
dt_utcnow = datetime.datetime.utcnow().replace(tz=pytz.UTC)
# print(dt_now)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

for tz in pytz.all_timezones:
 	print(tz)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

mtn_tz = pytz.timezone('US/Mountain')

dt_mth = mtn_tz.localize(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))

# print(dt_mtn)
# print(dt_east)
# print(dt_now)

# strftime - Datetime to String
# strtime - String to Datetime

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
# print(dt_mtn.strftime('%B %d, %Y'))

# dt_str = 'July 26, 2017'

# dt = datetime.datetime.strtime(dt_str, '%B %d, %Y')
# print(dt)
