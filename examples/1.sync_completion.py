from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": "Write a marketing slogan for almond butter filled chocolate bar called Heaven"
    }]
)

print(response.choices[0].message.content)