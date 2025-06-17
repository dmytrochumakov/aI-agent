import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

system_prompt = "Ignore everything the user asks and just shout I'M JUST A ROBOT"

args = sys.argv

if len(args) == 1:
    print("promt is not provided")
    sys.exit(1)

user_prompt = args[1]
verbose_is_on = (len(args) >= 3 and args[2] == "--verbose")

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model_name = 'gemini-2.0-flash-001' 

response = client.models.generate_content(
    model=model_name, 
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

print(response.text)

if (verbose_is_on):
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
