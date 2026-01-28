from langchain_ollama import OllamaLLM
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_core.prompts import PromptTemplate

from datetime import datetime


# 1. Define a simple tool
def get_current_time(_):
    return f"The current time is: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

tools = [
    Tool(
        name="get_current_time",
        func=get_current_time,
        description="Use this to know the current date and time.",
    ),
]

# 2. Load LLaMA 3.2 via Ollama
llm = OllamaLLM(model="llama3.2")

# 3. Initialize LangChain Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 4. Ask a question
agent.run("What is the current time?")
