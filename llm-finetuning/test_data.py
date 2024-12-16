import json
def check_outputs(input_file_path, output_file_path):
    total = 0
    valid_rows = []
    with open(input_file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line)
                output = data.get('output')
                
                # Skip rows where output is a number instead of a string
                if isinstance(output, (int, float)):
                    print(f"Line {line_num}: Skipping numeric output (type {type(output)}): {output}")
                    total += 1
                    continue
                    
                # If we get here, the row is valid
                valid_rows.append(line.strip())
                
            except json.JSONDecodeError:
                print(f"Line {line_num}: Skipping invalid JSON")
                continue
    
    # Write valid rows to new file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for row in valid_rows:
            f.write(row + '\n')

    print(f"Cleaned data saved to {output_file_path}")
    print(total)

# Usage
check_outputs('data/combined_data.jsonl', 'data/cleaned_data.jsonl')