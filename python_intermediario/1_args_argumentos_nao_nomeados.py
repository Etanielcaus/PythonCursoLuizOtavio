"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        # print(f'Total: %d' % total)
        total += numero
        # print(numero)
    return total

soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6)

numeros = 100, 2, 3, 4, 5, 6
outra_soma = soma(*numeros) # empacota os numeros
print(outra_soma)

print(sum(numeros)) # como foi empacotado, é uma variavel que recebe a tupla, e por isso consegue fazer a soma

# print(sum((100, 2, 3, 4, 5, 6))) # ele faz a soma com uma tupla
print(*numeros) # Ele desempacotou a tupla

# Em Python, `args` é uma convenção para se referir a uma sequência (geralmente uma tupla) de argumentos posicionais em uma função. A palavra "args" é apenas uma abreviação para "arguments" (argumentos, em inglês). Isso é frequentemente usado quando você deseja criar uma função que pode aceitar um número variável de argumentos posicionais.

# Aqui está um exemplo simples de como usar `*args` em uma função:

# ```python
# def minha_funcao(*args):
#     for arg in args:
#         print(arg)

# minha_funcao(1, 2, 3, 4)
# ```

# Nesse exemplo, a função `minha_funcao` recebe uma quantidade variável de argumentos posicionais e os itera através de um loop `for`, imprimindo cada um deles.

# Quando você chama a função com argumentos (como `minha_funcao(1, 2, 3, 4)`), esses argumentos são empacotados em uma tupla e passados para a função como o parâmetro `args`. Isso permite que a função manipule uma quantidade variável de argumentos sem a necessidade de definir explicitamente cada um deles como parâmetros individuais.

# Lembre-se de que o nome `args` é uma convenção, não um requisito absoluto. Você pode usar qualquer nome que faça sentido para você, como `*argumentos` ou qualquer outro nome válido em Python que comece com um asterisco (*).