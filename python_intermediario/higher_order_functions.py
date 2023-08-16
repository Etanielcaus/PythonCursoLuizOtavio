"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Bom dia', 'Luiz') # Ele executa a funcao executa, que tem como parametro a funcao e também msg que está dentro de saudacao, msg recebe a mensagem
print(v)

# saudacao_2 = saudacao
# v = saudacao_2('Bom dia') # Ele faz a mesma coisa, porém, somente passando de uma variavel para outra

# print(v)