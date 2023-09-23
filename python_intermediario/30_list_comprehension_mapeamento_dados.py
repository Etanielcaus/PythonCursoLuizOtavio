# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    # produto['preco'] # exibe por item
    # {'nome': produto['nome'], 'preco': produto['preco'], 'novo': 10} # eu fiz o mapeamento e adicionei algo novo no produto
    # {**produto, 'preco': produto['preco'] * 1.05} # Ele desempacota os produtos, e também faz um aumento de 5% sobre o preco
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] >= 20 else {**produto} # faz o aumento somente se o preco for maior que 20
    for produto in produtos # Ele mostrou a mesma lista anteriormente
]

print(*novos_produtos, sep='\n') # ele vai exibir a lista com uma quebra de linha
# print(*produtos, sep='\n')