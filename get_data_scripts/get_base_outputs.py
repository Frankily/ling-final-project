import pandas as pd
import requests
from urllib.parse import quote
def make_get_request(base_url, input_param):
    # URL encode the input parameter
    encoded_input = quote(input_param)
    
    # Construct the full URL
    full_url = f"{base_url}?input={encoded_input}"
    
    # Make the GET request
    response = requests.get(full_url)
    
    return response

df = pd.read_csv("examples_test.csv")
generated_statements = []
for i, row in df.iterrows():
    # print(row[0])
    user_input = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a grammar error correction chatbot.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nFix all mistakes in the text (spelling, punctuation, grammar, etc) and respond with the correct version of the text free of all mistakes. If there are no errors, respond with the original text.\nText: {row[0]}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    url = 'https://praximai--example-axolotl-inference-web.modal.run'
    try:
        response = make_get_request(url, user_input)
        generated_statements.append(response.text)
        # print(f"Status Code: {response.status_code}")
        # print(f"Response: {response.text}")
    except Exception as e:
        generated_statements.append("error in generation")
        print(f"An error occurred: {e}")
    if i % 50 == 0:
        print(i)
df['Generated Statements'] = generated_statements
df.to_csv("finetuned_model_test.csv", index = False)