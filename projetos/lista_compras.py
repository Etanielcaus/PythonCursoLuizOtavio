import os
listacompras = []



while True:
    seleciona_opcao = input('Selecione uma opção:\n[i]nserir: [a]pagar: [l]istar:')
    if seleciona_opcao == 'i':
        adicionar_item = input('valor: ')
        os.system('clear')
        listacompras.append(adicionar_item)
        for indice, compras in enumerate(listacompras):
            print(indice, compras)
    
    elif seleciona_opcao == 'a':
        try:
            remover_item = input('selecione o indice: ')
            listacompras.pop(int(remover_item))
            os.system('clear')
            for indice, compras in enumerate(listacompras):
                print(indice, compras)
        except ValueError as e:
            print('digite um número inteiro')
        except IndexError:
            print('Não existe na lista')
         
    elif seleciona_opcao == 'l':
        os.system('clear')
        for indice, compras in enumerate(listacompras):
            print(indice, compras)
    
    else:
        print('valor invalido')
    
