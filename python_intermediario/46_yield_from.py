# Yield from
def gen1():
    yield 1
    yield 2
    yield 3
   
def gen3():
    yield 10
    yield 20
    yield 30
    yield 'acabou aqui'
    
def gen2(gen, otergen):
    yield from gen() # Ele vai fazer umam continuação a partir do gen1
    yield 4
    yield 5
    yield 6
    yield from otergen() # vai fazer outra continuacao
    
g = gen2(gen1, gen3)
for numero in g:
    print(numero)