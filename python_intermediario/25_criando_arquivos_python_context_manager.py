import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
# caminho_arquivo = '/home/etaniel/Área de Trabalho/pythonestudos/'
caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w') # cria o arquivo com o 'w'
# # #
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo: # context manager, ele ja abre e fecha o arquivo
#     arquivo.write('Linha 1\n') # escrever dentro do arquivo
#     arquivo.write('Linha 2\n') # escrever dentro do arquivo
#     arquivo.writelines(('Linha 3\n', 'Linha 4\n')) # ele adiciona varias linhas
#     arquivo.seek(0, 0) # mover o cursos no arquiv
#     print(arquivo.read()) #ler o arquivo completo quando o cursor voltou do inicio
#     arquivo.seek(0, 0)
#     print(arquivo.readline()) # (ler linha)
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('------------')
    
# with open(caminho_arquivo, 'r') as arquivo: # context manager, ele ja abre e fecha o arquivo
#     print(arquivo.read()) # ele vai ler o arquivo
    
# print('--------------------------------')

# modos:
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo: # context manager, ele ja abre e fecha o arquivo, o encoding é para escolher qual quer utilizar
    arquivo.write('Atenção\n') # escrever dentro do arquivo
    arquivo.write('Linha 1\n') # escrever dentro do arquivo
    arquivo.write('Linha 2\n') # escrever dentro do arquivo
    arquivo.writelines(('Linha 3\n', 'Linha 4\n')) # ele adiciona varias linhas
# o 'a' ele adiciona itens nas ultimas linhas

# os.remove('aula116.txt') # Ele remove o arquivo
# os.rename(caminho_arquivo, 'aula116-2.txt')