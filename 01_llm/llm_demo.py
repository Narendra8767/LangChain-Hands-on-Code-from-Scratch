from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
os.environ['SSL_CERT_FILE'] = certifi.where()

llm = ChatOpenAI(
    model="gpt-4o-mini",  
    temperature=0
)

results = llm.invoke('What is Capital of India')

print(results.content)