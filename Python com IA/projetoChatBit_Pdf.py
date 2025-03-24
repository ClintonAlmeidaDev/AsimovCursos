import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.2-1b-preview')

caminho = 'arquivos/CLINTON DE ALMEIDA - 2022310354 - ANHEMBI MORUMBI.pdf'
loader = PyPDFLoader(caminho)
lista_documentos = loader.load()

documento = ''
for doc in lista_documentos:
    documento = doc.page_content + documento

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigavel, que possui as seguinte informações para formular uma resposta: {informacoes}'),
    ('user', '{input}')
])

chat_pdf = template | chat

resposta = chat_pdf.invoke({'informacoes': documento, 'input': 'Qual o titulo desse livro?'})

print(resposta)