import os

caminho_arquivo="C:\\python_udemy\\Nova pasta Atenção\\"

caminho_arquivo += 'aula116_criando_arquivos_com_python_context.txt'



with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write('ATENÇÃO \n')
    arquivo.write('Second Row \n')
    arquivo.writelines(
        ('Third Row\n', 'Fourth Row \n')
    )

# os.remove(caminho_arquivo)
# os.unlike(caminho_arquivo)
# os.rename(caminho_arquivo, 'aula116-2.txt')
