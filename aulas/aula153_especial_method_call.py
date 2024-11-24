# Especial method __call__
# callable is something that can be executed with parentheses.
# in regular classes, the __call__ instantiates a ''callable'' class.

class callMe():
    def __init__(self, phone):
        self.phone = phone
    def __call__(self, *args, **kwargs):
        print("You're calling", self.phone)

call1 = callMe('999299958')
call1()