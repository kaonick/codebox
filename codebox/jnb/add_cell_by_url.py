import json

import requests

def add_code_cell_to_notebook(notebook_url, code_content):
    # Define the Jupyter API endpoint for executing code cells
    execute_endpoint = f"{notebook_url.rstrip('/')}/api/contents/"
    headers = {'Accept': 'application/json'}
    # Get the notebook's content
    response = requests.get(execute_endpoint,headers=headers)

    sub = json.loads(response.text)
    print(sub)

    notebook_content = response.json()

    # Create a new code cell
    new_cell = {
        'cell_type': 'code',
        'metadata': {},
        'execution_count': None,
        'source': code_content
    }

    # Append the new cell to the notebook's cells
    notebook_content['content']['cells'].append(new_cell)

    # Save the modified notebook
    response = requests.put(execute_endpoint, json=notebook_content)
    response.raise_for_status()

# Example usage:
notebook_url = 'http://localhost:8888/notebooks/tmp/my_example.ipynb'
code_content = 'print("Hello, World!")'

add_code_cell_to_notebook(notebook_url, code_content)