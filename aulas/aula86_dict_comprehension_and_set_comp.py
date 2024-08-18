product = {
    'Name': 'Pen',
    'Price': 2.5,
    'Category': 'Officer',
}

'''for key, value in product.items():
    print(key, value)'''

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value
    in product.items()
    if key != 'Category'
}

listt = [
    ('a', 'value a'),
    ('b', 'value b'),
    ('c', 'value c'),
]

'''dc = {
    key: value
    for key, value in listt
}

print(dc)'''

s1 = {2 ** i for i in range(10)}
print(s1)