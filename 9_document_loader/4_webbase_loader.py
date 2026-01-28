from langchain_community.document_loaders import WebBaseLoader
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
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)


parser = StrOutputParser()

url = "https://www.amazon.in/dp/B0D7Z8CJP8/?_encoding=UTF8&ref_=cct_cg_Budget_3c1&pf_rd_p=08cca591-02d2-42db-b7e0-2108e1b9e9ab&pf_rd_r=90Q00X8ZFN9PJZPF74J7&th=1"
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))