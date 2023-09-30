import discord
import os
import asyncio
from pathlib import Path
from discord.ext import commands 
from Cog import cpbl
from keep_alive import keep_alive

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
OWNER_ID = os.environ['OWNER_ID']

bot = commands.Bot(command_prefix = '!', 
                   owner_ids = OWNER_ID,
                   intents = discord.Intents.all())

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"Cog.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"Cog.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"Cog.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")



keep_alive()



async def main():
    async with bot:
        await bot.load_extension("Cog.cpbl")
        await bot.load_extension("Cog.dice")
        await bot.start(DISCORD_TOKEN)

asyncio.run(main())
#client.run(main())
