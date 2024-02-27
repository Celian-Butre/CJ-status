import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

from datetime import datetime, timedelta
from date_time_event import Untiltime

import threading
import asyncio

import discord,asyncio,os
from discord.ext import commands, tasks

import atexit
import signal

SERVER_ID = INSERT_SERVER_ID_HERE
CHANNEL_ID = INSERT_CHANNEL_ID_HERE
TOKEN = INSERT_BOT_TOKEN_HERE


BotId = "1211581026959364147"
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="?",intents=intents)


@bot.event
async def on_ready():
    # Delete all messages in the channel

    print(1)
    guild = bot.get_guild(SERVER_ID)
    channel = guild.get_channel(CHANNEL_ID)


    await channel.purge()

    # Send initial message
    with open("Open.jpg", "rb") as image_file:
        initial_message = await channel.send("Le CJ est ouvert et il est {}".format(get_current_time()), file=discord.File(image_file))
    
    
    # Schedule the message update loop
    await update_message(initial_message, channel)

async def update_message(message, channel):
    while True:
        try :
        # Update message content
            await message.edit(content="Le CJ est ouvert et il est {}".format(get_current_time()))
        except :
            pass
        # Wait for 1 minute
        await asyncio.sleep(60)

def get_current_time():
    # Get current time in minutes
    return datetime.now().strftime("%H:%M")

bot.run(TOKEN)