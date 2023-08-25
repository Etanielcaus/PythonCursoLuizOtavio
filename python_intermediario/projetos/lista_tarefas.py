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

lista = []
historico = []  # Histórico para armazenar ações

while True:
    comando = input('O que quer fazer? (tarefa) (listar) (refazer) (desfazer): ')

    if comando == 'tarefa':
        tarefa = input('Qual a tarefa? ')
        lista.append(tarefa)  # Adiciona a tarefa à lista
        historico.append(('adicionar', tarefa))  # Adiciona a ação ao histórico

    if comando == 'desfazer':
        if lista:
            lista.pop()  # Remove a última tarefa da lista se houver alguma
            print(lista)
        else:
            print('Lista vazia, não é possível desfazer.')
    
    if comando == 'refazer':
        if historico:
            acao, item = historico.pop()  # Recupera a última ação do histórico
            if acao == 'adicionar':
                lista.append(item)  # Adiciona novamente o item à lista
            elif acao == 'remover':
                lista.remove(item)  # Remove novamente o item da lista

    if comando == 'listar':
        print(lista)


