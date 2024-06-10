import os
import openai

from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()

assistant_id = ""
assistant = None

if assistant_id == "":
    # 创建不了，报错 openai.NotFoundError: Error code: 404 - {'timestamp': 1718012186335, 'status': 404, 'error': 'Not Found', 'path': '//assistants'}
    assistant = client.beta.assistants.create(
        name="二手商品价格助手",
        instructions="帮我计算一些二手商品的价格",
        tools=[{"type": "code_interpreter"}],
        model="gpt-3.5-turbo",
        response_format={"type": "text"},
    )
    print("创建了助手", assistant)
else:
    assistant = client.beta.assistants.retrieve(assistant_id=assistant_id)
    print("使用已有的助手", assistant)
