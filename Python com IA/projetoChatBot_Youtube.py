import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.2-1b-preview')

url = 'https://www.youtube.com/watch?v=jDSh7fBigPU'

loader = YoutubeLoader.from_youtube_url(
        url,
        language=['pt']
    )

lista_documentos = loader.load()

documento = ''

for doc in lista_documentos:
    documento = doc.page_content + documento

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigavel, que possui as seguinte informações para formular uma resposta: {informacoes}'),
    ('user', '{input}')
])

chain_Youtube = template | chat

resposta = chain_Youtube.invoke({'informacoes': documento, 'input': 'Como posso fazer uma empada?'})

print(resposta)