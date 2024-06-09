import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import  StrOutputParser
from dotenv import load_dotenv
load_dotenv()

openai_host = os.environ.get("OPENAI_HOST")
openai_api_key = os.environ.get("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key, openai_api_base=openai_host)

prompt=PromptTemplate.from_template("{flower}的花语是什么？")
output_parser=StrOutputParser()

chain=prompt|model|output_parser

result=chain.invoke({"flower":"向日葵"})

print(result)
