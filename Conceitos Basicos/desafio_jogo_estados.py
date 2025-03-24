# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.
import random

estados_capitais = (
    ("Acre", "Rio Branco"),
    ("Alagoas", "Maceio"),
    ("Amapa", "Macapa"),
    ("Amazonas", "Manaus"),
    ("Bahia", "Salvador"),
    ("Ceara", "Fortaleza"),
    ("Distrito Federal", "Brasilia"),
    ("Espirito Santo", "Vitoria"),
    ("Goias", "Goiania"),
    ("Maranhao", "Sao Luis"),
    ("Mato Grosso", "Cuiaba"),
    ("Mato Grosso do Sul", "Campo Grande"),
    ("Minas Gerais", "Belo Horizonte"),
    ("Para", "Belem"),
    ("Paraiba", "Joao Pessoa"),
    ("Parana", "Curitiba"),
    ("Pernambuco", "Recife"),
    ("Piaui", "Teresina"),
    ("Rio de Janeiro", "Rio de Janeiro"),
    ("Rio Grande do Norte", "Natal"),
    ("Rio Grande do Sul", "Porto Alegre"),
    ("Rondonia", "Porto Velho"),
    ("Roraima", "Boa Vista"),
    ("Santa Catarina", "Florianopolis"),
    ("Sao Paulo", "Sao Paulo"),
    ("Sergipe", "Aracaju"),
    ("Tocantins", "Palmas"),
)

acertos = 0
erros = 0
qtdPerguntas = 0
opcao = 1
resposta = 'nda'
listaTemp = list(estados_capitais)
random.shuffle(listaTemp)
estados_embaralhada = tuple(listaTemp)

while opcao == 1:
    print("Jogo dos Estados\n\n")
    for k, v in estados_embaralhada:
        if opcao == 0:
            break
        resposta = str(input(f'Qual a capital da UF {k} ?\n'))
        qtdPerguntas = qtdPerguntas + 1
        if resposta.lower() == v.lower():
            print("Certa resposta ")
            acertos = acertos + 1
        else:
            print(f'Errado, a resposta correta e: {v}')
        
        print('Escolha uma das opcoes abaixo: ')
        print('1 - Continuar com a proxima pergunta')
        print('0 - Finalizar o jogo')
        
        while opcao != 1 or opcao != 0:
            opcao = int(input(': '))
            if opcao == 1:
                break
            elif opcao == 0:
                break
            else:
                print("Opcao invalida, digite uma opcao valida")
    
    print("FIM DE JOGO")
    mediaAcertos = (acertos/qtdPerguntas) * 100
    print(f'VOCE ACERTOU {round(mediaAcertos,2)} %')