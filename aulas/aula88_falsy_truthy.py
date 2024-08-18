# Truthy and Falsy values, Mutables and immutables types:

#MUTABLES: [] {} set()
#IMMUTABLES: () " "  0  0.0  None  False  range(0,10)

listt = [1]
dictionary = {1}
sett = set([1])
tuplee = ()
string = ''
int_number = 1
float_number = 0.0
nothing = None
false = False
interval = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{listt=}', falsy(listt))
print(f'{dictionary=}', falsy(dictionary))
print(f'{sett=}', falsy(sett))
print(f'{tuplee=}', falsy(tuplee))
print(f'{string=}', falsy(string))
print(f'{int_number=}', falsy(int_number))
print(f'{float_number=}', falsy(float_number))
print(f'{nothing=}', falsy(nothing))
print(f'{false=}', falsy(false))
print(f'{interval=}', falsy(interval))