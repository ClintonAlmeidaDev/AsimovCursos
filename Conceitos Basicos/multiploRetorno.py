def retornaMultiplosValores(qtdValores):
    lista = []
    for i in range(1, qtdValores + 1):
        lista.append(i)

    return lista



a, b, c, d = retornaMultiplosValores(4)

print(a)
print(b)
print(c)
print(d)
