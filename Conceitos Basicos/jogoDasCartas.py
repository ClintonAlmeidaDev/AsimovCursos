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
    
    valor = 0
    for indice, i in enumerate(baralho):
        valor = valor + len(baralho[indice])
        
    print(f'QUANTIDADE DE CARTAS: {valor}')  
    print(*baralho)  

def dar_as_cartas(baralho, qtdJogadores, qtdCartas):
    jogadores_agrupados = []
    for _ in range(qtdJogadores):
        lista = []
        jogadores_agrupados.append(lista)

    for indCartas, carta in enumerate(range(qtdCartas)):
        for indiceJogadores, i in enumerate(range(qtdJogadores)):
            listaBaralhoTemp = list(baralho)
            print(f'Carta da Lista - {listaBaralhoTemp[indiceJogadores][indCartas]}')
            cartaTemp = listaBaralhoTemp.pop([indiceJogadores][indCartas])
            baralho = tuple(listaBaralhoTemp)
            jogadores_agrupados[indiceJogadores].append(cartaTemp)


    return jogadores_agrupados



valores = gerar_baralho(2, True, True)

jogadores = dar_as_cartas(valores, 2, 9)

print(jogadores)

# for indice, i in enumerate(jogadores):
#     print(f'{indice} - {i}')

#mostrar_baralho(valores)
    
    


