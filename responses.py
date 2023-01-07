import random
import os
import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

async def handle_response(message) -> str:
    p_message = message.lower()
    # Load your API key from an environment variable or secret management service
    openai.api_key = config["OPENAI_API_KEY"]


    if p_message.startswith('Hello'):
        return "Hello you, how you doing?"
    # if p_message == "roll":
    #     return str(random.randint(1, 6))

    # if p_message == "!help":
    #     return str(random.randint(1, 6))
    response = openai.Completion.create(model="text-davinci-003", prompt=p_message, temperature=0, max_tokens=150)
    return response['choices'][0]['text']
