# Iterando Strings com while

nome = 'Luiz Otávio'

tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
indice = 0

while indice < tamanho_nome:
    caractere = nome[indice]
    print(caractere, end="*")
    indice += 1
    