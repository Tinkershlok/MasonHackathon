import os
from dotenv import load_dotenv
from google import genai
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=['AIzaSyCM4uL_WXs76v7-cIFfuyrCY_OUhhkkY6A'])
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("what is Figma.")
print(response.text)

"""
client = genai.Client(api_key="AIzaSyCM4uL_WXs76v7-cIFfuyrCY_OUhhkkY6A")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="What is Figma"
)
print(response.text)
"""

