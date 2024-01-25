"""
https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/gpt-with-vision
"""
# Packages required:
import requests
import json

api_base = 'https://ftc-ap-3000-wu.openai.azure.com/'
deployment_name = 'dp-gpt4v'
API_KEY = 'b44439faab214afaa606515a51dd04f8'

base_url = f"{api_base}openai/deployments/{deployment_name}"
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY
}

# Prepare endpoint, headers, and request body
endpoint = f"{base_url}/chat/completions?api-version=2023-12-01-preview"
data = {
    "messages": [
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "user", "content": [
            {
                "type": "text",
                "text": "Describe this picture:"
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                }
            }
        ] }
    ],
    "max_tokens": 2000
}

# Make the API call
response = requests.post(endpoint, headers=headers, data=json.dumps(data))

print(f"Status Code: {response.status_code}")
print(response.text)
