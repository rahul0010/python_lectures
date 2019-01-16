from datetime import *
today_date = datetime.now()
new_date = datetime(2015,4,20)
print(new_date.strftime('%d %B %Y'))
print(today_date.year)
print(today_date.day)
print(today_date.month)