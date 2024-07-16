from openai import OpenAI
from config import Config

openai_client = OpenAI(api_key=Config.OPENAI_API_KEY)

def get_openai_response(question):
    response = openai_client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": question}
    ])
    return response.choices[0].message['content']
