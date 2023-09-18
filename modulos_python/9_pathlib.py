# O módulo pathlib em Python fornece uma interface orientada a objetos para
# manipulação de caminhos de arquivos e diretórios de uma maneira mais
# intuitiva e eficiente do que as abordagens tradicionais baseadas em strings.
# Ele foi introduzido na versão Python 3.4 e oferece uma maneira mais moderna e
# legível de lidar com operações relacionadas a arquivos e diretórios.

# Aqui estão algumas das funcionalidades e conceitos-chave do pathlib:

# Objetos Path: O pathlib introduz a classe Path que representa caminhos de
# arquivos e diretórios. Você pode criar objetos Path para representar caminhos
# em seu sistema de arquivos e, em seguida, realizar várias operações nesses
# objetos.

# Manipulação de Caminhos: Com objetos Path, você pode realizar operações
# comuns, como concatenar caminhos, verificar se um caminho existe, criar ou
# excluir diretórios e arquivos, e muito mais.

# Resolução de Caminhos: O pathlib lida automaticamente com a resolução de
# caminhos absolutos e relativos, tornando mais fácil trabalhar com caminhos
# em diferentes contextos.

# Iteração em Diretórios: Você pode usar o método iterdir() para iterar sobre
# os itens em um diretório, como arquivos e subdiretórios.

# Comportamento Multiplataforma: O pathlib é projetado para ser independente
# de plataforma, o que significa que suas operações funcionarão de maneira
# consistente em sistemas operacionais diferentes, como Windows, macOS e Linux.

from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)  # pega o arquivo atual, deste arquivo atual

# print(caminho_arquivo.parent)  # caminho do arquivo parente do anterior
# print(caminho_arquivo.parent.parent)  # caminho do arquivo parente do anterio

ideias = caminho_arquivo.parent / 'ideias'
# print(ideias)

# arquivo = Path.home() / 'Área de Trabalho' / 'arquivo.txt'
# arquivo.touch()  # Cria um arquivo
# print(arquivo)
# arquivo.write_text('Olá mundo')  # Escrever dentro do arquivo
# print(arquivo.read_text())  # Ler o que está dentro do arquivo
# arquivo.unlink()  # Deletar arquivo
area_de_trabalho = Path.home() / 'Área de Trabalho'

caminho_arquivo = (Path.home() /
                   'Área de Trabalho' /
                   'desenvolvimento' /
                   'arquivo.txt')

print(caminho_arquivo)
caminho_arquivo.touch()
# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha\n')
#     file.write('Outra linha\n')

# print(caminho_arquivo.read_text())

caminho_pasta = Path.home() / 'Área de Trabalho' / 'pasta'
caminho_pasta.mkdir(exist_ok=True)  # Criar pasta
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

for item in area_de_trabalho.iterdir():
    print(item.name)
