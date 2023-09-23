# Introdução às Generator functions em Python
# generator = (n for n in range(10000))
# Generator são funções que sabem pausar
# Geradores (generators) são uma característica poderosa em Python que
# permitem a criação de sequências de valores de forma eficiente e lazy, ou
# seja, os valores são gerados sob demanda, economizando memória e melhorando
# o desempenho. Eles são definidos por funções que contêm pelo menos uma
# instrução yield.
#  A instrução yield é usada para retornar um valor da função e "pausá-la"
# temporariamente. Quando a função é chamada novamente, ela retoma a partir do
# ponto onde estava e continua a gerar valores.


# def generator(n=0):
#     yield 1 # Pausou
#     print('Continuando')
#     yield 2 # Pausou
#     print('mais uma vez')
#     yield 3 # Pausou
#     return 'Acabou'

# gen = generator(n=0)
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# for n in gen:
#     print(n)

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return


gen = generator()
for n in gen:
    print(n)


# def contador(maximo):
#     contador = 0
#     while contador < maximo:
#         yield contador
#         contador += 1

# meu_gerador = contador(maximo=6)

# for valor in meu_gerador:
#     print(valor)
