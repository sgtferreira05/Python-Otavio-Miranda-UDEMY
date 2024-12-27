# datetime.timedelta and dateutil.relativetimedelta (calculating datas)

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
start_date = datetime.strptime('22/09/1972 10:35:20', fmt)
end_date = datetime.strptime('05/09/1996 10:35:15', fmt)

# increase days, weeks, hours... in a choose date
# delta = timedelta(days=10, hours=2)
# print(end_date + delta)



# Using relativedelta instead of a timedelta
print(end_date + relativedelta(seconds=60, minutes=2))
# Relatives betwen two dates
delta = relativedelta(end_date, start_date)
print(delta)
print(delta.years)
print(delta.days)
 




# We can verified the relatived betwen two or more dates
# print(end_date > start_date)
# print(end_date < start_date)
# print(end_date == start_date)

# That code returns us a timedelta
# print(end_date - start_date)
# delta = end_date - start_date
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
