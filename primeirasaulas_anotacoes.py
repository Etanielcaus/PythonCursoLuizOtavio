# \n -> LF quebra de linha
# print(12, 30, sep='-', end='##')
# print(12, 67, sep='-', end='\n')
# Escape: print("Luiz \"Otavio") aspas contraria \ significa que escape, se deseja incessir algo diferente na string
# Se eu quiser que o parametro de escape seja exibido: print(r"Luiz \"Otavio") utilizar o r antes da string

# ----------------------------------------------------------------
# Boolean é basicamente True ou False, para mudar o fluxo do interpretador
# ----------------------------------------------------------------
# Coerção de tipos - type convertion, typecasting, coercion
# print(int('1'), type(int('1'))) # Isso é a conversão de tipos, converteu um str em um int
# print(int('1') + 1) # str + int, porém, com '1' convertido
# print(bool('')) # Se vazio, retorna False, se com conteúdo True
# print(str(11) + 'b') # para apresentar 11b
# ----------------------------------------------------------------
# Variaveis - são usadas para salvar algo na memória do computador.
# PEP8: inicie variaveis com letras maiusculas, pode usar números e underline.
# nome_variavel = expressão
# nome_variavel = 'expressão'
# print(nome_variavel)

# nome = 'Luiz'
# idade = 30
# maior_de_idade = idade >= 18
# print('Nome:' , nome, 'idade:', idade)
# print('É maior?', maior_de_idade)
# ----------------------------------------------------------------
# Concatenação
# concatenacao = 'Luiz' + ' ' + 'Otavio' # Concatenação de Strings
# print(concatenacao)

# a_dez_vezes = 'A' * 10 # A multiplicação faz a repetição
# print(a_dez_vezes)
# tres_vezes_luiz = 3 * 'Luiz' # A multiplicação faz a repetição
# print(tres_vezes_luiz)
# ----------------------------------------------------------------
# F Strings
# f'{nome} tem {altura:,.2f} # O ,.2f significa a quantidade de casas decimais desejo aplicar, e a virgula é para modificar o ponto.
# ----------------------------------------------------------------
# Format / formatação de strings
# a = 'A'
# b = 'B'
# c = 1.1
# formato = 'a={0} b={1} b={1} c={2:.2f} c={2:.2f} c={2:.2f}'.format(a, b, c) # Ele passa os argumentos para o método, que aplica dentro da string, é possivel utilizar um indice.
# print(formato)
# ----------------------------------------------------------------
# Input - Coletar dados de usuarios
# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome=}')

# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro: ')

# int_numero_1 = int(numero_1)
# int_numero_2 = int(numero_2)

# print(f'A soma dos números é {int_numero_1 + int_numero_2}')
# ----------------------------------------------------------------
# If / elif      / else
# se / se não se / se não
# entrada = input('Você quer "entrar" ou "sair"? ')

# if entrada == 'entrar':
#     print('Você entrou')
# elif entrada == 'sair': # elif é para que você consiga dar outra opção
#     print('Você saiu do sistema')
# else:
#     print('Tente novamente')

# condicao = False

# if condicao:
#     print('Este é o código if')
# else:
#     print('O contrário do if') 
# print('Fora do if')
# ----------------------------------------------------------------
# Operadores relacionais
# Igualdade (==): Verifica se dois valores são iguais.
# Desigualdade (!=): Verifica se dois valores são diferentes.
# Maior que (>): Verifica se o valor da esquerda é maior do que o valor da direita.
# Menor que (<): Verifica se o valor da esquerda é menor do que o valor da direita.
# Maior ou igual (>=): Verifica se o valor da esquerda é maior ou igual ao valor da direita.
# Menor ou igual (<=): Verifica se o valor da esquerda é menor ou igual ao valor da direita.
# ----------------------------------------------------------------
# Operador lógico "and"
# Se qualquer valor for cosiderado falso, a expressão inteira será avaliada naquele valor
# print(True and True and True)
# print(True and False and True) #Ele vai parar no False

# entrada = input('Você quer "entrar" ou "sair"? ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# if entrada == 'entrar' and senha_digitada == senha_permitida:
#     print('Você entrou')
# else:
#     print('Tente novamente')
# ----------------------------------------------------------------
# Operador lógico "or"
# Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# print(False or False or False or 'abc' or 'True') # Ele vai parar no primeiro valor True

