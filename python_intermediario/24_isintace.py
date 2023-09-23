# isinstace - para saber se objeto é de determinado tipo
# Em Python, a função isinstance() é usada para verificar se um objeto é uma instância de uma determinada classe ou tipo. Ela retorna True se o objeto for uma instância do tipo especificado, caso contrário, retorna False.
lista = ['a', 1, 1.1, True, [0, 1, 2], (1,2), {0, 1}, {'nome': 'Luiz'}, ]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        item.add(6)
        item.remove(5)
        print(item, isinstance(item, set)) # Ele vai checar o tipo de objeto
    
    elif isinstance(item, str):
        print(item.upper())
    
    elif isinstance(item, (int, float)):
        print(item, item * 2)
    
    else:
        print('outro')
        print(item)
    



# Exemplo de uso da função isinstance()
# numero = 10
# if isinstance(numero, int):
#     print("O objeto é um número inteiro.")
# else:
#     print("O objeto não é um número inteiro.")
