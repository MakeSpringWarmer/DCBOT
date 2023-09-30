from discord.ext import commands
import discord
from discord.ext.commands import bot
from .crawler.crawler import get_cpbl_now

import datetime
import pytz


class Cpbl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cpbl_now(self, ctx):
        taipei_timezone = pytz.timezone('Asia/Taipei')
        taipei_time = datetime.datetime.now(taipei_timezone)
        game_status_dict = get_cpbl_now()
        embed=discord.Embed(title="中職比分", description=str(taipei_time.strftime("%Y-%m-%d %H:%M:%S ")),url="http://cpbl.com.tw/",color=0x4b83dd)
        if game_status_dict['game_end']:
            for game in game_status_dict['game_end']:
                embed.add_field(name=game, value="比賽結束", inline=False)
        if game_status_dict['game_wait']:
            for game in game_status_dict['game_wait']:
                embed.add_field(name=game, value="比賽未開始", inline=False) 
        if game_status_dict['game_live']:
            for game in game_status_dict['game_live']:
                embed.add_field(name=game, value="比賽進行中", inline=False)
        await ctx.send(embed=embed)
    
async def setup(bot):
    await bot.add_cog(Cpbl(bot))