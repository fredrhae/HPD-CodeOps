#!/usr/bin/env python3
import docker, argparse
from datetime import datetime

def logando(mensagem, e, lofile='docker-cli.log'):
    """Função para logar mensagens da aplicação"""
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
    with open('docker-cli.log','a') as log:
        texto = "%s \t %s \t %s \n" % (data_atual, mensagem, str(e))
        log.write(texto)

def criar_container(args):
    """Função para criar um container usando a biblioteca do docker"""
    try:
        client = docker.from_env()
        executando = client.containers.run(args.imagem, args.comando,detach=args.detach)
        return(executando)
    except docker.errors.ImageNotFound as e:
        logando('Erro: Essa imagem não existe!', e)
    except docker.errors.NotFound as e:
        logando('Erro: Esse comando não existe!', e)
    except Exception as e:
        logando('Erro! Favor verificar o comando digitado', e)
    finally:
        print('Comando executado!')

def listar(self):
    """Listando os containers e suas respectivas imgens"""
    try:

        client = docker.from_env()
        get_all = client.containers.list()
        for cada_container in get_all:
           conectando = client.containers.get(cada_container.id)
           print("O container %s utiliza a imagem %s e está rodando o comando %s" % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))
    except Exception as e:
        logando('Erro! Algo não saiu como esperado, analis o log para ver o que houve.', e)
    finally:
        print('Comando executado!')


parser = argparse.ArgumentParser(description="Meu CLI docker fodástico, feito durante a aula HPD")
subparser = parser.add_subparsers()

listar_opt = subparser.add_parser('listar')
listar_opt.set_defaults(func=listar) 

criar_opt = subparser.add_parser('criar')
criar_opt.add_argument('--imagem',required=True)
criar_opt.add_argument('--comando',required=False)
criar_opt.add_argument('--detach',action='store_true',required=False,default=False)
criar_opt.set_defaults(func=criar_container) 

cmd = parser.parse_args()
cmd.func(cmd)
