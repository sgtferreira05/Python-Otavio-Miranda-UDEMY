# Context Manager with class;
# You can implement your own protocols just implementing the dunder methods that Python will use.
# This is called Duck Typing. A concept related to dynamic typing where Python isn't interested in the type, but if some methods exist on your object so that it works properly.
# When i see a bird that walks like a duck, swims like a duck and quacks like a duck, i call that bird a duck.
# To creat a context manager, the __enter__ and __exit__ methods must be implemented
# The __exit__ method will receive the exception class, the exception and traceback. If it returns True, exception in with will be supressed.

# Ex.:
# with open('aula149.txt', 'w') as arquivo
#   ...

# class MyContextManager:
#     def __init__(self):
#         print('INIT')

#     def __enter__(self):
#         print('ENTER')
#         return 123 #*
    
#     def __exit__(self, class_exception, exception_, traceback_):
#         print('EXIT')

# instance = MyContextManager()
# with instance as anything: #*
#     print('WITH', anything)

class MyOpen():

    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Opening file')
        self._file = open(self.file_path, self.mode, encoding ='utf8')
        return self._file
    
    def __exit__(self, classs_exception, exception_, traceback_):
        print('Closing file')
        self._file.close()


        # raise classs_exception('My message')
        # raise classs_exception(*exception_.args).with_traceback(traceback_)


        # print(classs_exception)
        # print(exception_)
        # print(traceback_)

        exception_.add_note('My note')

        # raise ConnectionError("Couldn't connect")

        # return True     # Tratei a exceção

with  MyOpen('aula149.txt', 'w') as file:
    file.write('Line 1 \n')
    file.write('Line 2 \n', 123)
    file.write('Line 3 \n')
    print('WITH', file)