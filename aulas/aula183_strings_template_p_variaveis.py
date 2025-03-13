# string.Template to replace variables in texts
# Method:
# 1. substitute: replaces but generates erros if keys are missing; and
# 2. safe_substitute: replaces without erros.
# You can also change the delimiter and other things by creating a template subclass.

import json
import string
import locale
from datetime import datetime
from pathlib import Path
FILE_WAY = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')

def convert_to_brl(number: float | int ) -> str:
    brl = 'R$ ' + locale.currency(number, symbol=False, grouping=True)
    return brl

date = datetime(2022, 12, 28)
datas = dict(
    name= 'Yutung',
    value=convert_to_brl(1_234_567),
    date=date.strftime('%d/%m/%Y'),
    company='FAB',
    telephone='+55 (32) 99999-9999'
)

# print(json.dumps(datas, indent=2, ensure_ascii=False))

# text = '''
# Dear, ${name},


# -------------------
# We inform you that your monthly fee will be charged in the amount of $value on day ${date}. If you wish to cancel the service, please contact ${company} by the phone ${telephone}.

# Sincerely,

# ${company},
# '''
# template = string.Template(text)
# print(template.substitute(datas))
# # print(template.safe_substitute(datas)) Caso algum dado não tenha sido declarado



#-------------------
# with open(FILE_WAY, 'r') as file:
#     text = file.read()
#     template = string.Template(text)
#     print(template.substitute(datas))

#-----------------------

# Terá que mudar todos os $ por % lá no arquivo txt
class MyTemplate(string.Template):
    delimiter = '%'

with open(FILE_WAY, 'r') as file:
    text = file.read()
    template = MyTemplate(text)
    print(template.substitute(datas))
