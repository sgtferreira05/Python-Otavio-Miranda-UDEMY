import calendar
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(calendar.calendar(2024))
print(locale.getlocale())

