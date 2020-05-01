# connecting to discord and designing templar's logic :)
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# You can use discord client instead of bot with commands:
# client = discord.Client()
bot = commands.Bot(command_prefix='!')


# Gives info in terminal when You are successfully connected to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has joined us on the crusade!')


# sends private message to new users as they occur
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Jerusalem! Deus vult!'
    )


# specific user's message triggers this method
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'Deus Vult':
        response = 'Deus Vult!!!!!!!!!'
        await message.channel.send(response)
    # Prevents from stopping working of other methods:
    await bot.process_commands(message)

# handles errors
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

# let the templar praise the Lord
@bot.command(name='deus_vult')
async def deus_vult(ctx):
    templar_messages = [
        'Why am I even here? This is not a crusade.....',
        'DEUS VULT!',
        'Praise the Lord',
        'Yoy should be praying Son...',
        'Son are You praying there?'
    ]

    response = random.choice(templar_messages)

    await ctx.send(response)


# Returns all commands available
@bot.command(name="commands", description="Returns all commands available")
async def commands(ctx):
    text = "```"
    text += f"List of all templar's commands:\n"
    for command in bot.commands:
        text += f"{command}\n"
    text += "```"
    await ctx.send(text)


bot.run(TOKEN)
