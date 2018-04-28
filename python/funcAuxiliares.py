#!/usr/bin/env python3

def pause():
    input("\n\nPressione enter para continuar...\n\n")

def mensagemFim():
    print("Valeu por usar esse programa!")

def imprimaTresLinhas():
    for i in range(1,4):
        print('Esta eh a linha ' + str(i))

def imprimaNoveLinhas():
    for i in range(1,4):
        imprimaTresLinhas()

def mensagemInicio():
    print("Este programa eh somente para mostrar como funciona o uso de functions")
    pause()

def linhaBranco():
    print()

def limpaTela():
    for i in range(1,26):
        linhaBranco()

mensagemInicio()

imprimaTresLinhas()
print('Testando o paranauê')
imprimaNoveLinhas()
print('Não é que funciona?!')
linhaBranco()
print('Hello functions world!')
pause()
limpaTela()
mensagemFim()
