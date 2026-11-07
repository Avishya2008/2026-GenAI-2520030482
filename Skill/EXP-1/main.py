from dotenv import load_dotenv
from google import genai
import os
import time

# Step 1: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Step 2: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 3: Generate response with retry
def generate_response():

    for attempt in range(3):
        try:
            print(f"Attempt {attempt + 1}...")

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents="What is Artificial Intelligence? Explain in simple words."
            )

            print("\nLLM Response:")
            print(response.text)
            return

        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print("Gemini server is busy. Waiting...")
                time.sleep(5 * (attempt + 1))
            else:
                print("Error:", e)
                return

    print("Gemini is still unavailable. Please try again later.")

# Step 4: Run
generate_response()
