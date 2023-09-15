# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# import os
# import shutil

# # caminho = os.path.join('/home', 'etaniel', 'Documentos', 'exemplo')

# HOME = os.path.expanduser('~')
# DOCUMENTOS = os.path.join(HOME, 'Documentos')
# EXEMPLO = os.path.join(DOCUMENTOS, 'exemplo')
# NOVA_PASTA = os.path.join(EXEMPLO, 'NOVA_PASTA')

# os.makedirs(NOVA_PASTA, exist_ok=False)

# for root, dirs, files in os.walk(EXEMPLO):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             NOVA_PASTA, os.path.relpath(os.path.join(root, dir_), EXEMPLO)
#         )
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(
#             NOVA_PASTA, os.path.relpath(caminho_arquivo, EXEMPLO)
#         )
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)


import os
import shutil

# HOME = os.path.expanduser('~')
# DOCUMENTOS = os.path.join(HOME, 'Documentos')
# EXEMPLO = os.path.join(DOCUMENTOS, 'exemplo')
# NOVA_PASTA = os.path.join(EXEMPLO, 'NOVA_PASTA')

# os.makedirs(NOVA_PASTA, exist_ok=False)

# for root, _, files in os.walk(EXEMPLO):
#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(NOVA_PASTA, file)
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)

# ----------------------------------------------------------------
# copytree()
HOME = os.path.expanduser('~')
DOCUMENTOS = os.path.join(HOME, 'Documentos')
EXEMPLO = os.path.join(DOCUMENTOS, 'exemplo')
NOVA_PASTA = os.path.join(EXEMPLO, 'NOVA_PASTA')

try:
    shutil.rmtree(NOVA_PASTA)
except Exception:
    shutil.copytree(EXEMPLO, NOVA_PASTA)
