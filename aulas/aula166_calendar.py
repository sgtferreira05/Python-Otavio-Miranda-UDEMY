# Using calendar to calendars and dates;
# Calendar is used to genericals things of calendars and dates;
# Using calendar you can know things like:
# - Which the last day of a month;
# - Which the name and number of a determined date day (ex.: weekend);
# - Create a calendar (ex.: month calendar)
# - Working with a specifical calendar tool (calendar, month);
# By default, the week starts at 0 and ends at 6.(0= monday and 6 = sunday)

import calendar
# print(calendar.calendar(1996))
# print(calendar.month(1996, 9))

# first_day, last_day = calendar.monthrange(1996, 9)
# # print(calendar.monthrange(1996, 9))
# # print(calendar.month(1996, 9))
# print(calendar.day_name[first_day])
# print(calendar.day_name[calendar.weekday(1996, 9, last_day)])
print(calendar.weekday(1996, 9, 5))
print(calendar.day_name[calendar.weekday(1996, 9, 5)])
# ########

