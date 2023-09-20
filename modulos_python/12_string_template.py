# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime
from pathlib import Path
import json
from typing import TypedDict

# caminho para salvar em .json
NOME_ARQUIVO = '12_string.json'
CAMINHO_DO_JSON = Path(__file__).resolve().parent / NOME_ARQUIVO

# caminho com o template string
CAMINHO_ARQUIVO = Path(__file__).parent / '12_string.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)


# tipagem dos dados
class Tipo_dados(TypedDict):
    nome: str
    valor: float
    data: str
    empresa: str
    telefone: str


# o dicionario com a tipagem
dados: Tipo_dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)


# Definir um delimitador diferente
class MyTemplate(string.Template):
    delimiter = '%'


# criar um json para salvar os dados
with open(CAMINHO_DO_JSON, 'w') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)

# leitura com o template string
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.safe_substitute(dados))
# explicando o código:
# 1. abra o arquivo com open() dentro de CAMINHO_ARQUIVO contém
# o caminho para o arquivo com o template string 12_string.txt
# 2. leia o arquivo com read()
# 3. crie um objeto MyTemplate() com o conteúdo lido, e variáveis a serem lidos
# 4. substitua as variáveis com substitute()

print('-' * 80)

# substituir variáveis com string.Template()
texto = 'Olá, ${nome}. Você tem ${valor} para pagar em ${data}.' \
        ' Entre em contato com ${empresa} pelo telefone ${telefone}'
template = string.Template(texto)
print(template.safe_substitute(dados))
