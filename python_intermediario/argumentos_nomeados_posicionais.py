"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definição
def soma(x, y):
    print(f'{x=} + {y=} é igual a {x + y}')

soma(1, 3) # momento em que chama a função ele ja á executa
soma(y=3, x=1)