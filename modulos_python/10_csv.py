# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para uma
# planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
# Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
# editor de texto ou em uma planilha eletrônica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Luiz Otávio,32,"Av Brasil, 21, Centro"
# João da Silva,55,"Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas da, enquanto as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simples do CSV
# 1 - Separe os valores das colunas com um delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / '10_csv_ex.csv'
# print(CAMINHO_CSV)

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.DictReader(arquivo)

#     for linha in leitor:
#         print(linha['Nome'], linha['Idade'], linha['Endereço'])

print('-' * 80)

# -----------------------------------------------
# Escrever no csv (csv.writer e csv.DictWriter)

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)


# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)
