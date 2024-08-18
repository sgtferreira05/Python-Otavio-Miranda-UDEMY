numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [numbers for numbers in numbers if numbers > 5]
odd_numbers = [numbers for numbers in numbers if numbers % 2 == 1]
even_numbers = [numbers for numbers in numbers if numbers % 2 == 0]
another_if = [
    numbers if numbers != 6 else 600 for numbers in even_numbers
    ]
print(f'Main list: ', numbers)
print(f'Even list: ', even_numbers)
print(f'Odd list: ', odd_numbers)
print(f'another list: ', another_if)