import os
from dotenv import load_dotenv
from google import genai
import google.generativeai as genai

load_dotenv()

client=genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def factcheck(user_input):
    global chat_history
    
    chat_history_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])

    response = client.models.generate_content(
        model="gemini-2.0-flash",
    )
    output = response.text
    return output


