alunos = [[1,2,3,4,5], [3,4,5,6,7], [9,8,7,6,5,4], [6,5,7,3,5,3]]

print(alunos)

def distribuir_as_cartas(alunos, qtdJogadores, qtdCartas):
    grupoJogadores = []
    for _ in range(qtdJogadores):
        lista = []
        grupoJogadores.append(lista)

    for qc in range(qtdCartas):
        for indice, ij in enumerate(range(qtdJogadores)):
            for i in alunos:
                if i:
                    cartaTemporaria = i.pop()
                    grupoJogadores[indice].append(cartaTemporaria)
                    break
                else:
                    continue
                

    return grupoJogadores

jogadores = distribuir_as_cartas(alunos, 2, 3)

print(jogadores)
print(alunos)