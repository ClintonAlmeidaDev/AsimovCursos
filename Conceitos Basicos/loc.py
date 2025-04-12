import os



def exibir_veiculos(veiculos_aluguel):
    for indice, i in enumerate(veiculos_aluguel):
        print(f'ID: {indice} - VEICULO: {i['veiculo']} -  VALOR: {i['valor']}')

def alugar_veiculo(veiculos_aluguel, locatario, idVeiculo):
    print('ESCOLHA O VEICULO DESEJADO: ')
    print('\n')
    exibir_veiculos(veiculos_aluguel)
    veiculo = veiculos_aluguel.pop(idVeiculo)
    locatario.append(veiculo)

def devolver_veiculo(veiculos_aluguel, locatario, idVeiculo):
    print('ESCOLHA O VEICULO DESEJADO: ')
    print('\n')
    exibir_veiculos(locatario)
    
    veiculo = locatario.pop(idVeiculo)
    veiculos_aluguel.append(veiculo)

def opcoes_menu():
    print('1 - EXIBIR VEICULOS PARA ALUGUEL')
    print('2 - ALUGAR VEICULO')
    print('3 - DEVOLVER VEICULO')

def sub_menu():
    print('\n\n')
    print('0 - SAIR')
    print('4 - VOLTAR AO MENU ANTERIOR')

def executar_programa(veiculos_aluguel, locatario):
    opcao = 4
    idVeiculo = ''
    while opcao != 0:    

        if opcao == 1:
            exibir_veiculos(veiculos_aluguel)
            sub_menu()
            opcao = int(input(': '))
            os.system("cls")
        elif opcao == 2:
            exibir_veiculos(veiculos_aluguel)
            idVeiculo = int(input(': '))
            alugar_veiculo(veiculos_aluguel, locatario, idVeiculo)
            sub_menu()
            opcao = int(input(': '))
            os.system("cls")
        elif opcao == 3:
            exibir_veiculos(locatario)
            idVeiculo = int(input(': '))
            devolver_veiculo(veiculos_aluguel, locatario, idVeiculo)
            sub_menu()
            opcao = int(input(': '))
            os.system("cls")
        elif opcao == 4:
            opcoes_menu()
            opcao = int(input(': '))
            os.system("cls")
        else:
            print("OPCAO INVALIDA")


veiculos_aluguel = [
    {'veiculo': 'Onix LTX 2018', 'valor': 459.39 },
    {'veiculo': 'Renault Kwid', 'valor': 130.19 },
    {'veiculo': 'Fiat Uno', 'valor': 220.49 },
    {'veiculo': 'Volkswagen Gol', 'valor': 70.00 },
    {'veiculo': 'Jeep Renegade', 'valor': 560.20 },
    {'veiculo': 'Renault Sandero', 'valor': 400.20 },
    {'veiculo': 'Renault Logan', 'valor': 370.00 },
    {'veiculo': 'Hyundai Hb20', 'valor': 459.39 },
    {'veiculo': 'Fiat Strada', 'valor': 560.99 },
    {'veiculo': 'Volkswagen Voyage', 'valor': 410.00 },
    { 'veiculo': 'Fiat Argo', 'valor': 470/.30 }
]

locatario = []


executar_programa(veiculos_aluguel, locatario)