import os
import openai

open_ai_host = os.environ.get("OPEN_AI_HOST")
open_ai_api_key = os.environ.get("OPEN_AI_API_KEY")

client = openai.OpenAI(
    base_url=open_ai_host,
    api_key=open_ai_api_key
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={"type": "text"},
    messages=[
        {"role": "system", "content": "你是一个了解中国电商优惠信息的人"},
        {"role": "user", "content": "一般来说，如果我想早点了解淘宝、京东一类的优惠信息，我应该从哪里获取到？"},
    ]
)

print(response)
