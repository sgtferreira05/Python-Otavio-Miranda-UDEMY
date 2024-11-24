# Decorators classes


class Multiplication:
    def __init__(self, multiplicator):
        self._multiplicator = multiplicator

    def __call__(self, func):
        def internal(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._multiplicator
        return internal    

@Multiplication(3)
def _sum(x, y):
    return x + y

two_plus_two = _sum(2,2)
print(two_plus_two)