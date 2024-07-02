from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor
from langchain.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(temperature=0)

# 需要安装 langchain-community
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 设置提示模板
template = ('''
    '尽你所能用中文回答以下问题。如果能力不够你可以使用以下工具:\n\n'
    '{tools}\n\n
    Use the following format:\n\n'
    'Question: the input question you must answer\n'
    'Thought: you should always think about what to do\n'
    'Action: the action to take, should be one of [{tool_names}]\n'
    'Action Input: the input to the action\n'
    'Observation: the result of the action\n'
    '... (this Thought/Action/Action Input/Observation can repeat N times)\n'
    'Thought: I now know the final answer\n'
    'Final Answer: the final answer to the original input question\n\n'
    'Begin!\n\n'
    'Question: {input}\n'
    'Thought:{agent_scratchpad}' 
    '''
            )

prompt = PromptTemplate.from_template(template)

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    handle_parsing_errrors=True,
    verbose=True
)

agent_executor.invoke({"input":
                       '''目前市场上玫瑰花的一般进货价格是多少？\n
                       如果我在此基础上加价5%，应该如何定价？'''})

