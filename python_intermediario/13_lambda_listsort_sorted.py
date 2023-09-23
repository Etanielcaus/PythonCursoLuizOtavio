# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True) #ordenar a lista
# sorted(lista)

# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# # def ordena(item):
# #     return item['nome']


# def exibir(lista):
#     for item in lista:
#         print(item)

# l1 = sorted(lista, key=lambda item: item['nome']) # Esta função lambda faz a mesma coisa que a acão ordena
# l2 = sorted(lista, key=lambda item: item['nome']) # Esta função lambda faz a mesma coisa que a acão ordena

# exibir(l1)


# ----------------------------------------------------------------
# um pouco mais complexo para entendimento
def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_multiplicador(2)
duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(2))

print(executa(lambda x, y: x + y, 2, 3))

print(executa(lambda *args: sum(args), 1, 2, 3))
