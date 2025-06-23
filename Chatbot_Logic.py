# chatbot_logic.py

import openai
import os

# Load API key from environment variable for safety
openai.api_key = os.getenv("OPENAI_API_KEY")
print("API KEY:", openai.api_key)

def get_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant trained to help Indiana residents find emergency and public safety services. Provide short, useful, and safe replies."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return "Sorry, I couldn't process your request. Please try again later."
