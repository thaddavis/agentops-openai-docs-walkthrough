import os
from openai import OpenAI
import agentops
from dotenv import load_dotenv

load_dotenv()

AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")
agentops.init(AGENTOPS_API_KEY, auto_start_session=False)

client = OpenAI()

agentops.start_session(tags=["agentops-docs-openai-examples"])

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    stream=True,
    messages=[{
        "role": "user",
        "content": "Write a haiku about AI and humans working together"
    }]
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="")

agentops.end_session('Success')