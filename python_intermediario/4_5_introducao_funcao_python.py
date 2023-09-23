"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print(a, b, c):
#     print('Varias')
#     print('Varias')
#     print('Varias')
#     print('Varias')
#     print('Varias')

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

# def saudacao(nome='Sem nome'):
#     print(f'Olá, {nome}')

# saudacao('Luiz Otávio')
# saudacao('Etaniel')
# saudacao()

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)

multiplo_de(16, 8)