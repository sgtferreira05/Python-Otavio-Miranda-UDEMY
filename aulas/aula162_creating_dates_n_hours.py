# Creating dates with datetime module
# datetime(year, month, day)
# datetime(year, month, day, hours, minutes, seconds)
# datetime.strptime('DATE', 'FORMAT')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# To timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# to install the pytz
# pip install pytz types-pytz

# from pytz import timezone
from datetime import datetime

# date_str_date = '2024/12/24 07:12:10'
# date_str_date = '24/12/2024'
# date_str_fmt = '%d/%m/%Y'


# # date = datetime(2024, 12, 24, 9, 12, 10)
# date = datetime.strptime(date_str_date, date_str_fmt)
# print(date)

# #####################################33

# date = datetime.now(timezone('Asia/Hong_Kong'))
# date = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Hong_Kong'))

########################################

date = datetime.now()
print(date.timestamp())
print(datetime.fromtimestamp(0841924506.34673))
