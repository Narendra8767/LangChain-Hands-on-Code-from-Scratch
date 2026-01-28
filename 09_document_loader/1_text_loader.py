from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
os.environ['SSL_CERT_FILE'] = certifi.where()

model = ChatOpenAI(
    model="gpt-4o-mini",  
    temperature=0
)

prompt = PromptTemplate(
    template='Write a summary for the following text - \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

loader = TextLoader(r'C:\Users\narendra tekale\Langchain_campusx\9_document_loader\AB_de.txt')

docs = loader.load()

# print(docs)
# print(type(docs))
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'text':docs[0].page_content}))