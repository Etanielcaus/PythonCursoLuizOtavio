"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número: ')

try:

    numero = int(numero)
    print('numero inteiro')
    if numero % 2 == 0:
        print('Seu número é par')
    else:
        print('Seu número é impar')
except ValueError as e:
    print('numero invalido')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# pergunta = input('Que horas são?: ')

# try:
#     pergunta = int(pergunta)
#     if 0 <= pergunta <= 11:
#         print(f'Bom dia {pergunta}')
#     elif 12 <= pergunta <= 17:
#         print(f'Boa tarde {pergunta}')
#     elif 18 <= pergunta <= 23:
#         print(f'Boa noite {pergunta}')
#     else:
#         print('Digite algo valido')
# except ValueError:
#     print('Digite algo valido')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# pergunta = input('Qual seu nome: ')

# try:
    
#     if len(pergunta) <= 4:
#         print('Seu nome é curto')
#     elif 5 <= len(pergunta) <= 6:
#         print('Seu nome é normal')
#     elif len(pergunta) >= 7:
#         print('Seu nome é muito grande')
#     else:
#         print("passa")
# except ValueError:
#     print('Pergunta errada')