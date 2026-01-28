from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

from dotenv import load_dotenv
import certifi
import os

load_dotenv()
os.environ['SSL_CERT_FILE'] = certifi.where()

model = ChatOpenAI(
    model="gpt-4o-mini",  
    temperature=0
)
parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name,age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result)

# Using chain
chain = template | model | parser

result = chain.invoke({ })

print(result)