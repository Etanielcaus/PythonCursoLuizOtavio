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
    'nome': 'Luiz', # 'indice' : 'valor'
    'sobrenome': 'Miranda',
}

# print(len(pessoa)) # len - quantas chaves
# print(list(pessoa.keys())) # keys - iterável com as chaves
# print(list(pessoa.values())) # values - iterável com os valores
# print(list(pessoa.items())) # items - iterável com chaves e valores
# print(pessoa.get('nome', 'Não existe')) # get - obtém uma chave

# nome = pessoa.pop('sobrenome') # pop - Apaga um item com a chave especificada (del)
# print(nome)
# print(pessoa)

# ultima_chave = pessoa.popitem() # popitem - Apaga o último item adicionado
# print(ultima_chave)
# print(pessoa)

# pessoa.update({ # update - Atualiza um dicionário com outro
#     'nome': 'novo valor',
#     'idade': 30
# })
# pessoa.update(nome='novo valor', idade=30)
tupla = ('nome', 'novo valor'),
pessoa.update(tupla)
print(pessoa)

# pessoa.setdefault('idade', None) # setdefault - adiciona valor se a chave não existe
# print(pessoa['idade'])