# entrada = input('Você quer "entrar" ou "sair"? ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# if entrada == 'entrar' or entrada == 'Entrar' and senha_digitada == senha_permitida:
#     print('Você entrou')
# else:
#     print('Tente novamente')
# ----------------------------------------------------------------
# Operador lógico "not"
# Utilizado para inverter expressões
# print(not True) # retorna False
# senha = input('Senha: ')

# if senha == '123456':
#     print('Entrou')
# else:
#     print('Sair')
# ----------------------------------------------------------------
# Operadores "in" e "not in"
# nome = 'Otavio'
# print('a' in nome) # True 'a' está em nome
# print('b' not in nome) # True 'b' não está em nome 

# nome = input('Nome: ')
# encontrar = input('Digite o que deseja encontrar: ')

# if encontrar in nome:
#     print(f'{encontrar} está em {nome}')
# else:
#     print(f'{encontrar} não está em {nome}')
# ----------------------------------------------------------------
# Interpolação de strings com %
# s - string
# d e i - int
# f - float
# x e x - Hexadecimal

# nome = 'Luiz'
# preco = 1000.95958
# variavel = '%s, o preco é foi R$%.2f' % (nome, preco) # %s e $f recebe os argumentos dentro dos ()
# print(variavel)
# ----------------------------------------------------------------
# Interpolação de strings com f-strings
# s - string
# d e i - int
# f - float
# x e x - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - esquerda
# < - direita
# ^ - centro
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a

# variavel = 'ABC'
# print(f'{variavel: >10}') # >10 vai dar 10 espaços para a esquerda
# ----------------------------------------------------------------
# Fatiamento e Len
# [index:f:passo]
# print(len('nome')) # contagem de caracteres
# ----------------------------------------------------------------
# Introdução ao "try" e "except" para capturar erros
# Tratamento de erros - Capturar erros

# numero_str = input('Vou dobrar o numero que digitar: ')

# try:
#     print('STR:', numero_str)
#     numero_float = float(numero_str)
#     print('FLOAT:', numero_float)
#     print(f'O dobro de {numero_str} é: {numero_float * 2}')
# except:
#     print('Isso não é um numero')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é: {numero_float * 2}')
# else:
#     print('Isso não é um numero')
# ----------------------------------------------------------------
# Variaveis, constantes e complexidade de código
# velocidade = 61 # velocidade atual do carro
# local_carro = 100 # local em que o carro está na estrada

# # Em letra maiúscula se refere a algo que não deve ser mudado no código, ou seja, uma constante
# RADAR_1 = 60 # velocidade máxima do radar 1
# LOCAL_1 = 100 # local onde o radar 1 está
# RADAR_RANGE = 1 # A distancia onde o radar pega

# velocidade_carro_passou_radar_1 = velocidade > RADAR_1
# carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

# if velocidade_carro_passou_radar_1:
#     print('Carro passou do radar 1')

# if carro_multado_radar_1 and velocidade_carro_passou_radar_1:
#    print('Carro multado em radar 1')
# ----------------------------------------------------------------
# ID - A identidade do valor que está na memória

# v1 = 'a'
# print(id(v1))

# ----------------------------------------------------------------
# Flag - Marcar um local
# None = Não valor
# is e is not = é ou não é (tipo, valor, identidade)
# id = identidade
# condicao = True

# if condicao:
#     print('Faça algo')
# else:
#     print('Não faça algo')
# ----------------------------------------------------------------
# Documentações, tipo builtin, tipo imutaveis, metodo de strings...
# https://docs.python.org/pt-br/3/library/stdtypes.html
# Imutaveis: str, int, float, bool
# string = 'Luiz Otavio'
# outra_variavel = f'{string[:3]}ABC{string[4:0]}' # A unica maneira de modificar uma string é fazendo o fatiamento dela
# print(outra_variavel)
# ----------------------------------------------------------------
# Extrutura de repetições "While"
# Executa uma ação enquanto uma condição for verdadeira
# condicao = True

# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f"Seu nome: {nome}")

#     if nome == 'sair':
#         break

# contador = 0

# while contador < 10:
#     contador = contador + 1 # Assim ele vai fazer com que o contador tenha um fim
#     print(contador)

# print('Acabou')
# ----------------------------------------------------------------
# Operadores de atribuição
# = += -= *= /= //= **= %=
# contador = 0

# contador += 1
# print(contador)
# ----------------------------------------------------------------
# While + continue
# contador = 0

# while contador < 100:
#     contador += 1 

#     if contador == 6:
#         print('Não vou mostrar o 6')
#         continue
    
#     if contador >= 10 and contador <= 27:
#         print('Não')
#         continue
    
