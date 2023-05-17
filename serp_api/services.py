from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from dotenv import load_dotenv

# Reading environment variables from .env as well
load_dotenv()

# Initializing world
search = SerpAPIWrapper()
# Creating a tool which will help be connected to our agent so it can do a google search if needed.
tools = [
    Tool(
        name="google_search",
        func=search.run,
        description="use to find answers from internet"
    ),
]
# Creating a memory which is a must for this agent
memory = ConversationBufferMemory(memory_key="chat_history")

llm = OpenAI(temperature=0)
# init agent with CONVERSATIONAL_REACT_DESCRIPTION agent type. This is the best optimized agent type for conversations.
agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)

agent_chain.run(input="Hi, I am Pargev")
agent_chain.run(input="Should you use a tool for this question?")
agent_chain.run(input="When will the next soccer world cup take place?")
agent_chain.run(input="Do you remember who am I?")

