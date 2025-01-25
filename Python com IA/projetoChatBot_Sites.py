import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import ChatPromptTemplate


api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.2-1b-preview')

loader = WebBaseLoader('https://consciencianerd.com/')
lista_documentos = loader.load()

documento = ''
for doc in lista_documentos:
    documento = documento + doc.page_content

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}'),
    ('user', '{input}')
])

chain = template | chat
resposta = chain.invoke({'documentos_informados': documento, 'input': 'Qual o conteudo desse site'})

print(resposta.content)