import os
from langchain_core.output_parsers import StrOutputParser # 用于将输出结果解析为字符串
from langchain_core.prompts import ChatPromptTemplate # 用于创建聊天提示模板
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

openai_host = os.environ.get("OPENAI_HOST")
openai_api_key = os.environ.get("OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_template("讲一个关于 {topic} 的故事")

model = ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key, openai_api_base=openai_host)

output_parser = StrOutputParser()

# 使用 | 作为管道，连接各个处理步骤
chain = prompt | model | output_parser

# 调用处理链
message = chain.invoke({"topic": "玫瑰"})
print(message)

# 在一个古老的村庄里，有一个叫做罗萨的女孩，她是村里唯一的花匠。罗萨非常喜欢玫瑰，她的花园里充满了各种颜色和品种的玫瑰。她每天都会精心照料这些玫瑰，用她的爱使得玫瑰开得更加鲜艳、更加美丽。
#
# 然而，村里的人们并不理解她对玫瑰的热爱，他们认为玫瑰只是一种普通的花，为什么要花费那么多的时间和精力去照顾它呢？但罗萨并不介意，她依然每天早起晚归，用她的爱去呵护她的玫瑰。
#
# 就这样，时间悄悄地流逝，罗萨的玫瑰花园越来越美，她的玫瑰也越来越美。村里的人们开始被罗萨的玫瑰吸引，他们开始慢慢地理解罗萨对玫瑰的热爱。
#
# 有一天，邻近的王国的王子来到了这个村庄，他被罗萨的玫瑰花园深深地吸引。他看到罗萨在花园里辛勤的工作，看到她对玫瑰的热爱，他被罗萨的热情和执着深深地打动。
#
# 王子对罗萨说：“你的玫瑰真的很美，你的热情和执着让我非常敬佩。我想请你成为我的王后，让我们一起把这种美丽的玫瑰传播到我们的王国。”
#
# 罗萨被王子的诚意打动，她答应了王子的请求。从此，罗萨成为了王后，她的玫瑰也被带到了全王国，人们都被这种美丽的花朵所吸引，他们开始学习照顾玫瑰，用爱去呵护它。
#
# 这个故事告诉我们，热爱和执着总会被人们所理解和欣赏，就像罗萡的玫瑰一样，它的美丽是由罗萨的爱和执着造就的。