#     print(contador)

#     if contador == 40:
#         break
    

# print('Acabou')
# ----------------------------------------------------------------
# While + While (Laços internos)
# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1
# while linha <= qtd_linhas:
#     coluna = 1


#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1 
    
#     linha += 1
# ----------------------------------------------------------------
# while / else
# string = 'valor qualquer'

# i = 0
# while i < len(string):
#     letra = string[i]

#     print(letra)
#     i += 1
# else:
#     print("O else foi executado.")

# texto = 'Python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i])
    
#     i += 1


# senha_salva = '12345'
# senha_digitada = ''
# repeticoes = 3

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x):  ')
#     repeticoes += 1

# print('Aquele laço acima pode ter repetições infinitas')
# ----------------------------------------------------------------
# Introdução ao for / in - estruturas de repetição para coisas finitas
# texto = 'Python'

# novo_texto = ''
# for letra in texto:
#     novo_texto += f'*{letra}'
#     print(letra)
# print(novo_texto)
# ----------------------------------------------------------------
# For + Range
# Range -> range(start, stop, step)
# início: é o número inicial da sequência (inclusive).
# fim: é o número final da sequência (exclusivo). A sequência irá até esse valor, mas não o incluirá nos resultados.
# passo: é o valor que determina o incremento entre os números na sequência. Por padrão, o valor do passo é 1.

# numeros = range(10)
# numeros = range(5, 10)
# numeros = range(2, 10, 1)
# print(numeros)

# for numero in numeros:
#     print(numero)
# ----------------------------------------------------------------
# Como funciona por baixo dos panos?
# Iterável -> str, range, etc
# Iterador -> quem sabe entrar um valor por vez
# Next -> me entregue o próximo valor
# Iter -> me entregue seu iterador

# exto = iter('Luiz') # __iter__()
# print(next(texto))# __next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))

# iterador = iter(texto) # iterator

# while True:
#     try:
#         letra = next(iterador) 
#         print(letra)
#     except StopIteration:
#         break


# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)
# ----------------------------------------------------------------
# O que é feito com while, pode ser feito com for também

# for i in range(10):
#     if i == 2:
#         print('i é 2, pulando...')
#         continue
    
#     if i == 8:
#         print('i é 8, seu else não executará')

#     for j in range(1, 3):
#         print(i, j)

# else:
#     print('For completo com sucesso')
# ----------------------------------------------------------------
# Tipo List - Introdução as listas mutáveis
# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +

# lista = [123, True, 'Luiz Otávio', 1.2, []]
# lista[2] = 'Maria' # Aqui ele altera o valor na lista
# print(lista)
# print(lista[2]) # Acessar o indice da lista
# ----------------------------------------------------------------
# Modificando itens da lista utilizando um index
# lista = [10, 20, 30, 40]
# numero = lista[2]
# lista[2] = 300 # modificar item na lista
# del lista[2] # deletar item na lista
# lista.append(50) # adicionar item ao final da lista
# lista.pop() # remover o ultimo valor na lista
# lista.pop(0) # remover por indice
# lista.clear() # clear lista
# lista.insert(0, 'etaniel') # adiciona um item no indice (indice, item)
# print(lista)

# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b # concatenação de uma lista
# lista_a.extend(lista_c) # ele não retorna valor, ele somente meche na primeira lista extendendo ela
# print(lista_a)
# ----------------------------------------------------------------
# Cuidados com dados mutáveis
# = - copiado valor(imutáveis)
# = - aponta para o mesmo valor na memória (mutável)

# nome = 'Luiz'
# noutra_variavel = nome # guardar o valor antes de modifica-lo
# nome = 'João'
# print(nome)
# print(noutra_variavel)

# lista_a = ['Luiz', 'Maria']
# lista_b = lista_a # Ele aponta para a lista a, ou seja, se modificar a lista a, vai influenciar na lista b
# lista_b = lista_a.copy() # com o metodo copy() ele copia a lista inteiramente

# lista_a[0] = 'Qualquer coisa'
# print(lista_b) # Ele modifica o valor da lista b também
# ----------------------------------------------------------------
# for in com listas
# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')
# i = range(len(lista))
# for i in i:
#     print(i, lista[i], type(lista[i]))
# ----------------------------------------------------------------
# Introdução ao empacotamento e desempacotamento
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# print(nome1, nome2, nome3)
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, *resto = nomes # Ele vai empacotar o restante da lista em que não havia variaveis suficientes
# print(nome1, resto)
# ----------------------------------------------------------------
# Tipo Tupla - Uma lista imutável
# nomes = ('Maria', 'Helena', 'Luiz')
# converterlista = ['Maria', 'Helena', 'Luiz']
# converterlista.append('outro')
# listaconvertida = tuple(converterlista) # Converter uma lista em uma tupla

