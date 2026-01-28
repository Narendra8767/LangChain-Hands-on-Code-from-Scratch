from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Initialize the Ollama model (replace 'llama3' with your model name)
model = OllamaLLM(model="llama3.2")

message = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about Langchain')
]

# Get response (returns string directly)
result = model.invoke(message[1].content)  # Pass just the text content

# If you need AIMessage formatting:
response_message = AIMessage(content=result)

# Now you can use response_message.content safely
print(response_message.content)