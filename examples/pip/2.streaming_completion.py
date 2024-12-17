from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    stream=True,
    messages=[{
        "role": "user",
        "content": "Write a 16 line poem about AI and humans working together"
    }]
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="")

# print(response.choices[0].message.content)