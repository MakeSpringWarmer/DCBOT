from discord.ext import commands
import discord
from discord.ext.commands import bot


class Cpbl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cpbl(self, ctx):
        await ctx.send("中華職棒")
    
async def setup(bot):
    await bot.add_cog(Cpbl(bot))