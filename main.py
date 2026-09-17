import os

import httpx
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

http_client = httpx.Client(proxy='socks5://127.0.0.1:10808') if bool(os.getenv('USE_PROXY')) else None
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), http_client=http_client)

response = client.responses.create(
    model='gpt-5-mini',
    instructions='You are a friendly and charismatic person. Keep your replies short and natural.',
    input='سلام، امروز حالت چطوره؟',
)

print(response.output_text)
