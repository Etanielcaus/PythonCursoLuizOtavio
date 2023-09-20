import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="Texto aqui")
args = parser.parse_args()
print(args.echo)
