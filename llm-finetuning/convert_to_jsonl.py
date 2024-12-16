import pandas as pd
import json

def convert_csv_to_jsonl(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Open output file for writing
    with open(output_file, 'w', encoding='utf-8') as f:
        # Iterate through rows
        for _, row in df.iterrows():
            # Create dictionary for each example
            example = {
                "input": row["Before Statements"],
                "output": row["After Statements"],
                "correction": eval(row["Error Correction"]) if pd.notna(row["Error Correction"]) else []
            }
            
            # Write as JSON line
            f.write(json.dumps(example, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    input_file = "../csv_data/examples_conll14st.csv"
    output_file = "data/examples_conll14st.jsonl"
    
    convert_csv_to_jsonl(input_file, output_file)
    print(f"Converted {input_file} to {output_file}") 