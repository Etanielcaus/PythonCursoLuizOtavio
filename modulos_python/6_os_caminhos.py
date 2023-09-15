# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os
from itertools import count

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
# print(nome_arquivo, extensao_arquivo)
# print(os.path.exists('/home/etaniel/Área de Trabalho/desenvolvimento/python
# estudos Otavio Miranda'))
# print(os.path.abspath('.'))
print(caminho)
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))
print('-' * 80)

# ----------------------------------------------------------------
# os.listdir para navegar em caminhos
# /home/etaniel/Documentos/exemplo
# C:/home/etaniel/Documentos/exemplo
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

caminho = os.path.join('/home', 'etaniel', 'Documentos', 'exemplo')
print(caminho)

for pasta in os.listdir(caminho):
    print(f'--{pasta}')
    caminho_pasta = os.path.join(caminho, pasta)
    if os.path.isdir(caminho_pasta):
        print(f'Conteúdo de {pasta}:')
        for item in os.listdir(caminho_pasta):
            print(f'  {item}')

# ----------------------------------------------------------------
# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
# from itertools import count

caminho = os.path.join('/home', 'etaniel', 'Documentos', 'exemplo')
print(caminho)
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)
