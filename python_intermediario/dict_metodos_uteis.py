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

pessoa = {
    'nome': 'Luiz Otávio', # 'indice' : 'valor'
    'sobrenome': 'Miranda',
}

# print(len(pessoa)) # len - quantas chaves
# print(list(pessoa.keys())) # keys - iterável com as chaves
# print(list(pessoa.values())) # values - iterável com os valores
# print(list(pessoa.items())) # items - iterável com chaves e valores

# pessoa.setdefault('idade', None) # setdefault - adiciona valor se a chave não existe
# print(pessoa['idade'])
