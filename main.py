import os
caminho_arquivo = 'aula116.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0,0)
    print(arquivo.read())
    print('Reading...')
    arquivo.seek(0,0)
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print('Readlines...')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())


print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
    

# with open(caminho_arquivo, 'a+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )

# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)
os.rename(caminho_arquivo, 'aula116-2.txt')