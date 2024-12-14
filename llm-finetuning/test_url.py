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

# Example usage
if __name__ == "__main__":
    url = "https://rpalakkal--example-axolotl-inference-web.modal.run"
    user_input = "Dear Sir or Madam,"
    
    try:
        response = make_get_request(url, user_input)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")