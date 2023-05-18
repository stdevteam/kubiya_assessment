from langchain.agents import AgentExecutor, BaseSingleActionAgent, Tool
from langchain.schema import AgentAction, AgentFinish

from typing import List, Tuple, Any, Union

from tools import generate_simple_math_task


tools = [
    Tool(
        name="Simple Math",
        func=generate_simple_math_task,
        description="Useful for generating mathematical problems"
    )
]


class MyCustomAgent(BaseSingleActionAgent):
    """
    A custom agent to decide the action
    """

    @property
    def input_keys(self):
        return ["input"]

    def plan(
            self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """
        The function will decide which tool to use
        :param intermediate_steps: Steps the LLM has taken to date, along with observations
        :param kwargs: User inputs.
        :return: Action specifying what tool to use.
        """
        if not intermediate_steps:
            return AgentAction(tool="Simple Math", tool_input=kwargs["input"], log="")
        return AgentFinish(return_values={"output": ""}, log="")

    def aplan(
            self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """
        The function will decide which tool to use
        :param intermediate_steps: Steps the LLM has taken to date, along with observations
        :param kwargs: User inputs.
        :return: Action specifying what tool to use.
        """
        if not intermediate_steps:
            return AgentAction(tool="Simple Math", tool_input=kwargs["input"], log="")
        return AgentFinish(return_values={"output": ""}, log="")


agent = MyCustomAgent()
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

agent_executor.run("generate a math problem")
