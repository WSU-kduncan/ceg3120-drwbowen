import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    red_vs_blue_quotes = [
        'We need you to go to the store and get two quarts of elbow grease.',
        'Time is not made out of lines. It is made out of circles; that is why clocks are round.',
        'I am not gonna say I love you....I am gonna say I forget you.',
        'Never say goodbye. If you don’t say goodbye you aren’t really gone. You just aren’t here right now.',
    ]

    if message.content == 'red!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(red_vs_blue_quotes)
        await message.channel.send(response)

client.run(TOKEN)
