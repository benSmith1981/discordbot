import random
import os
import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
class BotResponses:
    def __init__(self):
        self.previousMessage = ""
        self.whichBot = os.environ.get("OPENAIAPIKEY")

    async def handle_response(self, message) -> str:
        p_message = message.lower()
        # Load your API key from an environment variable or secret management service
        if self.whichBot == os.environ.get("OPENAIAPIKEY"):
            openai.api_key = os.environ.get("OPENAIAPIKEY")
            self.whichBot = os.environ.get("OPENAIAPIKEY2")
        else:
            openai.api_key = os.environ.get("OPENAIAPIKEY2")
            self.whichBot = os.environ.get("OPENAIAPIKEY")


        # if p_message.startswith('Hello'):
        #     return "Hello you, how you doing?"
        # if p_message == "roll":
        #     return str(random.randint(1, 6))

        # if p_message == "!help":
        #     return str(random.randint(1, 6))
        print("p_message....." + message)

        response = openai.Completion.create(model="text-davinci-003", prompt=p_message, temperature=0, max_tokens=500)
        print(response)
        self.previousMessage = response['choices'][0]['text']
        if response['choices'][0]['text'] == "":
           response = openai.Completion.create(model="text-davinci-003", prompt="insult me", temperature=0, max_tokens=500)

        return response['choices'][0]['text'] 
