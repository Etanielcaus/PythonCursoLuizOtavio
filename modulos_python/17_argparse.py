# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

# Crie um objeto ArgumentParser
parser = ArgumentParser()

# Adicione a opção -b/--basic
parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    type=str,  # Tipo do argumento
    metavar='STRING',
    # default='Olá mundo',  # Valor padrão como uma lista
    required=False,
    action='append',  # Recebe o argumento mais de uma vez
    nargs='+',  # Recebe mais de um valor
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
)

# recebe os argumentos parseados
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

print(args.verbose)
