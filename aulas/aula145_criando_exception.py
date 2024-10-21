# Creating Exceptions in Object-Oriented Python.
# To create an exception in Python, you just need to inherit from some exception in the language. The doc documentation is to inherit from exception.
# raising (raise) / throwing (throw) exceptions
# rethrowing exceptions
# adding notes to exceptions

class MyError(Exception):
    ...
class AnotherError(Exception):
    ...


def raising():
    exception_ = MyError('My error message', 'b', 'c')
    exception_.add_note('Error: Pay attention while typing.')
    raise exception_


try:
    raising()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = AnotherError("I'll throw the error again")
    exception_.add_note('Another observation:')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error