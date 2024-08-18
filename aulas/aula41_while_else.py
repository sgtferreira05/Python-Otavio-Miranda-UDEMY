''' While/else '''

string = "Valorqualquer"

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else: #Será executado se o while não encontrar nenhum break
    print('Não encontrei nenhum espaço na string.')
print('Fora do while.')

