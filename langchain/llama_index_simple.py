# 使用 llama_index 来做个简单的基于 RAG 的 Agent
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from dotenv import load_dotenv

# 加载 openai 的环境变量
load_dotenv()

# 从 assets 文件夹里获取资源
doc = SimpleDirectoryReader("../assets").load_data()
# 为文档建立索引
index = VectorStoreIndex.from_documents(doc)
# 将索引保存到本地
index.storage_context.persist()

query_engine = index.as_query_engine()

# 运行的时候，第一个问题用英文回答，第二个问题用中文回答，所以在第一个问题里加下后面的用中文回答限制
response = query_engine.query("这篇新闻主要讲了什么？请用中文回答。")
print("这篇新闻主要讲了：", response)
response = query_engine.query("是什么让印度的黄金成本大增？")
print("让印度的黄金成本大增的原因是：", response)







