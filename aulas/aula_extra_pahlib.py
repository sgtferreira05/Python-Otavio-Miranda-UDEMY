from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto) #caminho relativo
print(caminho_projeto.absolute()) #caminho completo *absoluto
print()

caminho_projeto = Path(__file__)
# print(caminho_projeto)
# print()
# print(caminho_projeto.parent)
# print()
# print(caminho_projeto.parent.parent)
# print()
# print(caminho_projeto.parent.parent.parent)

# essa barra gera um novo caminho
ideias = caminho_projeto.parent / 'ideias'
# print(ideias / 'arquivo.txt')

# a home
# print(Path.home())
# print(Path.home() / 'Desktop')


caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo.touch() #criar o arquivo
caminho_arquivo.write_text('Olá mundo!')
caminho_arquivo.unlink() #excluir o arquivo

# escrever no arquivo e ler
# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha \n')
#     file.write('Uma linha \n')
#     file.write('Uma linha \n')
#     file.write('Uma linha \n')
# print(caminho_arquivo.read_text())

# criar pasta e arquivos dentro das pastas
caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)
outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey!')



# apagar as pastas e os arquivos
# caminho_pasta.rmdir()
files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)
for i in range(10):
    file = files / f'file_{i}.txt'
    # file.touch()
    # if file.is_file()
    # if file.is_dir()
    if file.exists():
        file.unlink()
    else:
        file.touch()  
    with file.open('a+') as text_file:
        text_file.write('Olá, mundo! \n')
        text_file.write(f'file_{i}.txt')
# APAGAR PASTA E ARQUIVOS ***
# from shutil import rmtree
# rmtree(caminho_pasta)

def rmtree(root:Path, remove_root=True):
    for file in root.glob('*'):
        if file.isdir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()
print(caminho_pasta)