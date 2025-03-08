import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key="AIzaSyCM4uL_WXs76v7-cIFfuyrCY_OUhhkkY6A"
    )
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="What is Figma"
)

response

print(response.text)


