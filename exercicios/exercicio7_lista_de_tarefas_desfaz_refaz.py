#  Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café'] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo['fazer café', 'caminhar']
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        print()
        return
    
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        print()
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=}  foi removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        print()
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        print()
        return
    
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas.')
    print()




tarefas = []
tarefas_refazer = []

while True:
    print('comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
    if tarefa == "listar":
        listar(tarefas)
        continue
    elif tarefa == "desfazer":
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        
    elif tarefa == "refazer":
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    
    elif tarefa == "clear":
        os.system('cls')
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
