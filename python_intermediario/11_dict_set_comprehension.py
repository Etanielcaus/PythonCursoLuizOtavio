# Dictionary Comprehension e Set Comprehension
# import pandas as pd
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
# Criar um DataFrame a partir do dicionário
# df = pd.DataFrame([produto])

# Imprimir o DataFrame
# print(df)

# for chave, valor in produto.items():
#     print(chave, valor)

dc = {
    chave: valor.upper() # deixar todos maiusculo, mas vai gerar um transtorno, ja que tem um float no meio do caminho
    if isinstance(valor,str) else valor # Ele vai checar se o valor é uma string, senão, ele vai apresentar da meneira que está
    for chave, valor in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave : valor
    for chave, valor in lista
}

print(dc)

s1 = {2 ** i for i in range(10)}
print(s1)

import numpy as np

# Criar um loop de 0 a 9 usando numpy
for valor in range(10):
    print(valor)
