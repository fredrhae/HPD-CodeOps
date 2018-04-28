#!/usr/bin/env python3
import docker, argparse

def listar(self):
    """Listando os containers e suas respectivas imgens"""
    client = docker.from_env()
    get_all = client.containers.list()
    for cada_container in get_all:
       conectando = client.containers.get(cada_container.id)
       print("O container %s utiliza a imagem %s e está rodando o comando %s" % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))


parser = argparse.ArgumentParser(description="Meu CLI docker fodástico, feito durante a aula HPD")
subparser = parser.add_subparsers()

listar_opt = subparser.add_parser('listar')
listar_opt.set_defaults(func=listar) 

cmd = parser.parse_args()
cmd.func(cmd)
