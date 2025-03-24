listaBaralho = ['2','3','4','5','6','0','1']

def retornaLista(listaBaralho, qtdJogadores, qtdCartas):
    jogadores_agrupados = []
    for _ in range(qtdJogadores):
        lista = []
        jogadores_agrupados.append(lista)

    for carta in range(qtdCartas):
        for indice, i in enumerate(range(qtdJogadores)):
            cartaTemp = listaBaralho.pop()
            jogadores_agrupados[indice].append(cartaTemp)


    return jogadores_agrupados

print(listaBaralho)
listaDeJogadores = retornaLista(listaBaralho, 2, 3)
print(listaBaralho)

print(listaDeJogadores)