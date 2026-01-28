from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
os.environ['SSL_CERT_FILE'] = certifi.where()

model = ChatOpenAI(
    model="gpt-4o-mini",  
    temperature=0
)
class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="""Generate details of a fictional {place} person.
Return ONLY a JSON object with these exact fields:
{{
  "name": "person's full name",
  "age": number greater than 18,
  "city": "city name"
}}

Example of valid response:
```json
{{
  "name": "John Doe",
  "age": 25,
  "city": "Colombo"
}}
Generate the response in JSON format ONLY:""",
input_variables=['place'],
partial_variables={'format_instruction': parser.get_format_instructions()}
)


# prompt = template.invoke({'place':'India'})

# result = model.invoke(prompt)

# final_result = parser.parse(result)

# print(final_result)

# using chain
chain = template | model | parser

final_result = chain.invoke({'place':'sri lankan'})

print(final_result)