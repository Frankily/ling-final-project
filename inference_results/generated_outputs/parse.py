import pandas as pd

# Load the CSV file
df = pd.read_csv('base_prompt.csv')

# Function to extract the first line after the first colon in the 'Generated Statements' column and remove quotes
def extract_first_line_and_remove_quotes(statement):
    if pd.isna(statement):
        return statement
    parts = statement.split(':', 1)
    if len(parts) > 1:
        first_line = parts[1].strip().split('\n')[0]
        first_line = first_line.strip('"').strip("'")  # Remove leading and trailing quotes
        return first_line
    return statement.strip('"').strip("'")

# Apply the function to the 'Generated Statements' column
df['Generated Statements'] = df['Generated Statements'].apply(extract_first_line_and_remove_quotes)

# Save the modified DataFrame back to a CSV file
df.to_csv('base_prompt2.csv', index=False)
