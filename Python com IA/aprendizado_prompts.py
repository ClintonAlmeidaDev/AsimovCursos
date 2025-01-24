import os
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.2-1b-preview')

template = ChatPromptTemplate.from_messages(
        [
            ('system', 'Você é um assistente humorista, responde fazendo piadas'),
            ('user', 'Traduza {expressao} para a {lingua}')
        ]
    )

#template.invoke({'expressao': 'Beleza?', 'lingua': 'inglês'})

chain = template | chat

resposta = chain.invoke({'expressao': 'Comendo macarrao?', 'lingua': 'inglês'})

print(resposta.content)

