# os.path works with paths in Windows, Linux and Mac
# os.path is a module that provides functions for working with file on Windows, Mac and Linux without having to worry about the differences between these systems.
# os.path Examples: 

#1. os.path.join: join strings into a single path. This way, os.path.join('pasta1', 'pasta2', 'arquivo.txt') it would return 'pasta1\pasta2\arquivo.txt' in Windows and 'pasta1/pasta2/arquivo.txt' in Mac and Linux.

#2. os.path.split: divides a file path into a tuple (directory, file)
#such as, os.path.split('/home/user/file.txt') would return ('/home/user', 'file.txt').

#3. os.path.exists: verify if a specific path exists.

# os.path only works with file paths and does not perform any input/output(I/O) operations on the files themselves.

# https://docs.python.org/3/library/os.path.html   doc

import os

path = os.path.join('\\home\\users', 'Desktop', 'curso', 'arquivo.txt')
print(path)

directory, file = os.path.split(path)
file_name, file_extension = os.path.splitext(file)
print(file_name, file_extension)

print(os.path.exists('D:\\CURSOS\\python_udemy'))
# print(os.path.abspath('.'))
print(os.path.basename(path))
print(os.path.basename(directory)) 
print(os.path.dirname(path)) 
# print(file)