from dotenv import load_dotenv
from openai import OpenAI
from prompt import SYSTEM_PROMPT
import json

load_dotenv()

client = OpenAI()

messages = [
    {"role": 'system', "content": SYSTEM_PROMPT}
]

while True:
    query = input(">  ")
    messages.append({"role": "user", "content": query})
    
    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        messages=messages
    )
    
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    
    try:
        parsed_response = json.loads(response.choices[0].message.content)
        print("Hitesh Choudhary", parsed_response.get("content"))
    except:
        print("Hitesh Choudhary", response.choices[0].message.content)  # fallback if response is not JSON