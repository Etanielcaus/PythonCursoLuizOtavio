# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 para manipular arquivos PDF (PdfReader)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

# Encontrar a pasta pdfs e criar o diretório para uma nova pasta
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

# Encontrar o arquivo pdf e ler
RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

# Criar a pasta nova
PASTA_NOVA.mkdir(exist_ok=True)

# Ler o arquivo pdf
reader = PdfReader(RELATORIO_BACEN)

# Quantas páginas tem o arquivo?
# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]  # textos

imagem0 = page0.images[0]  # imagens

# extrair o texto da página 0
# print(page0.extract_text())

# Salvar a imagem da página 0
with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)

# Criar um novo arquivo pdf com a página 0 e salvar
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore
