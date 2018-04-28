import subprocess, argparse

def criar(args):
    """Cria o diretorio desejado"""
    diretorio = args.nome
    print(diretorio)
    subprocess.call(['mkdir', '-p', args.nome])
    for i in range(1,40):
      subprocess.call(['touch', str(i)],cwd=args.nome)

def listar(args):
    """Lista o diretorio desejado"""
    subprocess.call(['ls', args.nome])

def reiniciar():
    subprocess.call(['init 6'])

def listar_interfaces_redes(args):
    """Lista a interface de rede desejada"""
    interface = str(args.interface)
    print('interface: ' + interface)
    if interface != "None":
      subprocess.call(['ifconfig', str(args.interface)])
    else:
      subprocess.call(['ifconfig'])

parser = argparse.ArgumentParser(description="Comando para criar e listar diretorios durante a aula.")


subparser = parser.add_subparsers()

criar_dir = subparser.add_parser('criar')
criar_dir.add_argument('--nome', required=True)
criar_dir.set_defaults(func=criar)

listar_dir = subparser.add_parser('listar')
listar_dir.add_argument('--nome', required=True)
listar_dir.set_defaults(func=listar)

reiniciar = subparser.add_parser('reiniciar')
reiniciar.set_defaults(func=reiniciar)

listar_interface_rede = subparser.add_parser('rede')
listar_interface_rede.add_argument('--interface', required=False)
listar_interface_rede.set_defaults(func=listar_interfaces_redes)

cmd = parser.parse_args()
cmd.func(cmd)

