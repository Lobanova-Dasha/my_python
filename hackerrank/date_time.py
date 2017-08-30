# date_time.py

# Calendar Module
import calendar

day = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}

m,d,y = map(int, input().split())
print(day[calendar.weekday(y,m,d)])


# Time Delta
from datetime import datetime

for i in range(int(input())):
    t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(abs(int((t1-t2).total_seconds())))