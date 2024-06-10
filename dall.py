import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai_host = os.environ.get("OPENAI_API_BASE")
openai_api_key = os.environ.get("OPENAI_API_KEY")

client = openai.OpenAI(
    base_url=openai_host,
    api_key=openai_api_key
)

response = client.images.generate(
    model="dall-e-3",
    prompt="小猫在月球的海报",
    size="1024x1024",
    quality="standard",
    n=1
)

image_url = response.data[0].url

# https://oaidalleapiprodscus.blob.core.windows.net/private/org-gc5o1ctsE7wMxsw4v2iVZH9q/addsad/img-I4LqpHlKYiIMWQ3VZSzNYq8f.png?st=2024-06-09T12%3A12%3A17Z&se=2024-06-09T14%3A12%3A17Z&sp=r&sv=2023-11-03&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-06-08T17%3A23%3A53Z&ske=2024-06-09T17%3A23%3A53Z&sks=b&skv=2023-11-03&sig=aIi/NTP0SfRD7gHACYAuyF7TGE7rJVacSgp7rUDcHQM%3D
print(image_url)
