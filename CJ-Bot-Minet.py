import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

TOKEN = "MTIxMTU4MTAyNjk1OTM2NDE0Nw.GCjUcy.mJqt8MNkR1Al27_FStvabQV_c2QJ0bVnfqml-o"


SERVER_ID = INSERT_SERVER_ID_HERE
CHANNEL_ID = INSERT_CHANNEL_ID_HERE

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents)

@tasks.loop(seconds=60)  # Check the channel every minute
async def check_channel():
    print("looping")
    channel = bot.get_channel(CHANNEL_ID)
    async for message in channel.history(limit=None):
        print("here now")
        print("testing Message : " + message.content)
        if message.content.startswith("Le CJ est ouvert et il est "):
            time_str = message.content.split()[-1]
            try:
                message_time = datetime.strptime(time_str, "%H:%M")
                current_time = datetime.now().replace(second=0, microsecond=0)  # Round to the nearest minute
                print('here')
                time_difference = current_time - message_time.replace(year=current_time.year, month=current_time.month, day=current_time.day)
                if time_difference > timedelta(minutes=2):
                    print("passed")
                    await channel.purge()
                    with open("Closed.jpg", "rb") as image_file:
                        await channel.send("Le CJ est fermé", file=discord.File(image_file))
            except ValueError:
                pass  # Ignore messages with invalid time format

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    check_channel.start()

bot.run(TOKEN)
