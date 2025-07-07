import requests
import json
import os

# Ensure the tests directory exists
os.makedirs('tests', exist_ok=True)

with open('main.cpp', 'r') as f:
    cpp_code = f.read()
with open('instructions.yaml', 'r') as f:
    yaml_instructions = f.read()

prompt = f"Please generate Google Test unit tests for the following C++ file according to these YAML instructions:\n\n{yaml_instructions}\n\nC++ code:\n{cpp_code}"

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}
data = {
    "model": "gemma3",
    "prompt": prompt,
    "stream": True  # Streaming is default, but be explicit
}

response = requests.post(url, headers=headers, json=data, stream=True)

responses = []
for line in response.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        try:
            json_data = json.loads(decoded_line)
            responses.append(json_data['response'])
        except json.JSONDecodeError:
            continue  # skip lines that are not valid JSON

combined_response = ''.join(responses)

with open('tests/test_main.cpp', 'w', encoding='utf-8') as f:
    f.write(combined_response)

print("Generated unit tests saved to tests/test_main.cpp")
