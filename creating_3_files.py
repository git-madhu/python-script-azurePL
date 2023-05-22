file_contents = [
    "This is a sample text file created by a Python script.",
    "This is file2 created by a Python script.",
    "This is file3 created by a Python script using Azure Pipelines."
]

for i, content in enumerate(file_contents, start=1):
    file_name = f"file{i}.txt"
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Created {file_name}")
