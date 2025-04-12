import random
def gerar_baralho(qtdBaralhos, possuiCoringas = False, deveSerEmbaralhado = False):

    lista_nipes = ['♠', '♥', '♦', '♣']
    lista_valores = list(['A']) + list(range(2,11)) + list('J') + list('Q') + list('K')
    
    baralhos = []
    baralho = []

    for nipe in lista_nipes:
        for valor in lista_valores:
            baralho.append(str(f'{nipe} - {valor}'))
    
    if possuiCoringas:
        for i in range(qtdBaralhos):
            baralho.append('CORINGA')
            
    
    for i in range(qtdBaralhos):
        copia = baralho.copy()
        baralhos.append(copia)

    if deveSerEmbaralhado:
        for indice, i in enumerate(baralhos):
            random.shuffle(baralhos[indice])

    return tuple(baralhos)

def mostrar_baralho(baralho):
    baralhoTemp = list(baralho)
    for i in baralhoTemp:
        print(f'Quantidade de cartas por baralho: {len(i)}')

    print(f'Cartas: {baralhoTemp}')

def dar_as_cartas(baralho, qtdJogadores, qtdCartas):
    grupoJogadores = []

    for _ in range(qtdJogadores):
        lista = []
        grupoJogadores.append(lista)

    for qc in range(qtdCartas):
        for indice, ij in enumerate(range(qtdJogadores)):
            for i in baralho:
                if i:
                    cartaTemporaria = i.pop()
                    grupoJogadores[indice].append(cartaTemporaria)
                    break
                else:
                    continue
    return grupoJogadores

def mostrar_jogadores(jogadores):
    for indice, i in enumerate(jogadores):
        print(f'JOGADOR {indice} \n QUANTIDADE DE CARTAS {len(i)} \n CARTAS: {i}')

valores = gerar_baralho(2, True, True)

mostrar_baralho(valores)
jogadores = dar_as_cartas(valores, 2, 40)
mostrar_baralho(valores)
mostrar_jogadores(jogadores)

    
    


