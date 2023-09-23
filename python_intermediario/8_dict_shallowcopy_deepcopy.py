# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

# copy - retorna uma cópia rasa (shallow copy)

# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'li': [0, 1, 2]
}

d2 = d1 # Ele não faz a cópia, d2 apenas aponta para o d1, ou seja, é possível mudar os objetos de d1 com o d2

d3 = copy.deepcopy(d1) # Copia profunda de d1, isso exclui os problemas que a copia rasa tem
d3 = d1.copy() # d1 foi copiado para d3, ambos se tornam independentes, porém, uma copia rasa e não copia os valores mutaveis, apenas os linka
d3['c1'] = 20 # é possível realizar as mudanças sem afetar os outros objetos
print(d3) # 