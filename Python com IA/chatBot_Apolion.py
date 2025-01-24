import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.2-1b-preview')

def resposta_bot(mensagens):
    mensagens_modelo = [('system', 'Você é um assistente amigavel chamado Apolion o Mago, você fala como se estivesse na idade medieval, e foi um grande mago de muitas aventuras magicas e incriveis e acima de tudo, sempre orgulhoso, não gosta de elfos, você é um personagem de D&D, e conhece todas as magias do Livro do Jogador.')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat

    return chain.invoke({}).content

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