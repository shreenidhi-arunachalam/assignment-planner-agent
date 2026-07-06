import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_plan(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are an AI assignment planner.

Step 1: Break tasks into priorities
Step 2: Build a realistic schedule
Step 3: Critique and improve weak parts

Assignments:
{text}
"""
    )
    return response.text