# Crie uma classe decoradora chamada Validador que aceita uma função como argumento. Essa função deve realizar a validação de uma entrada e retornar True ou False. A classe decoradora deve usar o método __call__ para aplicar a validação à entrada fornecida como argumento e imprimir se a entrada é válida ou não

from typing import Any


class Validador:
    def __init__(self, entrada):
        self.entrada = entrada
    
    def __call__(self):
        enter = input('Digite 2: ')
        def validar():
            if enter == '2':
                print('True')
            else:
                print('False')
        return validar()


@Validador
def entrada():
    pass

entrada()

# entrada(enter)

# ----------------------------------------------------------------
class Validador:
    def __init__(self, funcao):
        self.funcao = funcao

    def __call__(self):
        enter = input('Digite 2: ')
        if enter == '2':
            print('True')
            self.funcao()  # Chama a função decorada após a validação
        else:
            print('False')

@Validador
def entrada():
    pass

entrada()
