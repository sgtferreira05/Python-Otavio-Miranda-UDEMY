# Context Manager with function - Creating and Using context managers;

from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('Opening file')
        file = open(file_path, mode, encoding='utf8')
        yield file # funçao geradora
    except Exception as e:
        print('There was the error: ',e)
    finally:
        print('Closing file')
        file.close()

with my_open('class150.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n', 12)
    print('WITH', file)
