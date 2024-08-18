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
        return None
    
    tarefa = tarefas.pop()
    print(f'{tarefa=}  foi removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    listar(tarefas)

    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        print()
        return None
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    listar(tarefas)
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        print()
        return None
    
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas.')
    listar(tarefas)
    print()




tarefas = []
tarefas_refazer = []

while True:
    print('comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()





    # if tarefa == "listar":
    #     listar(tarefas)
    #     continue
    # elif tarefa == "desfazer":
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
        
    # elif tarefa == "refazer":
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    
    # elif tarefa == "clear":
    #     os.system('cls')
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue
