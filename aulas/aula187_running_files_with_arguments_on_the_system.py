# sys.argv - Running files with arguments on the system
# Font = Fira Code 12

import sys

arguments = sys.argv
qtd_arguments = len(arguments)

if qtd_arguments <= 1:
    print('No arguments were passed.')
else:
    try:
        print(f'Arguments passed: {arguments[1:]}')
        print(f'First argument: {arguments[1]}')
        print(f'Second argument: {arguments[2]}')
    except IndexError:
        print('Not enough arguments passed.')