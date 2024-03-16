import discord
from discord.ext import commands

from lib.log import Log

class OnMemberJoin(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member:discord.Member):
        await Log(self.bot).info(f"{member.mention} joined {member.guild.name}")

def setup(bot:discord.Bot):
    bot.add_cog(OnMemberJoin(bot))