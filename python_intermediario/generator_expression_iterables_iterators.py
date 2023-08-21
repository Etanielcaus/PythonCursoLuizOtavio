# Generator expression, Iterables e Iterators em Python
# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iter(iterable) # tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) # Aqui ele abre um StopInteration, que é o erro que o for normalmente trata para terminar o loop

# print(dir(iterator))
# print(dir(iterable))

# for iterator in iterable:
#     print(iterator)

# ----------------------------------------------------------------
# Generator são funções que sabem pausar
# Geradores (generators) são uma característica poderosa em Python que permitem a criação de sequências de valores de forma eficiente e lazy, ou seja, os valores são gerados sob demanda, economizando memória e melhorando o desempenho. Eles são definidos por funções que contêm pelo menos uma instrução yield.
#  A instrução yield é usada para retornar um valor da função e "pausá-la" temporariamente. Quando a função é chamada novamente, ela retoma a partir do ponto onde estava e continua a gerar valores. 
# def contador(maximo):
#     contador = 0
#     while contador < maximo:
#         yield contador
#         contador += 1

# meu_gerador = contador(maximo=6)

# for valor in meu_gerador:
#     print(valor)
import sys

lista = [n for n in range(10000)] # Ele salva tudo na memória e entrega um valor por vez
generator = (n for n in range(10000)) # Ele não salva na memória, mas ele entrega o valor requerido

print(sys.getsizeof(lista)) # o tamanho do arquivo em lista
print(sys.getsizeof(generator)) # o tamanho do arquivo em generator

print(next(generator))
print(next(generator)) # Ele vai entregar o próximo valor, semelhante a um iterator

# for n in generator:
#     print(n)


























# import itertools

# iteravel1 = [1, 2, 3]
# iteravel2 = ['a', 'b', 'c']

# for item in itertools.chain(iteravel1, iteravel2):
#     print(item)

