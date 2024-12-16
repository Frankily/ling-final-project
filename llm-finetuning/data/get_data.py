import json
file_paths = ['CLC_FCE.jsonl', 'examples_a3.jsonl', 'examples_a4.jsonl', 'examples_conll14st.jsonl', 'lang8.jsonl']
combined_data = []

for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            combined_data.append(data)

print(f"Total number of JSON objects combined: {len(combined_data)}")

# Optional: Write combined data back into a new JSONL file
output_file = 'combined_data.jsonl'
with open(output_file, 'w', encoding='utf-8') as out_file:
    for obj in combined_data:
        # Write each JSON object as a line
        out_file.write(json.dumps(obj) + '\n')

print(f"Combined data written to {output_file}")