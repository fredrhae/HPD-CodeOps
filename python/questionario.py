#!/usr/bin/env python
print('Olá, sou a Elisabot. Bot de atualização cadastral. Tudo bem?\n')
print('Vou coletar algumas informações contigos, certo? Vamos começar.\n')

print('Qual é o seu nome?')
nome = input()

print('Prazer em te conhecer, %s\n' % nome)

print('Qual a sua idade?')
idade = input()

print('Sua idade é ' + str(idade) + '. Anotei aqui.\n')

print('Qual o seu sexo?')
sexo = input()

print('Você se definiu como: %s\n' %sexo)

print('Qual a cidade que você mora?')
cidade = input()

print('Humm, legal! Se eu fosse de verdade queria conhecer {}\n'.format(cidade))
# Outra forma de escrever a bagaça
#print('Humm, legal! Se eu fosse de verdade queria conhecer {cidade}\n'.format(cidade = "Porto Alegre"))

print('Ela fica em qual estado brasileiro?')
estado = input()

print('Já sei que irei conhecer %s quando eu tiver forma física!\n' % estado)

print('Estamos terminando, só falta eu saber mais uma coisa. Qual seu estado civil?')
estado_civil = input()

print('Ok, então você %s é %s\n' % (nome,estado_civil))

print('Obrigado, finalizei o questionário. Tenha um ótimo dia %s\n' % nome)

