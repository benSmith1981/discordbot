import discord
from responses import BotResponses
from discord.ext import commands
import os
from pathlib import Path
from dotenv import dotenv_values
import time
config = dotenv_values(".env")

class DragBot:
    def __init__(self):
        self.botResponse = BotResponses()
    async def send_message(self, message, user_message, is_private):
        try:
            # while True:
                response = await self.botResponse.handle_response(user_message)
                await message.author.send(response) if is_private else await message.channel.send(response)
                user_message = response
                print(user_message)
                # time.sleep(3)
               
        except Exception as e:
            print(e)


    def run_discord_bot(self):
        TOKEN = os.environ.get("DISCORDTOKEN")#config["DISCORDTOKEN"]pip
        intents = discord.Intents.default()
        intents.message_content = True 
        intents.messages = True 
        client = commands.Bot(command_prefix = '!', intents = intents)    


        @client.event
        async def on_ready():
            print(f'{client.user} has connected to Discord!')

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return "hello"
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)

            print(f'{username} in {channel}: {user_message}')

            if user_message[0] == '?':
                user_message = user_message[1:]
                await self.send_message(message, user_message, is_private=True)
            else:
                await self.send_message(message, user_message, is_private=False)

        try:
            client.run(TOKEN)
        except Exception as e:
            print(e)