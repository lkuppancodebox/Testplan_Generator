import google.generativeai as palm

def send_query_to_ai (prompt):
    API_KEY="AIzaSyBtje444t0ysqDzj5JTvLoOXgU4psoC1Ac"
    palm.configure(api_key=API_KEY)

    model_id = [m.name for m in palm.list_models() if "generateText" in m.supported_generation_methods][0]

    completion = palm.generate_text(
        model=model_id,
        prompt=prompt,
        temperature=0.8,
        max_output_tokens=8192
    )
    return completion.result

def calculate_token_size(text):
    words = text.split()
    token_count = len(words)
    return token_count
