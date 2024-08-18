# Try, excepct, else and finally

try:
    print('Abrir arquivo')
    8/0
    #open
except ZeroDivisionError as e: # except praticamente para tratar execeção
    print(e.__class__.__name__)
    print('Dividiu por zero')

else: # só sera executado se não houver nenhum erro
    print('Não houve erro')    

finally: # sempre será executado, mesmo se houver erros
    print('Fechar arquivo')
    #close