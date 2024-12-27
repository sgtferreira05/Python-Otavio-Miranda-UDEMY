# Formatting dates from datetime
# datetime.trftime('DATE', 'FORMAT')

from datetime import datetime
fmt = '%d/%m/%Y'
# date = datetime(2022, 12, 13, 7, 59, 23)
date = datetime.strptime('1996-09-05 10:45:15', '%Y-%m-%d %H:%M:%S')
print(date.strftime('%d/%m/%Y'))
print(date.strftime('%d/%m/%Y %H:%M'))
print(date.strftime('%Y'))
print(date.strftime('%Y'), date.year) #String x Integer
print(date.strftime('%d'), date.day) #String x Integer
print(date.strftime('%m'), date.month) #String x Integer
print(date.strftime('%H'), date.hour) #String x Integer
print(date.strftime('%M'), date.minute) #String x Integer
print(date.strftime('%S'), date.second) #String x Integer


