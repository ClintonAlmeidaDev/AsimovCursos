#exercicio de acerte o numero
numero_secreto = 14

numero_escolhido = int(input("Tente adivinhar o numero secreto: "))

numero_tentativas = 0


while True:

    if numero_escolhido == numero_secreto:
        print("Parabens, você acertou o numero secreto...")
        print(f"Com um total de {numero_tentativas} tentativas")
        break

    elif numero_escolhido > numero_secreto + 100:
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, mas dessa vez um valor mais baixo: ")))
        numero_tentativas = numero_tentativas + 1

    elif numero_escolhido < numero_secreto + 100:
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, com um valor mais alto: ")))
        numero_tentativas = numero_tentativas + 1

    elif numero_escolhido > numero_secreto + 50:
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, mas dessa vez um valor mais baixo: ")))
        numero_tentativas = numero_tentativas + 1

    elif numero_escolhido < numero_secreto + 50:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, com um valor mais alto: ")))

    elif numero_escolhido > numero_secreto + 20:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, mas dessa vez um valor mais baixo: ")))

    elif numero_escolhido < numero_secreto + 10:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, com um valor mais alto: ")))

    elif numero_escolhido > numero_secreto + 10:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, mas dessa vez com um valor mais baixo: ")))

    elif numero_escolhido < numero_secreto + 5:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, com um valor mais alto: ")))

    elif numero_escolhido > numero_secreto + 5:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, mas dessa vez com um valor mais baixo: ")))

    elif numero_escolhido < numero_secreto + 2:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, com um valor mais alto: ")))

    elif numero_escolhido > numero_secreto + 2:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, com um valor mais baixo: ")))

    elif numero_escolhido < numero_secreto + 1:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, com um valor mais alto: ")))

    elif numero_escolhido > numero_secreto + 1:
        numero_tentativas = numero_tentativas + 1
        numero_escolhido = int(input(("Passou longe demais, tenta de novo, com um valor mais baixo: ")))
