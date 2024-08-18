import json

# people = {
#     'name': 'Ailton',
#     'lastname': 'F',
#     'address0': [
#         {'street': 'R1', 'number': 32},
#         {'street': 'R2', 'number': 55},
#     ],
#     'height': 1.8,
#     'preferences_numbers': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nothing': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as file:
#     json.dump(people, 
#               file, 
#               ensure_ascii=False,
#               indent=2,)

with open('aula117.json', 'r', encoding='utf8') as file:
    people = json.load(file)
    print(people)
    print(people['name'])