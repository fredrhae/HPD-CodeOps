import argparse

parser = argparse.ArgumentParser()

parser.add_argument("giropops", help="Comando para possuir nomes.", type=int)

args = parser.parse_args()

print(args)
