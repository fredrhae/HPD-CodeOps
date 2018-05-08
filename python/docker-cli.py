#!/usr/bin/env python3
import docker, argparse, sys
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
        print("get all: %s" % get_all)
        for cada_container in get_all:
           conectando = client.containers.get(cada_container.id)
           print("O container %s utiliza a imagem %s e está rodando o comando %s" % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))
    except Exception as e:
        logando('Erro! Algo não saiu como esperado, analis o log para ver o que houve.', e)
    finally:
        print('Comando executado!')

def procurar_container(args):
    """Função para procurar containers com o nome passado""" 
    counter = 0
    try:
        client = docker.from_env()
        get_all = client.containers.list()
        for cada_container in get_all:
           container = client.containers.get(cada_container.id)
           container_name = container.attrs['Config']['Image']
           if str(args.imagem).lower() in str(container_name).lower():
               print("Achei o container com id \'%s\' que contém a palavra \'%s\' cujo nome da imagem é: %s" % (container.short_id, args.imagem, container_name))
               counter += 1
    except Exception as e:
        logando('Erro! Algo não saiu como esperado, analise o log para ver o que houve.', e)
    finally:
        if(counter == 0):
            print("Nenhum container encontrado com a palavra \'%s\'" % (args.imagem))

def remover_containers_binding(self):
    """Função para remover containers com portas \'bindadas\'."""
    counter = 0
    try:
       client = docker.from_env()
       all_containers = client.containers.list()
       for cada_container in all_containers:
            container = client.containers.get(cada_container.id)
            container_porta = container.attrs['HostConfig']['PortBindings']
            if isinstance(container_porta,dict) and container_porta != {}:
                print("O container \'%s\' tem porta em \'binding\'. Parando e removendo o container..." % container.short_id)
                container.stop()
                container.remove()
                print("Container \'%s\' removido com sucesso.\n" % container.short_id)
                counter += 1
    except docker.errors.APIErrors as e:
        logando('Erro: api do docker retornou algum erro inesperado.', e)
    except Exception as e:
        logando('Erro! Algo não saiu como esperado, analise o log para ver o que houve.', e)
    finally:
        if(counter != 0):
            print("%d containers foram removidos" % counter)
        else:
            print("Nenhum container em binding para ser removido")


parser = argparse.ArgumentParser(description="Meu CLI docker fodástico, feito durante a aula HPD")
subparser = parser.add_subparsers()

listar_opt = subparser.add_parser('listar')
listar_opt.set_defaults(func=listar) 

criar_opt = subparser.add_parser('criar')
criar_opt.add_argument('--imagem',required=True)
criar_opt.add_argument('--comando',required=False)
criar_opt.add_argument('--detach',action='store_true',required=False,default=False)
criar_opt.set_defaults(func=criar_container) 

procurar_opt = subparser.add_parser('procurar')
procurar_opt.add_argument('--imagem',required=True)
procurar_opt.set_defaults(func=procurar_container) 

remover_binding_opt = subparser.add_parser('remover-binding')
remover_binding_opt.set_defaults(func=remover_containers_binding) 

if len(sys.argv[1:]) == 0:
    parser.print_help()
    parser.print_usage()
    parser.exit()

cmd = parser.parse_args()
cmd.func(cmd)
