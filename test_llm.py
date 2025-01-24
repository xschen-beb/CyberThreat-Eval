import os
from openai import AzureOpenAI

os.environ["LOCAL_ENDPOINT"] = "http://10.150.142.182:9999"
os.environ["PROXY_KEY"] = "59ddb6820482b719e33661ccbfa98042"
client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=50
)
print(response.choices[0].message.content)