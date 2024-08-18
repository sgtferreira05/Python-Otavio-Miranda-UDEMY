'''import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
#p(lista)
        
lista = [
    (x, y) 
    for x in range(3)
    for y in range(3)
]   
p(lista) '''


#####################################################


'''def divisionFn (x, y):
    return x/y

def multiplicationFn(x, y):
    return x * y

def squareFn (x, y):
    return ( x ** y)




numbers = [1, 2, 3, 4, 5]
division = [divisionFn(numbers, 2) for numbers in numbers]
multiplication = [multiplicationFn(numbers, 2) for numbers in numbers]
square = [squareFn(numbers, 2) for numbers in numbers]


print(numbers)
print(division)
print(multiplication)
print(square)
'''
##############################################################

'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [numbers for numbers in numbers if numbers > 5]
odd_numbers = [numbers for numbers in numbers if numbers % 2 == 1]
even_numbers = [numbers for numbers in numbers if numbers % 2 == 0]
another_if = [
    numbers if numbers != 6 else 600 for numbers in even_numbers
    ]
print(f'Main list: ', numbers)
print(f'Even list: ', even_numbers)
print(f'Odd list: ', odd_numbers)
print(f'another list: ', another_if)'''

################################################################

'''rows_and_columns = [
    (x, y)
    if y != 2 else (x, y * 1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]

print(rows_and_columns)'''

################################################

'''string = 'Ailton Ferreira da Silva'
letters_numbers = 3
new_string = '-'.join([string[indice:indice + letters_numbers] for indice in range(0, len(string), letters_numbers)])
print(new_string)'''

#################################################################

'''names = ['Steverson', 'Ellen', 'Edna', 'Jenn', 'Ailton', 'Marcelo', 'Gabrielli', 'Yuri']
new_names = [ f'{name[:-1].lower()}{name[-1].upper()}' for name in names]
print(new_names)'''

####################################################################

numbers = [[number, number ** 2] for number in range(10)]
flat = [y for x in numbers for y in x]
print(numbers)
print(flat)