# print(converterlista)
# print(listaconvertida)
# print(nomes)
# ----------------------------------------------------------------
# enumerate - enumera iteráveis (índices)
# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada) 

# for indice, nome in enumerate(lista):
#     print(indice, nome)
# -----------------------------------------------------------------
# Imprecisão de ponto flutuante
# import decimal
# numero_1 = decimal.Decimal('0.1')
# numero_2 = decimal.Decimal('0.7')
# numero_3 = numero_1 + numero_2
# # print(numero_3) # 0.799999999999999
# # Maneiras de contornar esse problema:
# print(f'{numero_3:.2f}') # 0.80
# print(round(numero_3, 1)) # arredondar as casas decimais
# decimal.Decimal faz a conta corretamente
# ----------------------------------------------------------------
# split e join com list e str
# plit - divide uma string
# join - une uma string
# frase = 'Olha só que,   coisa interessante'
# lista_frases_cruas = frase.split(',') # dentro dos () se passa o argumento para fazer a divisão

# lista_frases = []
# for i, frase in enumerate(lista_frases_cruas):
#     lista_frases.append(lista_frases_cruas[i].strip()) # strip corta os espaços. 

# print(lista_frases_cruas)
# print(lista_frases) #
# frases_unidas = ', '.join(lista_frases)
# print(frases_unidas) 
# ----------------------------------------------------------------
# Lista de listas e seus indices
# salas = [
#     ['Maria', 'Helena', ],
#     ['Elaine', ],
#     ['Luiz', 'João', 'Eduarda', (0,10,20,30,40) ],
# ]
# print(salas[1][0]) # [indice geral] [indice interno de uma lista]
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2]) # [indice geral] [indice interno de uma lista] [indice ainda mais interno]

# for sala in salas:
#     for aluno in sala:
#         print(aluno)
# ----------------------------------------------------------------
# Interpretador do Python

# python mod.py (executa o mod)
# python -u (unbuffered)
# python -m mod (lib mod como script)
# python -c 'cmd' (comando)
# python -i mod.py (interativo com mod)

# The Zen of Python, por Tim Peters

# Bonito é melhor que feio.
# Explícito é melhor que implícito.
# Simples é melhor que complexo.
# Complexo é melhor que complicado.
# Plano é melhor que aglomerado.
# Esparso é melhor que denso.
# Legibilidade conta.
# Casos especiais não são especiais o bastante para quebrar as regras.
# Embora a praticidade vença a pureza.
# Erros nunca devem passar silenciosamente.
# A menos que sejam explicitamente silenciados.
# Diante da ambiguidade, recuse a tentação de adivinhar.
# Deve haver um -- e só um -- modo óbvio para fazer algo.
# Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
# Agora é melhor que nunca.
# Embora nunca frequentemente seja melhor que *exatamente* agora.
# Se a implementação é difícil de explicar, é uma má ideia.
# Se a implementação é fácil de explicar, pode ser uma boa ideia.
# Namespaces são uma grande ideia -- vamos fazer mais dessas!
# ----------------------------------------------------------------
# Desempacotamentos em chamadas de métodos e funções
# string = 'ABCD'
# lista = ['Maria', 'Helena', 1, 2, 'Eduarda']
# tupla = 'Pyhton', 'é', 'legal'

# salas = [
#     ['Maria', 'Helena', ],
#     ['Elaine', ],
#     ['Luiz', 'João', 'Eduarda', (0,10,20,30,40) ],
# ]

# print(*salas, sep='\n')

# a, b, *_, c = lista 
# print(a, c)

# for nome in lista:
#     print(nome, end=' ')

# print(*lista)
# print(*string)
# print(*tupla)
# ----------------------------------------------------------------
# Operação ternária (condicional de uma linha)
# <valor> if <condicao> else <outro valor>
# print('Valor' if True else 'Outro valor')
# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

# digito = 9
# novo_digito = digito if digito <= 9 else 0
# novo_digito_novo = 0 if digito > 9 else digito
# print(novo_digito)

# print('Etaniel' if True else 'Gabrieli' if False else 'Octávio')
# ----------------------------------------------------------------
# Return
variavel = print('Luiz')
print(variavel) # Vai retornar None, pois print não guarda nenhum valor