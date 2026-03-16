from openai import OpenAI
from config import api_key
client = OpenAI(
  api_key=api_key
)

response = client.responses.create(
  model="gpt-5-nano",
  input="kim jestes?",
  store=True,
)

print(response.output_text)
