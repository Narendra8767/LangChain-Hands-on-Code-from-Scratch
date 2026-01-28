from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
os.environ['SSL_CERT_FILE'] = certifi.where()

llm = ChatOpenAI(
    model="gpt-4o-mini",  
    temperature=0
)


# 1st promptv -> detailed report
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)


# 2nd prompt -> summary
template2 = PromptTemplate(
    template='write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = llm.invoke(prompt1)

prompt2 = template2.invoke({'text':result})

result1 = llm.invoke(prompt2)

print("Detailed Answer : ",result)
print("5 line Summary : ",result1.content)