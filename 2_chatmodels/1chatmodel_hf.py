from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    temperature=0.1,
    max_new_tokens=512
)

# Create chat model
chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("What is the capital of India")

print(result.content)