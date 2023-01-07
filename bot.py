import discord
import responses
from discord.ext import commands
import os
from pathlib import Path
from dotenv import dotenv_values

config = dotenv_values(".env")

async def send_message(message, user_message, is_private):
    try:
        response = await responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = config["DISCORD_TOKEN"]
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
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    try:
        client.run(TOKEN)
    except Exception as e:
        print(e)