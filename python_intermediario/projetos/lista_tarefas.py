# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json
import os
lista = []
historico = []  # Histórico para armazenar ações

while True:
    comando = input('O que quer fazer? (tarefa) (listar) (refazer) (desfazer): ')

    if comando == 'tarefa':
        tarefa = input('Qual a tarefa? ')
        lista.append(tarefa)  # Adiciona a tarefa à lista
        historico.append(('adicionar', tarefa))  # Adiciona a ação ao histórico
        os.system('clear')

    elif comando == 'desfazer':
        if lista:
            lista.pop()  # Remove a última tarefa da lista se houver alguma
            os.system('clear')
            print(lista)
        else:
            os.system('clear')
            print('Lista vazia, não é possível desfazer.')
            
    
    elif comando == 'refazer':
        if historico:
            acao, item = historico.pop()  # Recupera a última ação do histórico
            if acao == 'adicionar':
                lista.append(item)  # Adiciona novamente o item à lista
            elif acao == 'remover':
                lista.remove(item)  # Remove novamente o item da lista

    elif comando == 'listar':
        os.system('clear')
        for itens in lista:
            print( f'\t{itens}' )
    
    elif comando == 'sair':
        break
    
    else:
        os.system('clear')
        print('Comando invalido, tente novamente')
    
    with open('lista_tarefas.json', 'w') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)
        
        
# ----------------------------------------------------------------
# arquivo professor:
# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     if tarefa == 'listar':
#         listar(tarefas)
#         continue
#     elif tarefa == 'desfazer':
#         desfazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'refazer':
#         refazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'clear':
#         os.system('clear')
#         continue
#     else:
#         adicionar(tarefa, tarefas)
#         listar(tarefas)
#         continue

# ----------------------------------------------------------------
# Comandos em um dict:
# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()
#     listar(tarefas)


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)


# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     comandos = {
#         'listar': lambda: listar(tarefas),
#         'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#         'refazer': lambda: refazer(tarefas, tarefas_refazer),
#         'clear': lambda: os.system('clear'),
#         'adicionar': lambda: adicionar(tarefa, tarefas),
#     }
#     comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#         comandos['adicionar']
#     comando()