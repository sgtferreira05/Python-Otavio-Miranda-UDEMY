# Probema dos parâmetros mutávveis em funções Python


def add_customers(name, list=None):
    if list is None:
        list = []
    list.append(name)
    return list


customer1 = add_customers('Ailton')
add_customers('Andressa', customer1)
add_customers('Fernando', customer1)
customer1.append('Marie')

customer2 = add_customers('Maria')
add_customers('Helena', customer2)

customer3 = add_customers('Moreira')
add_customers('Vivi', customer3)

print(customer1)
print(customer2)
print(customer3)