"""
測試 litellm proxy用
"""

import openai
client = openai.OpenAI(
    api_key="anything",
    base_url="http://localhost:8000",
    # base_url="http://localhost:8001/",
    # base_url = "https://llm-proxy-zmve.onrender.com/"
)
# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="gpt-4", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])
print(response)

res2= client.embeddings.create(model="azure-embedding",
                               input=["good morning from litellm"])
print(res2)