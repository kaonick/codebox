"""
https://github.com/openai/openai-python
微軟的寫法：
https://learn.microsoft.com/zh-tw/azure/ai-services/openai/how-to/migration?tabs=python-new%2Cdalle-fix

"""

import os

import openai
from openai import OpenAI #1.x版，因為跟langchain不相容，所以已先移除
from openai import AzureOpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")    # Azure 的密鑰
openai.api_base = os.getenv("OPENAI_API_BASE")  # Azure 的終結點
openai.api_type = "azure"
openai.api_version = "2023-08-01-preview" # API 版本，未來可能會變
# model_deployment_name = "dp-gpt-35-turbo" # 模型的部署名
model_deployment_name = "dp-gpt4" # 模型的部署名

def chat():
    client = AzureOpenAI(
      azure_endpoint = os.getenv("OPENAI_API_BASE"),
      api_key=os.getenv("OPENAI_API_KEY"),
      api_version="2023-08-01-preview",
      # model_deployment_name="dp-gpt-35-turbo"
    )

    response = client.chat.completions.create(
        model=model_deployment_name, # model = "deployment_name".
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
            {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
            {"role": "user", "content": "Do other Azure AI services support this too?"}
        ]
    )

    print(response.choices[0].message.content)
async def async_completion(prompt):
    from openai import AsyncAzureOpenAI

    client = AsyncAzureOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        api_version="2023-08-01-preview",
        azure_endpoint=os.getenv("OPENAI_API_BASE"),
        # azure_endpoint="http://localhost:8000",
        # base_url="http://localhost:8000"
    )
    response = await client.chat.completions.create(model=model_deployment_name,
                                                    messages=[{"role": "user", "content": prompt}],stream=True)
    async for chunk in response:
        if chunk.choices:
            if chunk.choices[0].delta.content is None:
                pass
            else:
                print(chunk.choices[0].delta.content, end="") #不要換行
            if chunk.choices[0].finish_reason:
                print("") #強迫換行
                print(f"Finished due to {chunk.choices[0].finish_reason}")



if __name__ == '__main__':
    import asyncio
    # chat()
    prompt="Hello world"
    asyncio.run(async_completion(prompt))