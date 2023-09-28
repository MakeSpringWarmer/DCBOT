import discord
import os
import asyncio
from pathlib import Path
from discord.ext import commands 
from Cog import cpbl
from keep_alive import keep_alive

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
OWNER_ID = os.environ['DISCORD_TOKEN']

keep_alive()
#client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
bot = commands.Bot(command_prefix = '!', 
                   owner_ids = OWNER_ID,
                   intents = discord.Intents.all())


async def main():
    async with bot:
        await bot.load_extension("Cog.cpbl")
        await bot.load_extension("Cog.dice")
        await bot.start(DISCORD_TOKEN)

asyncio.run(main())