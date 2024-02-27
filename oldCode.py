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

SERVER_ID = 1211580675199860746
CHANNEL_ID = 1211583863520763914

TOKEN = "MTIxMTU4MTAyNjk1OTM2NDE0Nw.GCjUcy.mJqt8MNkR1Al27_FStvabQV_c2QJ0bVnfqml-o"
BotId = "1211581026959364147"
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="?",intents=intents)

channel = None  # Define channel as a global variable

@bot.event
async def on_ready():
    global channel
    # Replace SERVER_ID with the ID of the server and CHANNEL_ID with the ID of the channel
    guild = bot.get_guild(SERVER_ID)
    channel = guild.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Bot is now online!")


@bot.command(name="ping")
async def pingTest(ctx):
    await ctx.send("pong 🏓")


@bot.command(name="cleanup")
async def cleanup(ctx = None):
    global channel  # Access the global variable channel
    #await ctx.message.delete()  # Delete the command message
    if channel:
        # Delete messages in the channel
        await channel.purge(limit=20)  # Adjust limit as needed
        # Send farewell message
        await channel.send("The bot is leaving now.")

"""
@atexit.register
def cleanup_0():
    print('running cleanup_0')
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(cleanup(None))
    print("done")
"""

def register_cleanup():
    for signame in {'SIGINT', 'SIGTERM'}:
        signal.signal(getattr(signal, signame), lambda signame, _: asyncio.create_task(cleanup(None)))

# Create an event loop
async def main():
    # Register cleanup for signals
    register_cleanup()

    # Rest of your program code goes here
    # ...

    # If you have an asyncio event loop running within your program,
    # you can use await asyncio.gather(...) to wait for it to complete
    # before the cleanup function runs. Otherwise, you can directly await cleanup_function().

if __name__ == "__main__":
    register_cleanup()
    # Rest of initialization goes here, then start the event loop if necessary.
    asyncio.run(main())

bot.run(TOKEN)