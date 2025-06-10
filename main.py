import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
args = sys.argv

if len(args) == 1:
    print("promt is not provided")
    sys.exit(1)

promt = args[1]
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=promt
)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(response.text)