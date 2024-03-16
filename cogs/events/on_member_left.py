import discord
from discord.ext import commands

from lib.log import Log

class OnMemberLeft(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self,member:discord.Member):
        await Log(self.bot).info(f"{member.mention} left {member.guild.name}")

def setup(bot:discord.Bot):
    bot.add_cog(OnMemberLeft(bot))