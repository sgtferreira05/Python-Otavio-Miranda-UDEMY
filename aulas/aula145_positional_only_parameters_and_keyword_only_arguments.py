# Controlando a quantidade de argumentos posicionais e nomeados em funções
# * args (ilimitado de argumentos posicionais)
#  **kwargs (ilimitado de argumentos nomeados)

# Positional-only Parameters (/) - Tudo antes da barra deve ser APENAS posicional.
# PEP 570 - Python Positional - Only Parameters
# https://peps.python.org/pep-0570/

# Keyword-Only Arguments (*) - * sozinho NÃO SUGA valores
# PEP 3102 - Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# def soma(a, b, /, x, y):
#     print(a + b + x + y)

# soma(7, 2, 3, y=4)

def soma(a, b, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)

soma(1, 2, c=3, nome='teste')