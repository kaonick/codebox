"""
https://litellm.vercel.app/docs/providers/azure
"""
import os
from litellm import acompletion, completion

print(f'HTTP_PROXY={os.getenv("HTTP_PROXY")}')

os.environ["AZURE_API_KEY"] = "b44439faab214afaa606515a51dd04f8"  # os.getenv("OPENAI_API_KEY")
os.environ["AZURE_API_BASE"] = "https://ftc-ap-3000-wu.openai.azure.com/"  # os.getenv("OPENAI_API_BASE")
os.environ["AZURE_API_VERSION"] = "2023-12-01-preview"
# os.environ["AZURE_API_VERSION"] = "vision-preview"
model = "azure/dp-gpt4v"  # "azure/dp-gpt4"



response = completion(
    # api_base="http://localhost:8000", # for llm proxy server
    # model="gpt-4v",
    model=model,
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What’s in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                    }
                }
            ]
        }
    ],
)

print(f"output={response}")
