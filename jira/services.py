from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits.jira.toolkit import JiraToolkit
from langchain.llms import OpenAI
from langchain.utilities.jira import JiraAPIWrapper
from dotenv import load_dotenv

# Reading environment variables from .env as well
load_dotenv()

# Initializing OpenAI object with the temperature parameter (0 - 1). 0 = highest probability 1 = more creativity.
llm = OpenAI(temperature=0)
# Initializing Jira API object
jira = JiraAPIWrapper()
# This is an already built in toolkit for jira
toolkit = JiraToolkit.from_jira_api_wrapper(jira)
# initializing agent. Agents are used to communicate to different APIs
agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# This will convert our message string to jira json object and make request to Jira.
agent.run("create a new task with highest priority in project KUB with title Hello and description world")
