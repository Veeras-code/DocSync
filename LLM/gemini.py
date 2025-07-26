# gemini.py

import google.generativeai as genai
import google.api_core.exceptions
import time

# Import your API key
from run import api_key

# Configure the Gemini API
genai.configure(api_key=api_key)

# Initialize the model once
model = genai.GenerativeModel("gemini-1.5-pro")

def gemini(prompt: str, retries: int = 3, delay: int = 60) -> str:
    """
    Sends a prompt to the Gemini 1.5 Pro model and returns the response text.
    Retries on quota errors up to `retries` times with `delay` seconds between attempts.
    """
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except google.api_core.exceptions.ResourceExhausted as e:
            print(f"[Gemini] Quota exceeded (attempt {attempt + 1}/{retries}). Retrying in {delay} seconds...")
            time.sleep(delay)
        except google.api_core.exceptions.GoogleAPIError as e:
            print(f"[Gemini] API error: {e}")
            break
        except Exception as e:
            print(f"[Gemini] Unexpected error: {e}")
            break

    return "[Gemini] Error: Could not get a response due to API limits or other issues."
