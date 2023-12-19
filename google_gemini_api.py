import google.generativeai as genai

def send_query_to_ai (prompt, API_KEY):
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(e)
        return False

def calculate_token_size(text):
    words = text.split()
    token_count = len(words)
    return token_count
