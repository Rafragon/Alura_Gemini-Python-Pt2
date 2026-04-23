import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
CHAVE_API = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
