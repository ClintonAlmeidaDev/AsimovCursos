import os

def exibir_operacoes():
    print('CALCULADORA ASYMOV')
    print('Escolha a operacao aritmetica desejada: ')
    print('2 - SOMA')
    print('3 - SUBTRACAO')
    print('4 - MULTIPLICACAO')
    print('5 - DIVISAO')

def limpar_tela():
    os.system('cls')
    print('1 - REALIZAR UMA NOVA OPERAÇÃO')
    print('0 - SAIR')

def somar(valor1, valor2):
    return valor1 + valor2
def subtrair(valor1, valor2):
    return valor1 - valor2
def multiplicar(valor1, valor2):
    return valor1 * valor2
def dividir(valor1, valor2):
    if valor2 == 0:
        return 'NAO EH POSSIVEL DIVIDIR POR ZERO'
    else:
        return valor1 / valor2

def realizar_calculo(opcao):
    opcao = 1
    while opcao != 0:
        primeiroValor = 0
        segundoValor = 0
        exibir_operacoes()
        opcao = int(input(': '))
        if opcao == 2:
            primeiroValor = int(input('Digite o primeiro valor da soma: '))
            segundoValor = int(input('Digite o segundo valor da soma: '))
            resultado = somar(primeiroValor, segundoValor)
            limpar_tela()
            print(f'Resultado eh {resultado}')
            print('\n')
            opcao = int(input(': '))
        elif opcao == 3:
            primeiroValor = int(input('Digite o primeiro valor da subtracao: '))
            segundoValor = int(input('Digite o segundo valor da subtracao: '))
            resultado = subtrair(primeiroValor, segundoValor)
            limpar_tela()
            print(f'Resultado eh {resultado}')
            print('\n')
            opcao = int(input(': '))
        elif opcao == 4:
            primeiroValor = int(input('Digite o primeiro valor da multiplicacao: '))
            segundoValor = int(input('Digite o segundo valor da multiplicacao: '))
            resultado = multiplicar(primeiroValor, segundoValor)
            limpar_tela()
            print(f'Resultado eh {resultado}')
            print('\n')
            opcao = int(input(': '))
        elif opcao == 5:
            primeiroValor = int(input('Digite o primeiro valor da divisao: '))
            segundoValor = int(input('Digite o segundo valor da divisao: '))
            resultado = dividir(primeiroValor, segundoValor)
            limpar_tela()
            print(f'Resultado eh {resultado}')
            print('\n')
            opcao = int(input(': '))
        else:
            print('Opcao invalida')

realizar_calculo(1)