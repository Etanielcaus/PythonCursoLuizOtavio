# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
copia_produtos = copy.deepcopy(produtos)
# print(copia_produtos)

for pessoas in copia_produtos:
    nomes = pessoas['nome']
    novo_preco = round(pessoas['preco'] * 1.10, 2)
    pessoas['preco'] = novo_preco # Errei aqui, faltou fazer a atualização do código

print(*copia_produtos, sep='\n')

    

# print(produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# numeros_ordenados = sorted([num * 2 for num in numeros], reverse=True)
copia_produtos_ex2 = copy.deepcopy(produtos)

# Ordenando produtos por nome em ordem decrescente usando list comprehension
produtos_ordenados_por_nome = sorted(copia_produtos_ex2, key=lambda x: x['nome'], reverse=True)
# O argumento key=lambda x: x['nome'] especifica que a ordenação deve ser feita com base nos valores da chave 'nome' de cada dicionário na lista.

# Exibindo a lista de produtos ordenada por nome decrescente
# for produto in produtos_ordenados_por_nome:
#     print(produto)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

copia_produtos_ex3 = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(copia_produtos_ex3, key=lambda x: x['preco'], reverse=True)

# for produto in produtos_ordenados_por_preco:
#     print(produto)

# ----------------------------------------------------------------
# Resolução do professor:
import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# FINAL

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')