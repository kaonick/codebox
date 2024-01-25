import nbformat

def add_code_cell(notebook_path, code_content):
    # Load the existing notebook
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
        notebook = nbformat.read(notebook_file, as_version=4)

    # Create a new code cell
    code_cell = nbformat.v4.new_code_cell(code_content)

    # Add the code cell to the notebook
    notebook['cells'].append(code_cell)

    # Save the modified notebook
    with open(notebook_path, 'w', encoding='utf-8') as notebook_file:
        nbformat.write(notebook, notebook_file)

# Example usage:
notebook_path = 'path/to/your/notebook.ipynb'
code_content = 'print("Hello, World!")'

add_code_cell(notebook_path, code_content)