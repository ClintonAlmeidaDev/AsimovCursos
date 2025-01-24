def resposta_bot(mensagens):
    return 'Resposta do Bot'

print('Bem-vindo ao AsimoBot')

mensagens = []
while True:
    pergunta = input('Usuario: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')

print('Muito obrigado por usar o AsimoBot')
print(mensagens)